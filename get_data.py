import requests
import pandas as pd
import io

land_list = ['A', 'F']
season_list = ['S1', 'S2', 'S3', 'S4']
year_list = ['102', '103', '104', '105', '106', '107', '108', '109', '110', '111', '112']

for year in year_list:
    for season in season_list:
        for land in land_list:
            url = f'https://plvr.land.moi.gov.tw//DownloadSeason?season={year}{season}&fileName={land}_lvr_land_A.csv'

            data = requests.get(url)

            df = pd.read_csv(io.StringIO(data.text))

            df.to_csv(f'{land}_lvr_land_A_{year}{season}.csv')