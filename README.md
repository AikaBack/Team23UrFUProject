# Team12UrFUProject
## Участники команды:

- Масленников Виктор (РИМ-130908)
- Скоробогач Максим (РИМ-130908)
- Саттаров Артем (РИМ-130908)
- Янабеков Александр Владимирович (РИМ-130907)

 **Модель:** Helsinki-NLP/opus-mt-ru-en
### Описание модели
Модель применяется для перевода текста с русского языка на английский.

### Задание №1

### Пример использования
```python
!pip install transformers sentencepiece sacremoses
from transformers import pipeline
translator = pipeline("translation_ru_to_en", model="Helsinki-NLP/opus-mt-ru-en")
cycle = "да"
while cycle == "да" or cycle == "Да":
  text = input('Введите текст для перевода на английский: ')
  results = translator(text)
  print("Переведенный текст: " + results[0]['translation_text'])
  cycle = input('Хотите продолжить? \nВведите "Да" для продолжения, "Нет" для остановки\n'
```
### Задание №2
## Пример использования
![image](https://github.com/Lunatik3/Team12UrFUProject/assets/147321002/32327578-1d01-467b-a88a-ab602e3324c6)

### Задание №3
## Пример использования
# Для запуска АПИ и ВЕБ интерфейса нужно:
# В командной строке запустить апи "uvicorn task3:app --reload --port 8000" - команда разворачивает на адрессе http://127.0.0.1:8000/ АПИ
# В другой командной строке запустить веб "streamlit run task3.py" - команда запускает веб интерфейс

После чего нужно вставить в поле текст который нужно перевести, после запроса на АПИ вернется результат перевода прямо под полем

![image](https://github.com/Lunatik3/Team12UrFUProject/assets/70605553/a83a1eb4-e08a-46d6-938d-204c0229302a)
