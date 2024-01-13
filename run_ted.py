import pandas as pd
import services.ted.download_data as download_data
import services.ted.clean_data as clean_data

data = []
for year in range(2006, 2021 + 1):
    print('Fetching data for year {}...'.format(year))
    df = download_data.get_notices_from_ted(year)
    df = clean_data.keep_columns(df)
    df = df.dropna()

    if not df.empty:
        data.append(df)

df = pd.concat(data)
df.to_parquet('training_data.parquet')
print(df)
