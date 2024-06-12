import pandas as pd
import numpy as np
import seaborn as sns

# Создание датасета о пассажирах Титаника
def create_titanic_dataset():
    # Загрузка датасета о пассажирах Титаника из seaborn
    titanic_df = sns.load_dataset('titanic')
    
    # Выбор необходимых признаков
    return titanic_df[['pclass', 'sex', 'age']].copy()

# Заполнение пропущенных значений в поле "age"
def fill_missing_age(df):
    df_filled = df.copy()
    mean_age = df_filled['age'].mean()
    df_filled['age'].fillna(mean_age, inplace=True)
    return df_filled

# Кодирование категориального признака "sex" с использованием one-hot-encoding
def one_hot_encode_sex(df):
    return pd.get_dummies(df, columns=['sex'])

# Загрузка и обработка датасета
def process_titanic_data():
    titanic_df = create_titanic_dataset()
    
    # Сохранение исходного датасета
    titanic_df.to_csv('data/titanic.csv', index=False)
    
    # Заполнение пропущенных значений в поле "age"
    titanic_df = fill_missing_age(titanic_df)
    
    # Добавление аномалий для тестирования
    titanic_df.loc[titanic_df['age'].isnull(), 'age'] = np.random.randint(1, 80, size=titanic_df['age'].isnull().sum())
    
    # Сохранение датасета с заполненными значениями
    titanic_df.to_csv('data/titanic_filled.csv', index=False)
    
    # Кодирование категориального признака "sex"
    titanic_encoded_df = one_hot_encode_sex(titanic_df)
    
    # Сохранение закодированного датасета
    titanic_encoded_df.to_csv('data/titanic_encoded.csv', index=False)

# Выполнение обработки данных
process_titanic_data()
