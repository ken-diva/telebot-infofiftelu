import pandas

file = ("test.xlsx")
data = pandas.read_excel(file)
data_baru = data.loc[data['kode'] == 'BBB']
aaa = data_baru["no.hp"]
print(aaa.to_string(index=False))