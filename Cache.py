
import streamlit as st
import time
#caching

@st.cache_data(ttl=60)
    # cache the data for 60s
def fetchd():
    time.sleep(3)
    return {"data":"Cached data"}
st.write("Fetching data..................")
data = fetchd()
st.write(data) 