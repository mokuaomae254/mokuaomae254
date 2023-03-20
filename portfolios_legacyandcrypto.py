def crypto_portfolio():
        import streamlit as st
        import matplotlib.pyplot as plt
        if age>=18  and age<=200 :
            #st.header("Portfolio Design and Risk Management")
            st.subheader("Crypto portfolio")

            income = st.number_input("Enter your annual income:")
            investment = income * 0.1
            st.text("Invest 10% of your income, or $" + str(investment) + ", in crypto.")

            if income > 100 :
                #st.text("Allocate 30% of your portfolio to layer 1 and the remaining 70% to be equally allocated among layer 0, layer 2 and layer 3.")
                labels = 'LAYER 1', 'LAYER 0', 'LAYER 2', 'LAYER 3','INFRA COINS','AI COINS'
                sizes = [30, 10, 20, 20,10,10]
                mycolors = ["yellow", "hotpink", "purple", "green","pink","maroon"]
                explode = (0, 0, 0, 0,0,0)
                fig1, ax1 = plt.subplots()
                ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90, colors = mycolors)
                ax1.axis('equal')
                st.pyplot(fig1)

            elif income > 100 and income <= 1000:
                #st.text("Allocate 30% of your portfolio to layer 1 and the remaining 70% to be equally allocated among layer 0, layer 2 and layer 3.")
                labels = 'LAYER 1', 'LAYER 0', 'LAYER 2', 'LAYER 3','INFRA COINS','AI COINS'
                sizes = [10, 20, 20, 20,10,20]
                mycolors = ["yellow", "hotpink", "purple", "green","pink","maroon"]
                explode = (0, 0, 0, 0,0,0)
                fig1, ax1 = plt.subplots()
                ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90, colors = mycolors)
                ax1.axis('equal')
                st.pyplot(fig1)

            elif income > 1000 and income <= 10000:
                #st.text("Allocate 30% of your portfolio to layer 1 and the remaining 70% to be equally allocated among layer 0, layer 2 and layer 3.")
                labels = 'LAYER 1', 'LAYER 0', 'LAYER 2', 'LAYER 3','INFRA COINS','AI COINS'
                sizes = [20, 10, 20, 20,20,10]
                mycolors = ["yellow", "hotpink", "purple", "green","pink","maroon"]
                explode = (0, 0, 0, 0,0,0)
                fig1, ax1 = plt.subplots()
                ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90, colors = mycolors)
                ax1.axis('equal')
                st.pyplot(fig1)
            elif income > 10000 and income <= 100000:
                #st.text("Allocate 30% of your portfolio to layer 1 and the remaining 70% to be equally allocated among layer 0, layer 2 and layer 3.")
                labels = 'LAYER 1', 'LAYER 0', 'LAYER 2', 'LAYER 3','INFRA COINS','AI COINS'
                sizes = [30, 10, 20, 20,10,10]
                mycolors = ["yellow", "hotpink", "purple", "green","pink","maroon"]
                explode = (0, 0, 0, 0,0,0)
                fig1, ax1 = plt.subplots()
                ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90, colors = mycolors)
                ax1.axis('equal')
                st.pyplot(fig1)
            elif income > 100000 and income <= 1000000:
                #st.text("Allocate 30% of your portfolio to layer 1 and the remaining 70% to be equally allocated among layer 0, layer 2 and layer 3.")
                labels = 'LAYER 1', 'LAYER 0', 'LAYER 2', 'LAYER 3','INFRA COINS','AI COINS'
                sizes = [40, 10, 20, 10,10,10]
                mycolors = ["yellow", "hotpink", "purple", "green","pink","maroon"]
                explode = (0, 0, 0, 0,0,0)
                
                fig1, ax1 = plt.subplots()
                ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90, colors = mycolors)
                ax1.axis('equal')
                st.pyplot(fig1)
            elif income > 1000000 and income <= 2000000:
                #st.text("Allocate 30% of your portfolio to layer 1 and the remaining 70% to be equally allocated among layer 0, layer 2 and layer 3.")
                labels = 'LAYER 1', 'LAYER 0', 'LAYER 2', 'LAYER 3','INFRA COINS','AI COINS'
                sizes = [50, 10, 10, 10,10,10]
                mycolors = ["yellow", "hotpink", "purple", "green","pink","maroon"]
                explode = (0, 0, 0, 0,0,0)
                fig1, ax1 = plt.subplots()
                ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90, colors = mycolors)
                ax1.axis('equal')
                st.pyplot(fig1)
            elif income >  2000000:
                st.text("consult with Hedge Funds,private Equity Firms or Venture Capitals as you are regarded as an accredited investor An accredited investor is an individual or entity that meets certain financial and income criteria as established by the Securities and Exchange Commission (SEC). The criteria are intended to identify individuals and entities that have the financial sophistication and ability to bear the economic risks of investing in securities that are not registered with the SEC. Examples of accredited investors include individuals with a net worth of over $1 million (excluding the value of their primary residence), or an annual income of over $200,000 for the past two years (or $300,000 when combined with a spouse). Institutions such as banks, insurance companies, and investment companies also qualify as accredited investors.")
            else:
                st.text("The minimum amount you can buy in an exchange is 10 USD")	
            #"""streamlit run crypto_portfolio.py
 
import streamlit as st
import matplotlib.pyplot as plt

