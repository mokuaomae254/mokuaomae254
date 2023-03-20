import streamlit as st
#st.set_page_config(layout="wide")
st.set_page_config(page_title="Welcome", page_icon=":guardsman:", layout="wide")

def topcryptos():
    import streamlit as st
    import pandas as pd
    import numpy as np
    import time
    import matplotlib
    #import streamlit as st
    import matplotlib.pyplot as plt
    matplotlib.use('TkAgg')
    st.header("Top 100 Cryptocurrencies")
    data=pd.read_csv("satoshi 100 index data58.csv")
    st.dataframe(data)
def scrapping():
	import pandas as pd
	import numpy as np
	import streamlit as st
	import requests
	#dataframe.index.name = "rank"
	r=requests.get("https://cryptoslate.com/coins/",verify=True)
	dataframe=pd.read_html(r.text)[0]
	dataframe.index.name = "rank"
	dataframe=dataframe[["Name","Price","Market Cap","24H Vol","24H %","7D %","30D %","ATH","% ATH"]]
	#dataframe = dataframe.drop(columns=[' '], axis=1)

	dataframe["Name"]=dataframe["Name"].apply(lambda x: x.split("  ")[0])#modify elements(entries) in x
	dataframe["Price"]=dataframe["Price"].apply(lambda x:x.replace(",","").replace("$",""))

	dataframe['Market Cap'] = dataframe['Market Cap'].str.replace(',', '').str.replace('$', '')
	dataframe["Market Cap"] = pd.to_numeric(dataframe["Market Cap"]).abs()
	dataframe["24H Vol"]=dataframe["24H Vol"].str.replace(',', '').str.replace('$', '')
	dataframe["24H Vol"] = pd.to_numeric(dataframe["24H Vol"]).abs()
	dataframe["ATH"]=dataframe["ATH"].str.replace(',', '').str.replace('$', '')

	#TO add % comment 
	dataframe["24H %"]=dataframe["24H %"].str.replace('%', '')
	dataframe["24H %"] = pd.to_numeric(dataframe["24H %"])
	dataframe["7D %"]=dataframe["7D %"].str.replace('%', '')
	dataframe["7D %"] = pd.to_numeric(dataframe["7D %"])
	dataframe["30D %"]=dataframe["30D %"].str.replace('%', '')
	dataframe["30D %"] = pd.to_numeric(dataframe["30D %"])
	dataframe["% ATH"]=dataframe["% ATH"].str.replace('%', '')
	dataframe["% ATH"] = pd.to_numeric(dataframe["% ATH"])
 

	data=dataframe.to_csv("satoshi 100 index data58.csv",index=True )#index true 0-99
	st.dataframe(data)
	dataframe.index.name = "rank"
	#converting column to list
	dataframe=pd.read_csv("satoshi 100 index data58.csv")
	liquidity_risk=[ ]
	for index in dataframe.index:
			if (dataframe["24H Vol"][index])<(dataframe["Market Cap"][index]*0.05):
				liquidity_risk.append("illiquid")

			elif (dataframe["24H Vol"][index])>(dataframe["Market Cap"][index]*0.05) and (dataframe["24H Vol"][index])<=(dataframe["Market Cap"][index]*0.1):
				liquidity_risk.append("fairly liquid")
			elif (dataframe["24H Vol"][index]) > (dataframe["Market Cap"][index] * 0.1) and (dataframe["24H Vol"][index]) <= (dataframe["Market Cap"][index] * 0.3 ):
				liquidity_risk.append("highly liquid") 
			
			elif (dataframe["24H Vol"][index]) > (dataframe["Market Cap"][index] * 0.3) and (dataframe["24H Vol"][index]) <= (dataframe["Market Cap"][index] * 0.5):
				
				liquidity_risk.append("limited long term potential")
			elif (dataframe["24H Vol"][index]) > (dataframe["Market Cap"][index] * 0.5):
				liquidity_risk.append("stay off")
			
	dataframe['liquidity_risk'] = liquidity_risk
	dataframe.loc[dataframe['Name'].isin(['Tether USDT','USD Coin USDC','Binance USD BUSD','Dai DAI','Paxos Standard USDP','TrueUSD TUSD','USDD USDD','Neutrino USD USDN','Gemini Dollar GUSD']), 'liquidity_risk'] = 'stablecoin'
	st.dataframe(dataframe)
	#streamlit run full_scrap.py
