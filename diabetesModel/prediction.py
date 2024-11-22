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


# ---- OPTIONAL ------ SHOULD BE DONE IN FRONTEND
categories = {
    "No Diabetes": lambda prob: prob < 0.4,
    "Pre-Diabetes": lambda prob: 0.4 <= prob <= 0.6,
    "Diabetes": lambda prob: prob > 0.6
}
#percent
for i, prob in enumerate(prediction):
    prob_percentage = prob * 100  # Convert to percentage
    for category, condition in categories.items():
        if condition(prob_percentage):  # Use percentage in the condition
            print(f"Sample {i + 1}: {category} (Probability of having diabetes: {prob_percentage:.2f}%)")
            break

