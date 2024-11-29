import streamlit as st
st.write({"key":"value"})
# write -- is a magic word like if i write smth it autmoatically detects and write 
# it in a specific format in 
# st.write({"key":"value"})
st.write(True)

4+7
"hello" if True else "bye"
# write commands are stereamlit magic

# Always rerun if any changes are made 
import streamlit as st
p=st.button("Press me")
print(p)

############

import streamlit as st

# text elements

st.title("Hello ")
st.header("This is a header")
st.subheader("THis js ")
st.markdown("This is **Markdown**")
st.caption("THis is a ")
c="""
def greet(name):
print(f"Hello, {name}!")
"""
st.code(c, language="python")
st.divider()


import os
st.image(os.path.join(os.getcwd(),"static","BG.jpg"))



import streamlit as st
import pandas as pd
#data elements

st.title("Streamlit Data elemnts")
st.subheader("DataFrame")
df=pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie", "Diana", "Eve"],
    "age": [25, 30, 35, 40, 28],
    "occupation": ["Engineer", "Doctor", "Artist", "Teacher", "Designer"]
})
st.dataframe(df)

st.subheader("Data Editor")
editable_df = st.data_editor(df)

st.subheader("Static Table")
st.table(df)

st.subheader("Metrics")
st.metric(label="Total Rows", value=len(df))
st.metric(label="Average age", value = round(df['age'].mean(),1))

st.subheader("Json and Dictionary")
sampledict ={
    "name": "John",
    "age":25,
    "city":"New York"
    
}
st.json(sampledict)

st.write("Dictionary view ", sampledict)