def altcoinseason():
    import pandas as pd
    import streamlit as st
    import matplotlib.pyplot as plt

    st.title("Altcoin Season Indicator")

    # Read in dataframe
    dataframe = pd.read_csv("satoshi 100 index data58.csv")

    #Check if the dataframe is empty or not
    if dataframe.empty:
        st.error("Dataframe is empty")
    else:
        # Select top 99 coins
        top_99 = dataframe.head(99)

        # Check if there is "Bitcoin BTC" in the dataframe
        bitcoin_24H_perc = dataframe.loc[dataframe["Name"] == "Bitcoin BTC", "24H %"]
        if bitcoin_24H_perc.empty:
            st.error("Bitcoin BTC not found in dataframe")
        else:
            # Create a new column that calculates the percentage difference between each coin's 24H % and Bitcoin BTC's 24H %
            top_99["Difference"] = top_99["24H %"] - bitcoin_24H_perc.values[0]

            # Create a new column that indicates whether each coin outperforms Bitcoin BTC or not
            top_99["Outperforms"] = top_99["Difference"] > 0

            # Count the number of coins that outperform Bitcoin BTC
            outperformers = top_99["Outperforms"].sum()

            # Calculate the percentage of coins that outperform Bitcoin BTC
            percent_outperform = (outperformers / len(top_99)) * 100

            # Create a pie chart to visualize the results
            labels = ["Altcoin Season", "Bitcoin BTC Season"]
            sizes = [percent_outperform, 100 - percent_outperform]
            st.set_option('deprecation.showPyplotGlobalUse', False)
            plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
            plt.axis('equal')
            st.pyplot()

    #streamlit run last.py
