import streamlit as st

# possible to have values pers

st.title('Counter Example')

if 'count' not in st.session_state:
	st.session_state.count = 0

increment = st.button('Increment')
if increment: # 버튼이 눌리면
    st.session_state.count += 1

decrement = st.button('Decrement')
if decrement:
    st.session_state.count -= 1

values = st.slider('Select a range of values', 0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)

st.write('Count = ', st.session_state.count, )
