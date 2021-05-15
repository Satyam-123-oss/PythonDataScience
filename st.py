import streamlit as st
import pandas as pd
import io
import numpy as np

from streamlit_player import st_player

# st_player("https://youtu.be/CmSKVW1v0xm")
st.title("Welcome Sattya Bhai")
st.write("""Hello welcome to the new era of Arificial inteligance..""")
st.text("Iris dtasets")
s=st.button("press me",)

def get_data():
    st.write("Button clicked")
    st.button("Now click this",)
    st.success("logged in")
    st.secrets="sa"

if s:
    get_data()
st.markdown('Streamlit is **_really_ cool**.')
st.latex(r'''
a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
\sum_{k=0}^{n-1} ar^k =
a \left(\frac{1-r^{n}}{1-r}\right)
''')
st.write('Hello, *World!* :sunglasses:')
st.write(123456222)
st.write(pd.DataFrame({
'first column': [1, 2, 3, 4],
'second column': [10, 20, 30, 40],
}))
st.write('1 + 1 = ', 2)
st.header('This is a header')
st.subheader('This is a subheader')
code = '''def hello():
print("Hello, Streamlit!")'''
st.code(code, language='python')
df = pd.DataFrame(
np.random.randn(50, 20),
columns=('col %d' % i for i in range(20)))

st.dataframe(df) # Same as st.write(df)

st.table(df)
chart_data = pd.DataFrame(
np.random.randn(20, 3),
columns=['a', 'b', 'c'])

st.line_chart(chart_data)

st.area_chart(chart_data)
x = st.slider('x') # this is a widget
st.write(x, 'squared is', x * x)

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
'How would you like to be contacted?',
('Email', 'Home phone', 'Mobile phone')
)
# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
'Select a range of values',
0.
)
left_column, right_column = st.beta_columns(2)
left_column.button('Press me!')
# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
    'Sorting hat',
    ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")


uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
# To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)
    ... # To convert to a string based IO:
    stringio = io.StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.write(stringio)
    # To read file as string:
    string_data = stringio.read()
    st.write(string_data)
    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)

