from fastapi import FastAPI, Query
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

app = FastAPI()

# Data Load and preprocess
file_path = r"C:\Users\chan-\OneDrive\Desktop\Y4\StockOptiMLV2.csv"
df = pd.read_csv(file_path)

# Convert to datetime
if 'event_date' in df.columns:
    df['event_date'] = pd.to_datetime(df['event_date'], errors='coerce')

# Eliminate rows with missing values
df = df.dropna(subset=['meal_id', 'day_of_week', 'demand', 'current_rec_stock'])

# Encode day_of_week
df['day_of_week_encoded'] = df['day_of_week'].astype('category').cat.codes

# Train the model
X = df[['meal_id', 'day_of_week_encoded']]
y = df['demand']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestRegressor(n_estimators=200, random_state=42)
model.fit(X_train, y_train)


@app.get("/predict/")
def predict_demand(
        meal_id: int = Query(...),
        day_of_week: str = Query(...)
):
    try:
        categories = df['day_of_week'].astype('category').cat.categories
        if day_of_week not in categories:
            return {"error": f"Invalid day_of_week. Must be one of: {list(categories)}"}

        day_encoded = categories.get_loc(day_of_week)

        matched_rows = df[(df['meal_id'] == meal_id) & (df['day_of_week'] == day_of_week)]
        if matched_rows.empty:
            return {"error": "No matching data found for the given meal_id and day_of_week"}

        current_rec_stock = matched_rows['current_rec_stock'].mean()

        input_data = pd.DataFrame([{
            'meal_id': meal_id,
            'day_of_week_encoded': day_encoded
        }])
        prediction = round(model.predict(input_data)[0])

        return {
            "meal_id": meal_id,
            "day_of_week": day_of_week,
            "current_rec_stock": round(current_rec_stock, 0),
            "predicted_demand": prediction
        }

    except Exception as e:
        return {"error": str(e)}


@app.get("/get")
def get_meal_ids():
    """Return a unique list of meal_ids available for prediction"""
    unique_ids = df['meal_id'].dropna().unique().tolist()
    return {"available_meal_ids": sorted(unique_ids)}
