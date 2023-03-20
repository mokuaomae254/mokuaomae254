"""To use threading or multiprocessing in your Streamlit application, you can create a new thread or 
process to handle long-running tasks, while the main thread continues to respond to user requests. 
Here is an example of how to use threading in a Streamlit application:"""
"""In this example, the long_running_task() function is defined to perform a long-running task. 
The main() function creates a Streamlit app that displays a button for the user to start the task.
When the user clicks the button, a new thread is created to run the task in the background, 
while the main thread continues to respond to user requests."""
import streamlit as st
import threading

# Define a function that performs a long-running task
def long_running_task():
    import streamlit as st
    import matplotlib.pyplot as plt
    age= st.number_input("enter your age:") 
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

# Create a Streamlit app that runs the long-running task in a separate thread
def main():
    st.title("My Streamlit App")
    st.write("Click the button to start a long-running task:")

    if st.button("Start"):
        # Create a new thread to run the long-running task
        thread = threading.Thread(target=long_running_task)
        thread.start()

        # Display a message to the user
        st.write("Task started!")
        long_running_task()
if __name__ == '__main__':
	main()
#Note that this is just a simple example of how to use threading in a Streamlit app. In practice, you may need to use more complex synchronization mechanisms to coordinate between the main thread and the worker thread, depending on your specific use case. Additionally, you can also use multiprocessing instead of threading to run tasks in parallel using multiple processes."""
#streamlit run multithreading.py