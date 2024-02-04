import streamlit as st
import yfinance as yf

st.title(''':blue[Preço de Ativo]''')
st.header("Informações a respeito do fechamento e volume de algumas ações")
st.markdown('''
    :red[Ativo PETR4] :orange[Temos] :green[outros] :blue[gráficos].''')

# ENBR3.SA
# BBAS3.SA
# BBDC4.SA
# PETR4.SA
# VALE5.SA

tickerSimbolo = "PETR4.SA"
tickerData = yf.Ticker(tickerSimbolo)
tikerDf = tickerData.history(period='1d', start='2022-1-1')
st.header("Grafico de Fechamento")
st.line_chart(tikerDf.Close)
st.header("Gráfico de Volume")
st.line_chart(tikerDf.Volume)
st.header("Gráfico de Dividendos")
st.line_chart(tikerDf.Dividends)
