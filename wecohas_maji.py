import streamlit as st

# Create a dictionary of products
products = {
    1: {"name": "Bottled Water", "price": 2.99},
    2: {"name": "Water Coolers", "price": 49.99},
    3: {"name": "Filtered Water Systems", "price": 199.99},
}

# Set the page config
#st.beta_set_page_config(page_bg_color='#ffffff', page_icon=":droplet:", layout="wide", page_title="Water Selling Company", page_image_url="wecohas.jpg")
st.set_page_config(page_title="Water Selling Company", page_icon=":droplet:", layout="wide")
st.markdown('<body style="background-image: url(wecohas.jpg);"></body>', unsafe_allow_html=True)


#st.set_body_background("water.jpg")
# Create the title
st.title("Water Selling Company")


# Create a button to view products
if st.button("View Products"):
    st.subheader("Products")
    for product_id, product in products.items():
        st.write(f"{product['name']} - ${product['price']}")
        # if st.button("Add to Cart"):   # <-- remove this line
        #     st.cache["cart"].append(product_id)
        #     st.success("Product added to cart!")

# Create a button to checkout and pay
if st.button("Checkout"):
    st.subheader("Checkout")
    # Add shipping information form
    name = st.text_input("Enter your name:")
    address = st.text_input("Enter your address:")
    phone_number = st.text_input("Enter your phone number:")
    email = st.text_input("Enter your email:")
    st.write(f"Shipping to {name} at {address}")
    st.write(f"Phone number: {phone_number}")
    st.write(f"Email: {email}")
    # Add payment method
    # Add payment method
    payment_method = st.selectbox("Select Payment Method", ["Mpesa", "Credit Card", "Paypal"])
    if payment_method == "Mpesa":
        st.write("Please use Paybill Number: 123456 to complete the payment.")
    elif payment_method == "Credit Card":
        card_number = st.text_input("Enter Card Number:")
        expiry_date = st.text_input("Enter Expiry Date:")
        cvv = st.text_input("Enter CVV:")
        st.write("Your card information is being processed.")
    elif payment_method == "Paypal":
        paypal_email = st.text_input("Enter your Paypal Email:")
        st.write("Please use this email to complete the payment on Paypal: ", paypal_email)
    st.write("Thank you for your purchase!")


    
       

    

#streamlit run wecohas_maji.py