import streamlit as st
from transformers import pipeline

translator = pipeline("translation_ru_to_en", model="Helsinki-NLP/opus-mt-ru-en")
st.title('Team12UrFUProject Task 2')
st.subheader('This app translates russian to english')
txt = st.text_area("Place russian text there:")
tr_txt = translator(txt)[0]['translation_text']
st.write('Translated text:')
st.write(tr_txt)
