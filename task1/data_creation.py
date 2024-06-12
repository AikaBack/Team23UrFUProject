import numpy as np
import pandas as pd
import os

def create_data(n_samples=100, noise=False):
    np.random.seed(0)
    x = np.linspace(0, 10, n_samples)
    y = 2 * x + 1
    if noise:
        y += np.random.normal(0, 1, n_samples)
    data = pd.DataFrame({'x': x, 'y': y})
    return data

os.makedirs('train', exist_ok=True)
os.makedirs('test', exist_ok=True)

train_data = create_data(noise=True)
test_data = create_data(noise=False)

train_data.to_csv('train/train_data.csv', index=False)
test_data.to_csv('test/test_data.csv', index=False)

train_data_anomalies = train_data.copy()
train_data_anomalies.loc[::10, 'y'] += 10

train_data_anomalies.to_csv('train/train_data_anomalies.csv', index=False)