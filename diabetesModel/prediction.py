import numpy as np
import pandas as pd
import joblib


diabetes_data = pd.read_pickle('data\diabetes_binary.pkl')
diabetes_data = diabetes_data.astype('int64')


model, reference_features, label = joblib.load('loadedModel.pkl')

input_data = diabetes_data
input = input_data.sample(10)

X_new = input.iloc[:, :-1]
y_new = input.iloc[:, -1]

prediction = model.predict(X_new).flatten()
predicted_classes = (prediction > 0.5).astype(int)

