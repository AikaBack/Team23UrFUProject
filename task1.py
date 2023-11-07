!pip install transformers sentencepiece sacremoses
from transformers import pipeline
translator = pipeline("translation_ru_to_en", model="Helsinki-NLP/opus-mt-ru-en")
cycle = "да"
while cycle == "да" or cycle == "Да":
  text = input('Введите текст для перевода на английский: ')
  results = translator(text)
  print("Переведенный текст: " + results[0]['translation_text'])
  cycle = input('Хотите продолжить? \nВведите "Да" для продолжения, "Нет" для остановки\n')
