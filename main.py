import streamlit as st
from formula import *
import math
from st_keyup import st_keyup


def convert_to_num(*args):
    try:
        return [int(i) for i in args]
    except ValueError:
        return [0 for i in args]


def format_output(value: int):
    try:
        return "{:,}".format(int(value))
    except ValueError:
        return ''


hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)
st.title('Расчет цены ипотеки')
res = 0
tax = 13  # подоходный налог
form = st.selectbox('Есть первоначальный взнос?', options=['Не выбрано', 'Да', 'Нет'], )

if form == 'Нет':
    buy = st_keyup(label=f'Первоначальная цена квартиры в руб: ')
    st.write(format_output(buy))

    sell = st_keyup('Цена при продаже на руки продавцу в руб (полностью)')
    st.write(format_output(sell))

    fee = st.number_input('Первоначальный взнос (%)', min_value=0, value=20)

    res = formula_without_entry_fee(*convert_to_num(sell, buy, tax, fee))

    st.subheader('Стоимость квартиры в ипотеку с занижением:')
    if res == 0:
        st.text('Сначала введите все данные')
    else:
        st.title('{:,}'.format(round(res, 2)).replace(',', ' ') + ' руб')

if form == 'Да':
    in_arms = st_keyup('Стоимость на руки продавцу в руб (полностью)')
    st.write(format_output(in_arms))

    dkp_seller = st_keyup('Стоимость в ДКП в руб (полностью)')
    st.write(format_output(dkp_seller))

    initial = st_keyup('Первоначальная цена квартиры в руб (полностью)')
    st.write(format_output(initial))

    bank = st.number_input('Банковский процент (%)', min_value=15)

    in_arms, dkp_seller, initial = convert_to_num(in_arms, dkp_seller, initial)
    res = round(math.ceil(formula_with_entry_fee(in_arms, dkp_seller, initial)))
    if res == 0:
        st.text('Сначала введите все данные')
    else:
        st.subheader('Стоимость квартиры в ипотеку с завышением:')
        st.subheader('{:,}'.format(res).replace(',', ' ') + ' руб')

        st.subheader('Первоначальный взнос: ')
        st.subheader('{:,}'.format(math.ceil(res * bank / 100)).replace(',', ' ') + ' руб')

        st.subheader('Сумма налога: ')
        st.subheader('{:,}'.format(math.ceil((res - initial) * 0.13)).replace(',', ' ') + ' руб ')
        st.text('Из них компенсирует продавец: ' + '{:,}'.format(math.ceil((dkp_seller - initial) * 0.13)))

        st.subheader('Покупатель компенсирует: ')
        st.subheader('{:,}'.format(math.ceil((res - initial) * 0.13 - (dkp_seller - initial) * 0.13)))