def Crypto_Analytics():
    
    import streamlit as st
    import pandas as pd
    import numpy as np
    import time
    import matplotlib
    #import streamlit as st
    import matplotlib.pyplot as plt
    matplotlib.use('TkAgg')


    #st.set_page_config(layout="wide")
    tab1, tab2, tab3,tab4,tab5,tab6,tab7,tab8,tab9 = st.tabs(["RISK DISCLAIMER","Top 100 Cryptocurrencies","Macro Analysis", "Sentiment Analysis", "portfolio design and risk management","investor connect","comments","market report","Altcoin Season Index"])
    with tab1:
        st.header("RISK DISCLAIMER")
        
        st.text(" \n\r       Before deciding to participate in the Crypto market,you should carefully consider your investment objectives, \n\rlevel of experience and risk appetite.Most importantly, do not invest money you cannot afford to lose.\n\rCrypto trading is very risky and you may lose all or some of your investments. \n\rAll the information, analyses, opinions, news, research, prices, or other information  are provided as general market commentary,\n\rand do not constitute or imply any investment advice.\n\rUnder no circumstances will OpenCipher  accept any liability for any loss or damage, including, any loss of profit, \n\rwhich may arise directly or indirectly from the use of or complete reliance on information contained in the given articles or in any analyses.")

    with tab2:
        #st.header("Top 100 Cryptocurrencies")
        #data=pd.read_csv("satoshi 100 index data31.csv")
        #st.dataframe(data)
        #scrapping()
        topcryptos()
        
        
    

    with tab3:
        st.header("Macro Analysis")
        import streamlit as st
        import matplotlib.pyplot as plt
            #time.sleep(10)
        from PIL import Image
        image = Image.open('Screenshot (32).png')
        image2 = Image.open('Screenshot (34).png')
        st.text("MACRO IS KING")
        st.image(image, caption='UNITED STATES CPI INFLATION DATA')
        st.image(image2, caption='UNITED STATES CORE INFLATION DATA')
        
        
    

    with tab4:
        st.header("Sentiment Analysis")
        import pandas as pd
        import matplotlib.pyplot as plt
        matplotlib.use('TkAgg')
        
            
            #time.sleep(10)
        dataframe = pd.read_csv("BCHAIN-MKPRU.csv")
        dataframe = dataframe.iloc[::-1]
        dataframe['200wma'] = dataframe['Value'].rolling(window = 1400).mean()

        dataframe = dataframe[1400:]
        dates = pd.to_datetime(dataframe['Date'])

        monthly = dataframe[::30]

        distance = monthly['200wma'].pct_change() * 100





        plt.style.use("dark_background")

        plt.semilogy(dates, dataframe['Value'], color = "grey", zorder = 1)
        plt.semilogy(dates, dataframe['200wma'], color = "purple", zorder = 2)

            
        plt.scatter(monthly['Date'], monthly['Value'], c = distance, cmap = 'rainbow', vmin = 0, vmax = 16, zorder = 4 )
            
        cbar = plt.colorbar()
        cbar.set_label("% monthly increase in 200wma")
        cbar.ax.yaxis.set_label_position("left")
            
        
        st.set_option('deprecation.showPyplotGlobalUse', False)

        st.pyplot( )
        

    with tab5:
        st.header("portfolio design and risk management")
        age= st.number_input("enter your age:")    
        #age=int(input("enter your age:"))
        #print("your age is",age)
        #age=18
        if age==18:
            #print("you are of age.")
            st.text("you are of age.")
            #print("allocate 50% of your portfolio to BTC")
            st.text("PORTFOLIO DESIGN AND RISK MANAGEMENT")
            st.text("allocate 50% of your portfolio to crypto and 50 % between the SP500,DJIA and NASDAQ indices")
            import streamlit as st
            import matplotlib.pyplot as plt
            #time.sleep(10)
            
            # Pie chart, where the slices will be ordered and plotted counter-clockwise:
            labels = 'CRYPTO', 'SP500', 'DJIA', 'NASDAQ'
            sizes = [50, 16.67, 16.67, 16.67]
            mycolors = ["yellow", "hotpink", "b", "#4CAF50"]
            explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
            fig1, ax1 = plt.subplots()
            ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90,colors = mycolors)
            ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

            st.pyplot(fig1)
    
            
        elif age>18 and age<=30:
            #print("allocate 50% of your portfolio to BTC")
            st.text("PORTFOLIO DESIGN AND RISK MANAGEMENT")
            st.text("allocate 50% of your portfolio to crypto and 50 % between the SP500,DJIA and NASDAQ indices")
            import streamlit as st
            import matplotlib.pyplot as plt
            #time.sleep(10)
            # Pie chart, where the slices will be ordered and plotted counter-clockwise:
            labels = 'CRYPTO', 'SP500', 'DJIA', 'NASDAQ'
            sizes = [50, 16.67, 16.67, 16.67]
            mycolors = ["yellow", "hotpink", "b", "#4CAF50"]
            explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
            fig1, ax1 = plt.subplots()
            ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90,colors = mycolors)
            ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

            st.pyplot(fig1)
        
        elif age>30 and age<=40:
            #print("allocate 40% of your portfolio to BTC")
            st.text("PORTFOLIO DESIGN AND RISK MANAGEMENT")
            st.text("allocate 40% of your portfolio to crypto and 60 % between the SP500,DJIA and NASDAQ indices")
            import streamlit as st
            import matplotlib.pyplot as plt
            #time.sleep(10)
            # Pie chart, where the slices will be ordered and plotted counter-clockwise:
            labels = 'CRYPTO', 'SP500', 'DJIA', 'NASDAQ'
            sizes = [40, 20, 20, 20]
            mycolors = ["yellow", "hotpink", "b", "#4CAF50"]
            explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
            fig1, ax1 = plt.subplots()
            ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90,colors = mycolors)
            ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

            st.pyplot(fig1)
        
        elif age>40 and age<=50:
            #print("allocate 30% of your portfolio to BTC")
            st.text("PORTFOLIO DESIGN AND RISK MANAGEMENT")
            st.text("allocate 30% of your portfolio to crypto and 70 % between the SP500,DJIA and NASDAQ indices")
            import streamlit as st
            import matplotlib.pyplot as plt
            #time.sleep(10)
            # Pie chart, where the slices will be ordered and plotted counter-clockwise:
            labels = 'CRYPTO', 'SP500', 'DJIA', 'NASDAQ'
            sizes = [30, 23.33, 23.33, 23.33]
            mycolors = ["yellow", "hotpink", "b", "#4CAF50"]
            explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
            fig1, ax1 = plt.subplots()
            ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90,colors = mycolors)
            ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

            st.pyplot(fig1)
        

        elif age>50 and age<=60:
            #print("allocate 20% of your portfolio to BTC")
            st.text("PORTFOLIO DESIGN AND RISK MANAGEMENT")
            st.text("allocate 20% of your portfolio to crypto and 80 % between the SP500,DJIA and NASDAQ indices")
            import streamlit as st
            import matplotlib.pyplot as plt
            #time.sleep(10)
            # Pie chart, where the slices will be ordered and plotted counter-clockwise:
            labels = 'CRYPTO', 'SP500', 'DJIA', 'NASDAQ'
            sizes = [20, 26.67, 26.67, 26.67]
            mycolors = ["yellow", "hotpink", "b", "#4CAF50"]
            explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
            fig1, ax1 = plt.subplots()
            ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90,colors = mycolors)
            ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

            st.pyplot(fig1)
        
        
        elif age>60 and age<=70:
            #print("allocate 10% of your portfolio to BTC")
            st.text("PORTFOLIO DESIGN AND RISK MANAGEMENT")
            st.text("allocate 10% of your portfolio to crypto and 90 % between the SP500,DJIA and NASDAQ indices")
            import streamlit as st
            import matplotlib.pyplot as plt
            #time.sleep(10)
            # Pie chart, where the slices will be ordered and plotted counter-clockwise:
            labels = 'CRYPTO', 'SP500', 'DJIA', 'NASDAQ'
            sizes = [10, 30, 30, 30]
            mycolors = ["yellow", "hotpink", "b", "#4CAF50"]
            explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
            fig1, ax1 = plt.subplots()
            ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90,colors = mycolors)
            ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

            st.pyplot(fig1)
        
        
        elif age>70 and age<=200:
            #print("allocate 5% of your portfolio to BTC")
            st.text("PORTFOLIO DESIGN AND RISK MANAGEMENT")
            st.text("allocate 5% of your portfolio to crypto and 95 % between the SP500,DJIA and NASDAQ indices")
            import streamlit as st
            import matplotlib.pyplot as plt
            #time.sleep(10)
            # Pie chart, where the slices will be ordered and plotted counter-clockwise:
            labels = 'CRYPTO', 'SP500', 'DJIA', 'NASDAQ'
            sizes = [5, 31.67, 31.67, 31.67]
            mycolors = ["yellow", "hotpink", "b", "#4CAF50"]
            explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
            fig1, ax1 = plt.subplots()
            ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90,colors = mycolors)
            ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
            st.pyplot(fig1)
            
        
        else:
            print("can not access the model.")
        
    
    
    with tab6:
        st.header("investor connect")
        st.text("share your charts below")
        uploaded_file = st.file_uploader("Choose a file")
        st.text("Coming Soon")
        st.image("bitcoin heatmap.png", width=800)
    with tab7:
        st.header("comments")
        comments = st.text_input('Leave a Comment Below: ')
        st.button('Submit Comment')
    
    with tab8:
        import pandas as pd
        import numpy as np
        import streamlit as st

        import base64
        from io import BytesIO
        from matplotlib.backends.backend_pdf import FigureCanvasPdf as FigureCanvas

        #from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
        from matplotlib.figure import Figure



            #streamlit run downloading_report.py
        dataframe = pd.read_csv("satoshi 100 index data58.csv")
        #st.header("Top 100 Cryptocurrencies")
        st.header("Cryptocurrency Market Daily,Weekly and Monthly Report ")
        #data=pd.read_csv("satoshi 100 index data29.csv")
        #st.dataframe(dataframe)
        
        #print(df)
        i=0
        st.subheader("Today's Winners ")
        for i in range(10):
            
            data=dataframe.sort_values(by=['24H %'], ascending=False)
        st.dataframe(data)
        df = pd.DataFrame(data)

        if st.button("Download CSV1"):
            csv = df.to_csv(index=False)
            b64 = base64.b64encode(csv.encode()).decode()
            href = f'<a href="data:file/csv;base64,{b64}" download="mydata.csv">Download CSV File</a>'
            st.markdown(href, unsafe_allow_html=True)
        #csv_downloader()
        st.subheader("Today's Biggest Losers ")
        for i in range(10):
            
            data=dataframe.sort_values(by=['24H %'])
        st.dataframe(data)
        df = pd.DataFrame(data)

        if st.button("Download CSV2"):
            csv = df.to_csv(index=False)
            b64 = base64.b64encode(csv.encode()).decode()
            href = f'<a href="data:file/csv;base64,{b64}" download="mydata.csv">Download CSV File</a>'
            st.markdown(href, unsafe_allow_html=True)
        #csv_downloader()
        st.subheader("This week's Winners ")
        for i in range(10):
        
            data=dataframe.sort_values(by=['7D %'], ascending=False)
        st.dataframe(data)
        df = pd.DataFrame(data)

        if st.button("Download CSV3"):
            csv = df.to_csv(index=False)
            b64 = base64.b64encode(csv.encode()).decode()
            href = f'<a href="data:file/csv;base64,{b64}" download="mydata.csv">Download CSV File</a>'
            st.markdown(href, unsafe_allow_html=True)
        #csv_downloader()
        st.subheader("This week's Biggest lossers ")
        for i in range(10):
            
            data=dataframe.sort_values(by=['7D %'])
        st.dataframe(data)
        df = pd.DataFrame(data)

        if st.button("Download CSV4"):
            csv = df.to_csv(index=False)
            b64 = base64.b64encode(csv.encode()).decode()
            href = f'<a href="data:file/csv;base64,{b64}" download="mydata.csv">Download CSV File</a>'
            st.markdown(href, unsafe_allow_html=True)
        #csv_downloader()
        st.subheader("This Month's Winners ")
        for i in range(10):
            
            data=dataframe.sort_values(by=['30D %'], ascending=False)
        st.dataframe(data)
        df = pd.DataFrame(data)

        if st.button("Download CSV5"):
            csv = df.to_csv(index=False)
            b64 = base64.b64encode(csv.encode()).decode()
            href = f'<a href="data:file/csv;base64,{b64}" download="mydata.csv">Download CSV File</a>'
            st.markdown(href, unsafe_allow_html=True)
        #csv_downloader()
        st.subheader("This Month's Biggest Losers ")
        for i in range(10):
            
            data=dataframe.sort_values(by=['30D %'])
        st.dataframe(data)
        df = pd.DataFrame(data)

        if st.button("Download CSV6"):
            csv = df.to_csv(index=False)
            b64 = base64.b64encode(csv.encode()).decode()
            href = f'<a href="data:file/csv;base64,{b64}" download="mydata.csv">Download CSV File</a>'
            st.markdown(href, unsafe_allow_html=True)
        #csv_downloader()
        #streamlit run market_report.py
    with tab9:
        altcoinseason()           
            
        

        
    #streamlit run cv.py
        

    #streamlit run finalc.py
    
    
    
