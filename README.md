# inventory-optimization-api

This project implements a lightweight API using **FastAPI** and **RandomForestRegressor** to predict meal demand for inventory optimization in food-related businesses. The purpose of this repository is to **showcase the backend logic and model implementation**, including API testing visuals and prediction insights.

## Project Objective

- Predict **meal demand** based on `meal_id` and `day_of_week`
- Help determine optimal recurring stock levels
- Minimise understocking for inventory planning

---

## Model Used

- **Random Forest Regressor** from `scikit-learn`
- Trained on features: `meal_id` and `day_of_week` (encoded)
- Target: `demand`
- Model was tested in Pycharm before porting to FastAPI for demonstration

---

## API Testing and Results

Below are screenshots of successful API tests using SwaggerUI after deployment:



> *All predictions were rounded and displayed along with current recurring stock (from dataset).*

---

## Files Included

- `app.py`: Main FastAPI application
- `images/`: API result screenshots
- `README.md`: Project documentation

---

## Notes

- **CSV file is not uploaded** due to data privacy.
- This repo is for demonstration only — actual data and deployment pipeline are internal.

---

## Future Work 

- Integrate with partner app frontend
- Automate predictions using scheduled queries in BigQuery
- Explore time series models for demand trends that takes note of edge-cases such as festive seasons and weather conditions

---

