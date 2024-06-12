import pandas as pd
from sklearn.preprocessing import StandardScaler
import os

def preprocess_data(input_path, output_path):
    data = pd.read_csv(input_path)
    scaler = StandardScaler()
    data[['x', 'y']] = scaler.fit_transform(data[['x', 'y']])
    data.to_csv(output_path, index=False)

preprocess_data('train/train_data.csv', 'train/train_data_scaled.csv')
preprocess_data('test/test_data.csv', 'test/test_data_scaled.csv')
preprocess_data('train/train_data_anomalies.csv', 'train/train_data_anomalies_scaled.csv')
