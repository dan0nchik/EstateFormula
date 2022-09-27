import streamlit as st
from formula import *
import pyperclip

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)
st.title('Расчет цены ипотеки')
res = 0
buy = st.number_input('Первоначальная цена квартиры (руб) (полностью, например, 8200000)', min_value=0, format='%i')
sell = st.number_input('Цена при продаже на руки продавцу (руб) (полностью, например, 10500000)', min_value=0)
tax = st.number_input('Подоходный налог при завышении (%)', value=13)
form = st.selectbox('Первоначальный взнос (проценты/рубли)', options=['Проценты', 'Рубли'])
if form == 'Проценты':
    fee = st.number_input('Первоначальный взнос (%)', min_value=0, value=20)
    res = formula_with_percent(sell, buy, tax, fee)
else:
    fee = st.number_input('Первоначальный взнос (полностью, в рублях)', min_value=0, value=0)
    res = formula_without_percent(sell, buy, tax, fee)


st.title('Результат:')
if res == 0:
    st.text('Сначала введите все данные')
else:
    res = '{:,}'.format(round(res, 2)).replace(',', ' ') + ' руб'
    st.title(res)
    if st.button('Скопировать'):
        pyperclip.copy(res)
        st.success('Скопировано!')

