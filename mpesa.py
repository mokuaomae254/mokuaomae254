import mpesa

# Initialize the mpesa library with your credentials
mpesa.init("consumer_key", "consumer_secret", "sandbox")

if st.button("View Cart"):
    st.subheader("Cart")
    comment = st.text_area("Enter any comments or questions about your order here:")
    total = 0
    for product_id in st.cache["cart"]:
        product = products[product_id]
        st.write(f"{product['name']} - ${product['price']}")
        total += product["price"]
    st.write(f"Total: ${total}")
    # Get the customer's phone number
    phone_number = st.text_input("Enter your phone number:")
    # Send the payment request to the customer's phone number
    mpesa.lipa_na_mpesa(
        phone_number, 
        total, 
        "Till Number",
        "Water Selling Company Order"
    )
    st.success("Payment request sent!")


import mpesa

# Initialize the mpesa library with your credentials
mpesa.init("consumer_key", "consumer_secret", "sandbox")

if st.button("View Cart"):
    st.subheader("Cart")
    comment = st.text_area("Enter any comments or questions about your order here:")
    total = 0
    for product_id in st.cache["cart"]:
        product = products[product_id]
        st.write(f"{product['name']} - ${product['price']}")
        total += product["price"]
    st.write(f"Total: ${total}")
    # Get the customer's phone number
    phone_number = st.text_input("Enter your phone number:")
    # Send the payment request to the customer's phone number
    mpesa.stk_push(
        phone_number, 
        total, 
        "Paybill Number",
        "Water Selling Company Order"
    )
    st.success("Payment request sent!")
