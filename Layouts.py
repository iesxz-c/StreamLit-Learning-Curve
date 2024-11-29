## Layouts
import streamlit as st

st.sidebar.title("THis a sidebar")
st.sidebar.write("Fui")
side = st.sidebar.text_input("Hi")

a,b,c  = st.tabs(["1","2","3"])
with a:
    st.write("1")
with b:
    st.write("2")
with c:
    st.write("3")

e,f = st.columns(2)

with e:
    st.write("HJINXcbmcjhcbckhcbj")
with f:
    st.write("bvhgcjbvjhcm bjvb cmsgumc hcbysc kc hcmd cijhckn cnd cmhcicckshjcc")

with st.container(border=True):
    st.write("Hello, world!")

place = st.empty()
place.write("bjhbvmdjbvjhbvhbm")

if st.button("Override"):
    place.write("hjcbhjcbhjcbhjcbhjcbh")

with st.expander("Expand"):
    st.write("This is an expander")

st.button("Button", help="Button")
