import pandas as pd

csv_file = pd.read_csv(r'.\CSV\TLG_SystemArchive_20161120_000000_-_20161121_000000.csv', delimiter=';')

csv_file.to_excel(r'test.xlsx', index=None, header=True)