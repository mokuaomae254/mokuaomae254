import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd


weightings1 = {"SPY":"100"}
weightings2 = {"SPY":"95","BTC-USD":"5"}


members = ["BTC-USD","SPY"]


def PortfolioCalc(weightings, data, name):
  data[name] = sum([  int(weightings[x])*data[x]/100 for x in list(weightings.keys())   ])
  return data

basedata = yf.Ticker(members[0]).history(period="max").reset_index()[["Date","Open"]]
basedata["Date"] = pd.to_datetime(basedata["Date"])
basedata = basedata.rename(columns = {"Open":members[0]})


if (len(members)>1):
  for x in range(1,len(members)):
    newdata = yf.Ticker(members[x]).history(period="max").reset_index()[["Date","Open"]]
    newdata["Date"] = pd.to_datetime(newdata["Date"])
    newdata = newdata.rename(columns = {"Open":members[x]})
    basedata = pd.merge(basedata, newdata, on="Date")


basedata = basedata[  basedata["Date"] > "2016-01-01"]


print(basedata)

for x in members:
  basedata[x] = basedata[x]/(basedata[x].iloc[0])

basedata = PortfolioCalc(weightings1, basedata, "crypto1")
basedata = PortfolioCalc(weightings2, basedata, "crypto2")

#for x in members:
  #plt.semilogy(basedata["Date"], basedata[x], label=x)

plt.style.use("dark_background")

plt.plot(basedata["Date"], basedata["crypto1"], label = "100% s&p500")
plt.plot(basedata["Date"], basedata["crypto2"], label = "95% s&p500, 5% BTC")

plt.legend(loc="upper left")
plt.show()

metcalfe-reddit-valuations
import plotly.express as px
import re
import requests
import pandas as pd
import json
import numpy as np

subs = pd.read_csv("subreddits.csv")

gecko = list(subs["gecko-name"])
subreddits = list(subs["reddit"])
subSize = []
mktcap = []

for x in subreddits:
  data = requests.get("https://frontpagemetrics.com/r/" + x).text
  data = re.findall("h2 class=.*",data)
  data = re.findall(">[0-9,]*<",data[0])[0]
  data = data.replace(">","").replace("<","").replace(",","")
  subSize.append(int(data))

subs["size"] = subSize

for x in gecko:
  data = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=" + x +"&order=market_cap_desc&per_page=100&page=1&sparkline=false")
  mktcap.append(int(data.json()[0]["market_cap"]))

subs["mktcap"] = mktcap
subs["kvalue"] = subs["mktcap"]/(subs["size"]**2)

fig = px.scatter(subs, x="size", y="mktcap",
	         size="kvalue",
                 hover_name="gecko-name", text = "gecko-name",template="plotly_dark",log_x=True,log_y=True,size_max=200)

fig.update_xaxes(title_text='Reddit Subscribers',
                 showgrid=False,
                 title_font = {"size": 30})
fig.update_yaxes(title_text='<br>Marketcap',
                 showgrid=False,
                 title_font = {"size": 30})

fig.update_layout(title_text="Relative valuations by Metcalfe's law", 
                  title_font_size=45,
                  title_yanchor="top",
                  title_pad_t=30,
                  title_pad_b=30)

fig.show()




