"""Caching
Streamlit runs your script from top to bottom at every user interaction or code change. This execution model makes development super easy. But it comes with two major challenges:

Long-running functions run again and again, which slows down your app.
Objects get recreated again and again, which makes it hard to persist them across reruns or sessions.
But don’t worry! Streamlit lets you tackle both issues with its built-in caching mechanism. Caching stores the results of slow function calls, so they only need to run once. This makes your app much faster and helps with persisting objects across reruns."""
@st.cache_data
def long_running_function(param1, param2):
    return
"""In this example, decorating long_running_function with @st.cache_data tells Streamlit that whenever the function is called, it checks two things:

The values of the input parameters (in this case, param1 and param2).
The code inside the function.
If this is the first time Streamlit sees these parameter values and function code, it runs the function and stores the return value in a cache. The next time the function is called with the same parameters and code (e.g., when a user interacts with the app), Streamlit will skip executing the function altogether and return the cached value instead. During development, the cache updates automatically as the function code changes, ensuring that the latest changes are reflected in the cache.

As mentioned, there are two caching decorators:

st.cache_data is the recommended way to cache computations that return data: loading a DataFrame from CSV, transforming a NumPy array, querying an API, or any other function that returns a serializable data object (str, int, float, DataFrame, array, list, …). It creates a new copy of the data at each function call, making it safe against mutations and race conditions. The behavior of st.cache_data is what you want in most cases – so if you're unsure, start with st.cache_data and see if it works!"""
"""st.cache_resource is the recommended way to cache global resources like ML models or database connections – unserializable objects that you don’t want to load multiple times. Using it, you can share these resources across all reruns and sessions of an app without copying or duplication. Note that any mutations to the cached return value directly mutate the object in the cache (more details below)."""
"""Basic usage
st.cache_data
st.cache_data is your go-to command for all functions that return data – whether DataFrames, NumPy arrays, str, int, float, or other serializable types. It’s the right command for almost all use cases!

Usage

Let's look at an example of using st.cache_data. Suppose your app loads the Uber ride-sharing dataset – a CSV file of 50 MB – from the internet into a DataFrame:"""
def load_data(url):
    df = pd.read_csv(url)  # 👈 Download the data
    return df

df = load_data("https://github.com/plotly/datasets/raw/master/uber-rides-data1.csv")
st.dataframe(df)

st.button("Rerun")
""" Running the load_data function takes 2 to 30 seconds, depending on your internet connection. (Tip: if you are on a slow connection, use this 5 MB dataset instead). Without caching, the download is rerun each time the app is loaded or with user interaction. Try it yourself by clicking the button we added! Not a great experience… 😕

Now let’s add the @st.cache_data decorator on load_data:"""
@st.cache_data  # 👈 Add the caching decorator
def load_data(url):
    df = pd.read_csv(url)
    return df

df = load_data("https://github.com/plotly/datasets/raw/master/uber-rides-data1.csv")
st.dataframe(df)

st.button("Rerun")
"""Run the app again. You'll notice that the slow download only happens on the first run. Every subsequent rerun should be almost instant! 💨

Behavior

How does this work? Let’s go through the behavior of st.cache_data step by step:

On the first run, Streamlit recognizes that it has never called the load_data function with the specified parameter value (the URL of the CSV file) So it runs the function and downloads the data.
Now our caching mechanism becomes active: the returned DataFrame is serialized (converted to bytes) via pickle and stored in the cache (together with the value of the url parameter).
On the next run, Streamlit checks the cache for an entry of load_data with the specific url. There is one! So it retrieves the cached object, deserializes it to a DataFrame, and returns it instead of re-running the function and downloading the data again.
This process of serializing and deserializing the cached object creates a copy of our original DataFrame. While this copying behavior may seem unnecessary, it’s what we want when caching data objects since it effectively prevents mutation and concurrency issues. Read the section “Mutation and concurrency issues” below to understand this in more detail.Examples

DataFrame transformations

In the example above, we already showed how to cache loading a DataFrame. It can also be useful to cache DataFrame transformations such as df.filter, df.apply, or df.sort_values. Especially with large DataFrames, these operations can be slow."""
@st.cache_data
def transform(df):
    df = df.filter(items=['one', 'three'])
    df = df.apply(np.sum, axis=0)
    return df
"""Array computations

Similarly, it can make sense to cache computations on NumPy arrays:"""
@st.cache_data
def add(arr1, arr2):
    return arr1 + arr2
"""Database queries

You usually make SQL queries to load data into your app when working with databases. Repeatedly running these queries can be slow, cost money, and degrade the performance of your database. We strongly recommend caching any database queries in your app. See also our guides on connecting Streamlit to different databases for in-depth examples."""
connection = database.connect()

@st.cache_data
def query():
    return pd.read_sql_query("SELECT * from table", connection)

"""You should set a ttl (time to live) to get new results from your database. If you set st.cache_data(ttl=3600), Streamlit invalidates any cached values after 1 hour (3600 seconds) and runs the cached function again. See details in Controlling cache size and duration."""
"""API calls

Similarly, it makes sense to cache API calls. Doing so also avoids rate limits."""
@st.cache_data
def api_call():
    response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
    return response.json()

"""Deciding which caching decorator to use

The sections above showed many common examples for each caching decorator. But there are edge cases for which it’s less trivial to decide which caching decorator to use. Eventually, it all comes down to the difference between “data” and “resource”:

Data are serializable objects (objects that can be converted to bytes via pickle) that you could easily save to disk. Imagine all the types you would usually store in a database or on a file system – basic types like str, int, and float, but also arrays, DataFrames, images, or combinations of these types (lists, tuples, dicts, and so on).
Resources are unserializable objects that you usually would not save to disk or a database. They are often more complex, non-permanent objects like database connections, ML models, file handles, threads, etc.
From the types listed above, it should be obvious that most objects in Python are “data.” That’s also why st.cache_data is the correct command for almost all use cases. st.cache_resource is a more exotic command that you should only use in specific situations.

Or if you’re lazy and don’t want to think too much, look up your use case or return type in the table below 😉:"""

#streamlit run streamlit_caching.py