from strsimpy.normalized_levenshtein import NormalizedLevenshtein
from pandas import read_excel
import pandas as pd
import os

my_sheet = 'Planilha1' # change it to your sheet name, you can find your sheet name at the bottom left of your excel file
file_name = 'produtos.xlsx' # change it to the name of your excel file
df = read_excel(file_name, sheet_name = my_sheet)
print(df.head()) # shows headers with top 5 rows

results = []

for index, row in df.iterrows():
    descricao = row['descricao']
    sku = row['sku']

    # read download directory and exxtract file names
    distance = 9999999;
    for filename in os.listdir('./Downloads/Vitamina'):
        levenshtein = NormalizedLevenshtein()
        actualDistance = levenshtein.distance(row['descricao'], filename)
        if actualDistance < distance:
            distance = actualDistance
            minorDistanceFile = filename

    results.append({
        'sku': sku,
        'descricao': descricao,
        'filename': minorDistanceFile,
        'distance': distance
    })

# create result file
df = pd.DataFrame(results)
df.to_excel('result.xlsx', index=False)

