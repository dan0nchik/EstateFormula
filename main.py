import streamlit as st
from formula import *
import math

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)
st.title('Расчет цены ипотеки')
res = 0
tax = 13  # подоходный налог
form = st.selectbox('Первоначальный взнос есть?', options=['Не выбрано', 'Да', 'Нет'], )
if form == 'Нет':
    buy = st.number_input('Первоначальная цена квартиры в руб (полностью, например, 8200000)', min_value=0)
    sell = st.number_input('Цена при продаже на руки продавцу в руб (полностью, например, 10500000)', min_value=0)
    fee = st.number_input('Первоначальный взнос (%)', min_value=0, value=20)
    res = formula_without_entry_fee(sell, buy, tax, fee)

    st.subheader('Стоимость квартиры в ипотеку с завышением:')
    if res == 0:
        st.text('Сначала введите все данные')
    else:
        st.title('{:,}'.format(round(res, 2)).replace(',', ' ') + ' руб')

if form == 'Да':
    in_arms = st.number_input('Стоимость на руки продавцу в руб (полностью, например, 10500000)', min_value=0)
    dkp_seller = st.number_input('Стоимость в ДКП в руб (полностью)', min_value=0)
    initial = st.number_input('Первоначальная цена квартиры в руб (полностью, например, 8200000)', min_value=0,
                              format='%i')
    bank = st.number_input('Банковский процент (%)', min_value=15)
    res = round(math.ceil(formula_with_entry_fee(in_arms, (in_arms - dkp_seller) * 0.13, initial)))
    if res == 0:
        st.text('Сначала введите все данные')
    else:
        st.subheader('Стоимость квартиры в ипотеку с занижением:')
        st.subheader('{:,}'.format(res).replace(',', ' ') + ' руб')
        st.subheader('Первоначальный взнос: ')
        st.subheader('{:,}'.format(res * bank / 100).replace(',', ' ') + ' руб')
        st.subheader('Сумма налога: ')
        st.subheader('{:,}'.format((res - initial) * 0.13).replace(',', ' ') + ' руб ')
        st.text('Из них компенсирует продавец: ' + '{:,}'.format((dkp_seller - initial) * 0.13))
        st.subheader('Покупатель компенсирует: ')
        st.subheader('{:,}'.format((res - initial) * 0.13 - (dkp_seller - initial) * 0.13))
