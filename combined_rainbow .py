import pandas as pd
import streamlit as st
import numpy as np
#import beautifulsoup4 as bs
import requests
#page = requests.get(url, verify=False)
#add website certificate to solve the error
r=requests.get("https://cryptoslate.com/coins/",verify=False)
df=pd.read_html(r.text)[0]
df=df[["Name","Price","Market Cap","24H Vol","24H %","7D %","30D %","ATH","% ATH"]]
#l risk= ['Delhi', 'Bangalore', 'Chennai', 'Patna']
  
# Using 'Address' as the column name
# and equating it to the list
#df['lrisk'] =df['lrisk']
#+[["l risk","i confidence","LTPP"]]
df["Name"]=df["Name"].apply(lambda x: x.split("  ")[0])#modify elements(entries) in x
df["Price"]=df["Price"].apply(lambda x:x.replace(",","").replace("$",""))

#df1['Avg_Annual'] = df1['Avg_Annual'].str.replace(',', '')
df['Market Cap'] = df['Market Cap'].str.replace(',', '').str.replace('$', '')
df["24H Vol"]=df["24H Vol"].str.replace(',', '').str.replace('$', '')
df["ATH"]=df["ATH"].str.replace(',', '').str.replace('$', '')
#TO add % comment 
df["24H %"]=df["24H %"].str.replace('%', '')
df["7D %"]=df["7D %"].str.replace('%', '')
df["30D %"]=df["30D %"].str.replace('%', '')
df["% ATH"]=df["% ATH"].str.replace('%', '')
#df['Circulating Supply'] = df['Circulating Supply'].replace(',','')
#df4["Market Cap"]=df4["Market Cap"].apply(lambda x:x.replace(",","").replace("$",""))
df.to_csv("satoshi 100 index data18.csv",index=True )#index true 0-99
#df.isnull()#testing for NA or NAN values
#df.isnull().sum()#nv in a column
#df.shape reads no of columns and rows
#df.isnull().sum().sum()#nv in total set

print(df )
#df2=df.fillna(method="pad")
#df['Market Cap']=df['Market Cap'].interpolate(method='linear')
def myindicator():
    import pandas as pd
    import matplotlib.pyplot as plt
   
    #age=int(input("enter your age:"))

    df = pd.read_csv("BCHAIN-MKPRU.csv")
    df = df.iloc[::-1]
    df['200wma'] = df['Value'].rolling(window = 1400).mean()
#df['300wma'] = df['Value'].rolling(window = 1400).mean()
    df = df[1400:]
    dates = pd.to_datetime(df['Date'])

    monthly = df[::30]

    distance = monthly['200wma'].pct_change() * 100

#distance = monthly['300wma'].pct_change() * 100



    plt.style.use("dark_background")

    plt.semilogy(dates, df['Value'], color = "grey", zorder = 1)
    plt.semilogy(dates, df['200wma'], color = "purple", zorder = 2)
#plt.semilogy(dates, df['300wma'], color = "green", zorder = 3)

    plt.scatter(monthly['Date'], monthly['Value'], c = distance, cmap = 'rainbow', vmin = 0, vmax = 16, zorder = 4 )

    cbar = plt.colorbar()
    cbar.set_label("% monthly increase in 200wma")
    cbar.ax.yaxis.set_label_position("left")



    plt.show()
age=int(input("enter your age:"))
#print("your age is",age)
#age=18
if age==18:
    print("you are of age.")
    print("allocate 50% of your portfolio to BTC")
    myindicator()
        
elif age>18 and age<=30:
    print("allocate 50% of your portfolio to BTC")
    myindicator()
elif age>30 and age<=40:
    print("allocate 40% of your portfolio to BTC")
    myindicator()
elif age>40 and age<=50:
    print("allocate 30% of your portfolio to BTC")
    myindicator()

elif age>50 and age<=60:
    print("allocate 20% of your portfolio to BTC")
    myindicator()
    
elif age>60 and age<=70:
    print("allocate 10% of your portfolio to BTC")
    myindicator()
    
elif age>70 and age<=200:
    print("allocate 5% of your portfolio to BTC")
    myindicator()
    
else:
    print("can not access the model.")
    