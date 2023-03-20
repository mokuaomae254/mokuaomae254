#syntax
import streamlit as st

@st.cache
def expensive_computation(arg1, arg2, ...):
    # perform a long or complex computation here
    result = ...
    return result

# Use the function in your Streamlit app as normal:
result = expensive_computation(arg1, arg2, ...)
st.write(result)
"""
In this example, the expensive_computation function is decorated with the st.cache decorator. 
This tells Streamlit to cache the result of the function so that it doesn't have to be recomputed every time
the function is called with the same arguments. Instead, Streamlit will store the result in memory and return
it immediately for subsequent calls with the same arguments.

You can control the behavior of the cache by specifying arguments to the st.cache decorator, 
such as the maximum size of the cache, the length of time that results should be kept in the cache,
or the number of function calls before the cache is flushed. For more details, please refer to the Streamlit 
documentation.
Yes, it is necessary to use the return statement in a function decorated with st.cache in Streamlit.
The return statement is used to return the result of the computation or data processing performed by the 
function, which will be cached by Streamlit and reused for subsequent calls with the same arguments. 
If you don't include a return statement in the function, it will not return any value and therefore there 
will be nothing to cache.

Here's an example of a function decorated with st.cache that returns a result:
"""