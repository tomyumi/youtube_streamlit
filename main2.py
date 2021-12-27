import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image 
import time

from streamlit.proto.Progress_pb2 import Progress

st.title("プログレスバー")

st.write("ぷろぐれすばーの表示")
'start!!'
'sutarrrt!!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)
    
'Done!!!!'














left_columun, right_columun = st.beta_columns(2)
button = left_columun.button('右カラムに文字を表示')
if button:
    right_columun.write("ここは右カラムです")

expander1 = st.beta_expander('問い合わせ1')
expander1.write('問い合わせ内容を書く1')
expander2 = st.beta_expander('問い合わせ2')
expander2.write('問い合わせ内容を書く2')
expander3 = st.beta_expander('問い合わせ3')
expander3.write('問い合わせ内容を書く3')

# text = st.text_input('あなたの趣味を教えてください',)
# condition = st.slider('あんたの調子は',0,10,5)


# 'あんたの趣味は, ', text, 'です。'
# 'コンディション',condition

# if st.checkbox('Show Image'):
#     img = Image.open('20.jpg')
#     st.image(img, caption='tom', use_column_width=True)

