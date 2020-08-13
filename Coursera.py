import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df_can = pd.read_excel('https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DV0101EN/labs/Data_Files/Canada.xlsx',
                       sheet_name='Canada by Citizenship',
                       skiprows=range(20),
                       skipfooter=2)
##print(df_can.isna().sum())
##print(type(df_can.columns))
df_can.columns.tolist()
##print(df_can.columns)
# size of dataframe (rows, columns)
##print(df_can.shape)
# in pandas axis=0 represents rows (default) and axis=1 represents columns.
df_can.drop(['AREA','REG','DEV','Type','Coverage'], axis=1, inplace=True)
##print(df_can.head(2))
df_can.rename(columns={'OdName':'Country', 'AreaName':'Continent', 'RegName':'Region'},inplace=True)
##print(df_can.head())
df_can["Total"]=df_can.sum(axis=1)
##print(df_can.head())
#returns a series, same a df["Country"]
##print(df_can.Country)
#list of series is called dataframe
##print(df_can[["Country","Continent","Region"]])
#Inorder to search by column th above method is used
#Inorder ot search by row, then we will have to setindex to any of column
df_can.set_index("Country",inplace=True)
print(df_can.head())
print(df_can.columns.values)
#for locating by column
#converting column names to integers to avoid confusion
df_can.columns=list(map(str,df_can.columns))
years = list(map(str,range(1980,2014)))
print(years)
print(df_can.loc["Afghanistan",years])
#create conditions and can pass into the dataframe
#for multiple conditions looping use '&'(and) and '|'(or)
# parentheses is important
condition = ((df_can["Continent"] == "Asia") & (df_can["Region"] =="Southern Asia"))
print(df_can[condition])
###For plotting
bhutan = df_can.loc["Bhutan",years]
#only one returns a series with years as indices, this can be plotted happily
print(bhutan)
bhutan.plot(kind="line")

plt.legend()
plt.xlabel("years")
plt.ylabel("migrants")
plt.title("migrants list Bhutan")
plt.show()
#but when multiple data is extracted thn dataframe is returned and it cannnot be plotted
china_india = df_can.loc[["China","India"],years]
china_india.plot(kind="line")
plt.show()
#the plot is not correct, it has to be readjusted by transposing as index line are countries
china_india = china_india.transpose()
china_india.plot(kind="line")
plt.show()

## getting top 5 in list and plotting them
df_sorted = df_can.sort_values("Total",ascending=False)
print(df_sorted.head())
df_top = df_sorted.head(5)
print(df_top[years])
print(df_top[years].transpose())
df_top[years].transpose().plot(kind="line")
#print(df_top[["1980","1981"]])
#.transpose().plot(kind="line")
plt.show()