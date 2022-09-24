import streamlit as st

st.title('Расчет цены ипотеки')

buy = st.number_input('Первоначальная цена квартиры (полностью, например, 8200000)', min_value=0, format='%i')
sell = st.number_input('Цена при продаже на руки продавцу (полностью, например, 10500000)', min_value=0)
tax = st.number_input('Подоходный налог при завышении (%)', value=13)
fee = st.number_input('Первоначальный взнос (%)', min_value=0, value=20)

tax /= 100
fee /= 100

st.title('Результат:')
res = (sell - buy * tax) / (1 - tax - fee)
st.title('{:,}'.format(round(res, 2)).replace(',', ' ') + ' руб')
