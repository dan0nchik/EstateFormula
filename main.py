import streamlit as st

st.title('Расчет цены ипотеки')

start = st.number_input('Начальная цену квартиры в млн (например, 8)', min_value=0)
sell = st.number_input('Цена при продаже в млн (например, 10)', min_value=0)
delta_tax = st.number_input('Налог при продаже (%)', value=13)
fee = st.number_input('Первоначальный взнос (%)', min_value=0, value=20)

start*=10**6
sell*=10**6
delta_tax/=100
fee/=100

st.title('Результат:')
res = (sell*(delta_tax-1))/(fee+delta_tax+-1)
st.title('{:,}'.format(round(res, 2)).replace(',', ' ')+' руб')

