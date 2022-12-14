import streamlit as st
from bbctest import retrieve_doc
import pandas as pd
import time

data=pd.read_csv('headings.csv')

message = st.text_input('Type a Heading to get relevant matches: ')
# number = st.slider('Choose the Number of Articles to Retrieve', 0, 50, 5)

# @st.cache
if st.button('Search'):
    shape, number_of_news_articles, new_query_vector, argmax, header, ind=retrieve_doc(message, raw_docs=data, colname="Article")
    with st.spinner('Wait for it...'):
        time.sleep(5)
    st.success('Successfully Retrieved')
    st.write('**Number of News Articles: **' + str(number_of_news_articles))
    st.write('**Retrieved Top Document Header is: **' + header)
    for i in ind:
        st.write(data.Heading.values[i])
    # st.table(ind)
