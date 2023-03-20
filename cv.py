import streamlit as st
#from PIL import Image
#image = Image.open('profile.jpg')
#st.image(image, width=200)
st.header("Profile")
st.text("  \n\r    Motivated software engineer looking to pursue a successful career in \n\rBlockchain development at Company Open Cipher,where I can help in the delivery of\n\r state-of-the-art software solutions.\n\r Experience includes coding, troubleshooting, and testing for my own \n\rpersonal projects while at Masinde Muliro University Of Science and Technology .\n\r Relevant skills include PHP, Data Structures, Machine Learning, and Debugging.")
st.header("Education")
st.markdown("""2019-09\n 
            \r2023-04   
            Masinde Muliro University Of Science and Technology,B.S COMPUTER SCIENCE
            \nIn my final year
            \n2015-03\n 
            \r2018-12 
            \nKanga School
            \nKCSE grade B
            \n2012-01\n 
            \r2014-12 
            \nTengecha Primary
            \nKCPE mark 385   
               """,True)
st.header("Experience ")
st.markdown("""2018-12\n 
            \r till date 
            \nI was actively investing and accumulating undervalue cryptocurrency projects.
            \n2020-08\n 
            \r till date
            \n I was  actively analyzing swing trading in the cryptocurrency markets.
            \n2021-08\n 
            \r till date
            \n I started Open Cipher a blockchain company that solves real life problems using blockchain technology .
            \n We also create trading and investing strategies for retail investors.
            \n below are the projects done by Open Cipher
            
            
            
               
               """,True)
st.header("Projects")
st.markdown("""_Crypto Service Aggregator(third year project)_\n
            \nIt compares the prices of digital assets from different fiat onramp gateways and \n gives the user the best execution price.
               \n_Decentralized Exchange(DEX)_
               \n It allows users to swap cryptocurrencies without the need of a third party in a trustless manner.
               \n_DEFI Yield Aggregator(in progress....)_
               \n It compares yields on different platforms offered for different digital assets and gives the most sustainable yields.
               \n_Decentralized Music Sreaming Platform(in progress....)_
               \n Immutable Records is streaming platform where the fanbase is connected directly to the artists.
               \n_cryptocurrency Price Tracker and Desion Making Assistant(forth year project)_
               \n It tracks the top 100 crypto assets and help investors make sound investment decisions by providing tested economic models and data. 
            
               
               """,True)
with st.sidebar:
    from PIL import Image
    image = Image.open('profile.jpg')
    st.image(image, width=100)
    st.title("Robert Mokua Omae Obare")
    st.text("Computer Science Professional")
    st.subheader("Personal Information")
    st.text("address")
    st.text("P.O BOX 2546-40200-Kisii ")
    st.text("Phone Number")
    st.text("+254 717150549")
    st.text("Email")
    st.text("robertobare68@gmail.com")
    st.text("Linkedin ")
    st.text("https://www.linkedin.com/in/robert-obare-832bb3251")
    
    st.text("twitter")
    st.text("")
    st.subheader("Programing languages(proficient)")
    st.text("solidity")
    st.text("C++")
    st.text("C")
    st.text("Python")
    st.subheader("Programing languages(familiar)")
    st.text("Rust")
    st.text("Java")
    st.text("PHP")
    st.subheader("Business Skills")
    st.text("Investing and trading")
    st.text("Leadership")
    st.text("Saling")
    st.subheader("Hard Skills")
    st.text("Smart Contract Development")
    st.text("Data Structures")
    st.text("Data Science")
    st.text("Python Programming")
    st.text("Algorithmic Trading")
    
        

    
#streamlit run cv.py