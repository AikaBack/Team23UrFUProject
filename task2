import os
import streamlit as st
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline

# Указание имени модели (то же имя, которое использовалось для сохранения модели)
model_name = "Helsinki-NLP/opus-mt-ru-en"

# Задание каталога, в котором вы хотите кэшировать и хранить файлы модели
cache_dir = os.getcwd()

# Загрузка модели и токенизатора из указанного каталога
loaded_model = AutoModelForSeq2SeqLM.from_pretrained(model_name, cache_dir=cache_dir)
loaded_tokenizer = AutoTokenizer.from_pretrained(model_name, cache_dir=cache_dir)

# Создание переводчика
translator = pipeline(
    task="translation",
    model=loaded_model,
    tokenizer=loaded_tokenizer
)

# Streamlit приложение
st.title("Русско-английский переводчик")

# Поле ввода текста на русском языке
input_text = st.text_area("Введите текст на русском языке:")

if st.button("Перевести"):
    if input_text:
        # Перевести введенный текст
        translation = translator(input_text)
        st.subheader("Перевод на английский:")
        st.write(translation[0]["translation_text"])
    else:
        st.warning("Пожалуйста, введите текст на русском языке.")

st.write("Пример ввода: 'Привет, как дела?'")