#st.header("portfolio design and risk management")
st.subheader("Crypto and the legacy market portfolio")
age= st.number_input("enter your age:")    
#age=int(input("enter your age:"))
#print("your age is",age)
#age=18
if age==18:
    #print("you are of age.")
    st.text("you are of age.")
    #print("allocate 50% of your portfolio to BTC")
    st.text("PORTFOLIO DESIGN AND RISK MANAGEMENT")
    #st.text("allocate 50% of your portfolio to crypto and 50 % between the SP500,DJIA and NASDAQ indices")
    import streamlit as st
    import matplotlib.pyplot as plt
    #time.sleep(10)
    
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = 'CRYPTO', 'SP500', 'DJIA', 'NASDAQ','Fine Art'
    sizes = [40, 15,15,15,15]
    mycolors = ["yellow", "hotpink", "b", "#4CAF50","maroon"]
    explode = (0, 0.1, 0, 0,0)  # only "explode" the 2nd slice (i.e. 'Hogs')
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90,colors = mycolors)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    st.pyplot(fig1)

        
elif age>18 and age<=30:
    #print("allocate 50% of your portfolio to BTC")
    st.text("PORTFOLIO DESIGN AND RISK MANAGEMENT")
    #st.text("allocate 50% of your portfolio to crypto and 50 % between the SP500,DJIA and NASDAQ indices")
    import streamlit as st
    import matplotlib.pyplot as plt
    #time.sleep(10)
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = 'CRYPTO', 'SP500', 'DJIA', 'NASDAQ','Fine Art'
    sizes = [40, 15,15,15,15]
    mycolors = ["yellow", "hotpink", "b", "#4CAF50","maroon"]
    explode = (0, 0.1, 0, 0,0)  # only "explode" the 2nd slice (i.e. 'Hogs')
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90,colors = mycolors)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    st.pyplot(fig1)
    
elif age>30 and age<=40:
    #print("allocate 40% of your portfolio to BTC")
    st.text("PORTFOLIO DESIGN AND RISK MANAGEMENT")
    #st.text("allocate 40% of your portfolio to crypto and 60 % between the SP500,DJIA and NASDAQ indices")
    import streamlit as st
    import matplotlib.pyplot as plt
    #time.sleep(10)
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = 'CRYPTO', 'SP500', 'DJIA', 'NASDAQ','Fine Art'
    sizes = [35, 16.25, 16.25, 16.25,16.25]
    mycolors = ["yellow", "hotpink", "b", "#4CAF50","maroon"]
    explode = (0, 0.1, 0, 0,0)  # only "explode" the 2nd slice (i.e. 'Hogs')
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90,colors = mycolors)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    st.pyplot(fig1)
    
elif age>40 and age<=50:
    #print("allocate 30% of your portfolio to BTC")
    st.text("PORTFOLIO DESIGN AND RISK MANAGEMENT")
    #st.text("allocate 30% of your portfolio to crypto and 70 % between the SP500,DJIA and NASDAQ indices")
    import streamlit as st
    import matplotlib.pyplot as plt
    #time.sleep(10)
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = 'CRYPTO', 'SP500', 'DJIA', 'NASDAQ','Fine Art'
    sizes = [30, 17.5, 17.5, 17.5,17.5]
    mycolors = ["yellow", "hotpink", "b", "#4CAF50","maroon"]
    explode = (0, 0.1, 0, 0,0)  # only "explode" the 2nd slice (i.e. 'Hogs')
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90,colors = mycolors)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    st.pyplot(fig1)
    

elif age>50 and age<=60:
    #print("allocate 20% of your portfolio to BTC")
    st.text("PORTFOLIO DESIGN AND RISK MANAGEMENT")
    #st.text("allocate 20% of your portfolio to crypto and 80 % between the SP500,DJIA and NASDAQ indices")
    import streamlit as st
    import matplotlib.pyplot as plt
    #time.sleep(10)
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = 'CRYPTO', 'SP500', 'DJIA', 'NASDAQ','Fine Art'
    sizes = [25, 18.75, 18.75, 18.75,18.75]
    mycolors = ["yellow", "hotpink", "b", "#4CAF50","maroon"]
    explode = (0, 0.1, 0, 0,0)  # only "explode" the 2nd slice (i.e. 'Hogs')
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90,colors = mycolors)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    st.pyplot(fig1)
    
    
elif age>60 and age<=70:
    #print("allocate 10% of your portfolio to BTC")
    st.text("PORTFOLIO DESIGN AND RISK MANAGEMENT")
    #st.text("allocate 10% of your portfolio to crypto and 90 % between the SP500,DJIA and NASDAQ indices")
    import streamlit as st
    import matplotlib.pyplot as plt
    #time.sleep(10)
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = 'CRYPTO', 'SP500', 'DJIA', 'NASDAQ','Fine Art'
    sizes = [20, 20, 20, 20,20]
    mycolors = ["yellow", "hotpink", "b", "#4CAF50","maroon"]
    explode = (0, 0.1, 0, 0,0)  # only "explode" the 2nd slice (i.e. 'Hogs')
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90,colors = mycolors)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    st.pyplot(fig1)
    
    
elif age>70 and age<=200:
    #print("allocate 5% of your portfolio to BTC")
    st.text("PORTFOLIO DESIGN AND RISK MANAGEMENT")
    #st.text("allocate 5% of your portfolio to crypto and 95 % between the SP500,DJIA and NASDAQ indices")
    import streamlit as st
    import matplotlib.pyplot as plt
    #time.sleep(10)
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = 'CRYPTO', 'SP500', 'DJIA', 'NASDAQ','Fine Art'
    sizes = [10, 22.5,22.5,22.5,22.5]
    mycolors = ["yellow", "hotpink", "b", "#4CAF50","maroon"]
    explode = (0, 0.1, 0, 0,0)  # only "explode" the 2nd slice (i.e. 'Hogs')
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90,colors = mycolors)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig1)
    
#crypto_portfolio()   
else:
    print("can not access the model.")
crypto_portfolio()	
#streamlit run portfolios_legacyandcrypto.py