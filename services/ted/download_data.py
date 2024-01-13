import pandas as pd
from io import BytesIO
from zipfile import ZipFile
from urllib.request import urlopen

URL_DATA_TED = "https://data.europa.eu/api/hub/store/data/ted-contract-award-notices-{}.zip"

URL_CPV_CODES = "https://simap.ted.europa.eu/documents/10184/36234/cpv_2008_xls.zip"

def get_notices_from_ted(year):
    return pd.read_csv(
        URL_DATA_TED.format(year),
        low_memory=False
                      )

def get_cpv_codes_from_simap(language):
    zipfile = ZipFile(BytesIO(urlopen(URL_CPV_CODES).read()))
    data = pd.read_excel(zipfile.open(zipfile.namelist()[0]))
    data.rename(columns = {language:'name'}, inplace = True)
    return data[['CODE', 'name']]
