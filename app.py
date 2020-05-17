import streamlit as st 
from Model import Banco,Percent
import pandas as pd 
import numpy as np


st.title("Qual o melhor sistema operacional para uso em servidores?")
st.subheader('Enquete da atividade de POO da PUCPR, Curso de BigData e IA.')


opcao = st.radio(
     " ",
     ("Windows Server","Unix","Linux","Netware","Mac OS","Outro"))
banco = Banco()

if st.button("votar"):
    value = banco.insert(opcao)
    st.title(value)

if st.button("Fim da Votação"):    
    dados = banco.list_itens(["Windows Server","Unix","Linux","Netware","Mac OS","Outro"])
    porcentage = Percent()
    df = porcentage.calcule()   
    chart_data  = pd.DataFrame.from_dict(df, orient='index',columns=['Porcentagem'])
    st.write(chart_data)
    st.bar_chart(chart_data)
