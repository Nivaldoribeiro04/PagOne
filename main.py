import streamlit as st


st.set_page_config(
    page_title="Gestão1"
)

st.header("Bem vindo ao sistema de Gestão de clientes",width=1000)


tab1,tab2,tab3,tab4 = st.tabs(['Inicio','Pagamentos','Clientes','Configurações'])

with tab1:
    st.write('Bem vindo')


with tab3:
    st.text_input("Nome do clinte")