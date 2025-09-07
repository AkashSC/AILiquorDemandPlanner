import pandas as pd
import pickle

def load_model():
    with open('model.pkl', 'rb') as f:
        return pickle.load(f)

def prepare_input(date, region, product_type):
    date = pd.to_datetime(date)
    input_df = pd.DataFrame([{
        'month': date.month,
        'day': date.day,
        'year': date.year,
        f'region_{region}': 1,
        f'product_type_{product_type}': 1
    }])

    # Fill missing columns with 0
    model = load_model()
    expected_cols = model.get_booster().feature_names
    for col in expected_cols:
        if col not in input_df.columns:
            input_df[col] = 0

    return input_df[expected_cols]

def predict_sales(date, region, product_type):
    model = load_model()
    input_df = prepare_input(date, region, product_type)
    prediction = model.predict(input_df)[0]
    return round(prediction, 2)
