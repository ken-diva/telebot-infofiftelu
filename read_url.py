import pandas as pd

SHEET_ID = '1FUO33IdeaxgFnEfyb0ELkKo6fBBw5JyWH0zfdHH6Stg'
SHEET_NAME = 'mbkm'
url = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}'
df = pd.read_csv(url)
link = []
ket = []
mess = []
for x in df["Link"]:
    link.append(x)
for x in df["Keterangan"]:
    ket.append(x)
mess.append(link[0] + " \n" + ket[0])
print(mess)
# print(df["Perintah"])