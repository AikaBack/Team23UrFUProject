import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

data = pd.read_csv('train/train_data_scaled.csv')
X = data[['x']]
y = data['y']

model = LinearRegression()
model.fit(X, y)

with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)
