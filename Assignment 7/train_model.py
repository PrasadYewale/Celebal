# train_model.py
from sklearn.datasets import load_diabetes
from sklearn.ensemble import RandomForestRegressor
import pandas as pd
import joblib

# Load dataset
data = load_diabetes()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = data.target

# Train model
model = RandomForestRegressor()
model.fit(X, y)

# Save model
joblib.dump(model, 'diabetes_model.pkl')
