# Waiter Tips Prediction Project

## Project Overview
This project uses Machine Learning (Linear Regression with scikit-learn) to predict the tip amount given to a waiter based on total bill, gender, smoker status, day of the week, time of day, and party size.

## Technologies Used
- Python 3
- Pandas & NumPy: Data processing and numerical calculations.
- Plotly Express: Interactive data visualizations.
- Scikit-Learn: Model building, data splitting, and Linear Regression.

## How to Run
1. Clone the repository:
   git clone https://github.com/lianahovsepyan/prediction-project.git
2. Install dependencies:
   python3 -m pip install pandas numpy plotly scikit-learn
3. Run the solution script:
   python3 solution.py

## Model Performance & Evaluation
- Algorithm: LinearRegression from sklearn.linear_model.
- Evaluation Metric: R2 score calculated using model.score(xtest, ytest).

## Status
Model successfully created and tested.
