""" 
The Password Generator
"""

import streamlit as st
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
           'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
           'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


if 'stage' not in st.session_state:
    st.session_state.stage = 0

def set_state(i):
    st.session_state.stage = i

if st.session_state.stage == 0:
    st.write("Click the button below to begin")
    st.button('Begin', on_click=set_state, args=[1])

if st.session_state.stage >= 1:
    st.write("## Welcome to the Password Generator!")
    name = st.text_input('What is your name?', on_change=set_state, args=[2])


if st.session_state.stage >=2:
    st.write(f'Hello {name.capitalize()}!')

    nr_letters = st.text_input(
            "How many letters would you like in your password?\n",
            on_change=set_state, args=[3]
            )
    
    if nr_letters  is None:
        set_state(2)

if st.session_state.stage >=3:
    nr_symbols = st.text_input(
            "How many symbols would you like?\n",
            on_change=set_state, args=[4]
            )
    
    if nr_symbols  is None:
        set_state(3)


if st.session_state.stage >=4:
    nr_numbers = st.text_input(
            "How many numbers would you like?\n",
            on_change=set_state, args=[5]
            )
    
    if nr_numbers  is None:
        set_state(4)


if st.session_state.stage >=5:
    rand_letters = random.choices(letters, k=int(nr_letters))
    rand_numbers = random.choices(numbers, k=int(nr_numbers))
    rand_symbols = random.choices(symbols, k=int(nr_symbols))


    password_list = rand_letters + rand_numbers + rand_symbols
    password_len = len(password_list)
    password_list_shuffled = random.sample(password_list, k=password_len)
    password = ''.join(password_list_shuffled)

    st.markdown(f"#### Here is your password: :blue[{password}]")
    st.button("Start Over", on_click=set_state, args=[0])
