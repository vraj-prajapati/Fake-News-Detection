import requests
from bs4 import BeautifulSoup as bs
import streamlit as st
import pandas as pd
url = "https://indianexpress.com/todays-paper/"
req = requests.get(url).text
soup = bs(req, 'html5lib')
req1 = soup.find('div', class_ = "today-paper")
# df = pd.read_csv('pages/datas1.csv')
# length = len(df)
st.header("Today's Trending NEWS");
if req1:
    links = req1.find_all('a')
    img = req1.find_all('img',class_ = 'attachment-thumbnail size-thumbnail wp-post-image')
    arr = {}
    #Pre-processing
    for link in links:
        href = link['href']
        text = link.text
        if(text and href.startswith('https://')):
            arr[href] = text
    #Showing output        
    for imgs,(key,value) in zip(img,arr.items()):
        i_link = imgs['src']
        # st.write(i_link)
        st.write(value,': ', key)
        st.image(i_link,width=400)
    #Changing dataset (should be done once per day)
        # dict = [length,key,value,0]
        # df.loc[length] = dict
        # length = length + 1
        
# df.to_csv('pages/datas1.csv')
