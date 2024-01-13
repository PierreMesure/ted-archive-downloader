import pandas as pd
import services.ted.download_data as download_data
import services.ted.clean_data as clean_data
from services.writer import Writer

data = []

df = download_data.get_cpv_codes_from_simap("SV")
df = clean_data.remove_check_digits(df)
df.to_csv('cpv.csv')

df = pd.read_csv('cpv.csv', dtype={'CODE': object})

data = clean_data.build_tree(df, df, 1)

Writer.write_json(data, 'cpv_sv.json')

