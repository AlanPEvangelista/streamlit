import streamlit as st
import yfinance as yf

st.title(''':blue[Preço de Ativo]''')
st.header("Informações de ações deste 01/01/2012")
st.markdown('''
    :orange[Temos] :green[outros] :blue[gráficos].''')

# ENBR3.SA
# BBAS3.SA
# BBDC4.SA
# PETR4.SA
# VALE5.SA

opcoes = st.selectbox('Escolha o Ativo', ('ENBR3.SA',
                      'BBAS3.SA', 'BBDC4.SA', 'PETR4.SA', 'VALE5.SA'))

tickerSimbolo = opcoes

tickerData = yf.Ticker(tickerSimbolo)
tikerDf = tickerData.history(period='1d', start='2012-1-1')
st.header("Grafico de Fechamento")
st.line_chart(tikerDf.Close)
st.header("Gráfico de Volume")
st.line_chart(tikerDf.Volume)
st.header("Gráfico de Dividendos")
st.line_chart(tikerDf.Dividends)
