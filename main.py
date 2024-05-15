import streamlit as st
import datetime

import yfinance as yf
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go
import pandas as pd
import cufflinks as cf

url = 'https://raw.githubusercontent.com/datasets/nasdaq-listings/master/data/nasdaq-listed-symbols.csv'

start_date=st.sidebar.date_input("Start date",datetime.date(2019,1,1))
end_date=st.sidebar.date_input("End date",datetime.date(2021,1,31))

st.title("Stock Predictor")
ticker_list=pd.read_csv(url)
tickerSymbol=st.sidebar.selectbox('Symbol',ticker_list)
tickerData=yf.Ticker(tickerSymbol)
tickerDf=tickerData.history(period='1d',start=start_date)

type(tickerData)
0
#string_logo='<img src=%s>'%tickerData.info['logo_url']
#st.markdown(string_logo, unsafe_allow_html=True)
st.markdown(open("index.html").read(), unsafe_allow_html=True)

string_name = tickerData.info.get('Symbol')
st.header('**%s**'%string_name)
string_summary = tickerData.info.get('logoBusinessSummary')
st.info(string_summary)

st.header('**Ticker data**')
st.write(tickerDf)

st.header('**Bollinger Bands**')
qf=cf.QuantFig(tickerDf,title='First Quant Figure',legend='top',name='GS')
qf.add_bollinger_bands()
fig=qf.iplot(asFigure=True)
st.plotly_chart(fig)
 





