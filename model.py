import pandas as pd
import xgboost as xgb
import pickle

# Load data
df = pd.read_csv('data/liquor_sales.csv')

# Feature engineering
df['date'] = pd.to_datetime(df['date'])
df['month'] = df['date'].dt.month
df['day'] = df['date'].dt.day
df['year'] = df['date'].dt.year

# Encode categorical features
df = pd.get_dummies(df, columns=['region', 'product_type'])

# Define features and target
X = df.drop(['sales', 'date'], axis=1)
y = df['sales']

# Train model
model = xgb.XGBRegressor()
model.fit(X, y)

# Save model
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)