def create_account():
    st.title("Create an Account")
    first_name = st.text_input("Enter your first name:")
    last_name = st.text_input("Enter your last name:")

    if first_name and last_name:
        username = first_name.lower() + "." + last_name.lower()
        st.success("Your username is: " + username)
    else:
        st.error("Please enter both your first and last name.")

    email = st.text_input("Enter your email address:")
    password = st.text_input("Enter a password:", type='password')
    password_confirmation = st.text_input("Confirm your password:", type='password')

    if password and password_confirmation and password == password_confirmation:
        st.success("Password set successfully!")
    else:
        st.error("Passwords do not match. Please try again.")

    if st.button("Submit"):
        if all([first_name, last_name, email, password]):
            st.success("Account created!")
        else:
            st.error("Please complete all fields.")

def login():
    st.title("Login")
    username = st.text_input("Enter your username:")
    password = st.text_input("Enter your password:", type='password')

    if st.button("Login"):
        if username and password:
            st.success("Logged in as: " + username)
            #Crypto_Analytics()
        else:
            st.error("Please enter both your username and password.")

#st.set_page_config(page_title="Welcome", page_icon=":guardsman:", layout="wide")

st.sidebar.title("Navigation")

menu = ["Homepage", "Create an account", "Login","Crypto Analytics","About The Team"]
choice = st.sidebar.selectbox("Select an option", menu)

if choice == "Homepage":
    st.write("Welcome to our platform!")
    topcryptos()
    

elif choice == "Create an account":
    create_account()

elif choice == "Login":
    login()
    
    
elif choice=="Crypto Analytics":
    Crypto_Analytics()
    
#streamlit run signup1.py