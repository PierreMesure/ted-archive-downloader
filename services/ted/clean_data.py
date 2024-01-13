COLUMNS = ['CPV', 'TITLE']

def keep_columns(raw_df, columns = COLUMNS):
    return raw_df[columns]

def remove_check_digits(df):
    df['CODE'] = df['CODE'].str[:-2]
    return df

def get_cpv_level(cpv_code):
    if '-' in cpv_code:
        cpv_code = cpv_code[:-2]

    cpv_code = cpv_code[2:]

    return 7 - cpv_code.count('0')

def get_one_digit_with_leading_zero(num):
    return str(num) if num >= 10 else '0{}'.format(num)

def build_tree2(list):
    tree = []
    for i in range(0, 10):
        for j in range(1, 10):
            second_level = '{}{}000000'.format(i, j)
            if second_level not in list:
                continue

            tree[second_level] = []

            for k in range(1, 10):
                third_level = '{}{}{}00000'.format(i, j, k)
                if third_level not in list:
                    continue

                tree[second_level][third_level] = []

                for l in range(1, 10):
                    fourth_level = '{}{}{}{}0000'.format(i, j, k, l)
                    if fourth_level not in list:
                        continue

                    tree[second_level][third_level][fourth_level] = []
                    for m in range(1, 10):
                        fifth_level = '{}{}{}{}{}000'.format(i, j, k, l, m)
                        if fifth_level not in list:
                            continue

                        tree[second_level][third_level][fourth_level][fifth_level] = []

                        for n in range(1, 10):
                            tree[second_level][third_level][fourth_level][fifth_level].append('{}{}{}{}{}{}00'.format(i, j, k, l, m, n))

def build_tree(df, children, level):
    if 'CODE' in children:
        children = children['CODE']

    if level == 6:
        last_level = []
        for child in children:
            last_level.append({
                'cpv': child,
                'name': df.loc[df['CODE'] == child, 'name'].item(),
                'children': None
            })
        return last_level
    else:
        intermediate_level = []
        for child in children:
            if get_cpv_level(child) != level:
                continue

            grandchildren = [grandchild for grandchild in children if grandchild.startswith(child[:level + 1])]

            intermediate_level.append({
                'cpv': child,
                'name': df.loc[df['CODE'] == child, 'name'].item(),
                'children': build_tree(df, grandchildren, level + 1)
            })

        return intermediate_level


def get_list_of_children(parent):
    return ''

def build_subtree(children):
    last_level = []
    for child in children:
        last_level.append({
            'cpv': child,
            'children': None
        })
