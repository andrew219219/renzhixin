import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('max_colwidth', 300)
pd.set_option('display.unicode.ambiguous_as_wide', True)
# pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width', 1000)

headers = [chr(x) for x in range(65, 91)]
df = pd.read_excel('data/SI 管理费用.xls', sheet_name='审定表', header=None)

print(df[0].str.findall)



# df.columns = headers[0: len(df.columns)]
# df.index = df.index + 1
#
# print(df.loc[11, 'M'])
# print(df)
