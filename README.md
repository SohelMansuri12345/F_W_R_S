---

# Fruit Warehouse Recommendation System

This application predicts sales-related outputs based on input parameters like the number of days, the number of fruits, and fruit costs. It leverages a pre-trained machine learning model stored as `LR.pkl` to predict the recommended quantity, margin, selling price, total income, and total profit.

## Features

- **Predictive Modelling**: Uses a logistic regression model to predict various sales metrics.
- **User-friendly Interface**: Easy-to-use web interface where users can input data and view predictions.
- **Results Visualization**: Outputs are displayed in a clean table format directly in the browser.

## Installation

To run this application, you'll need Python and some additional libraries installed. Here's how to get started:

### Prerequisites

- Python 3
- Flask
- Pandas
- NumPy
- Pickle

You can install all required packages using pip:

```bash
pip install Flask pandas numpy
```
### Run the Application

To run the application, execute:

```bash
python app.py
```

The application will start running on `http://127.0.0.1:8080`. You can access it via any web browser.

## Usage

Once the application is running:
1. Navigate to `http://127.0.0.1:8080` in your web browser.
2. Enter the required inputs (days, fruits, and fruit cost).
3. Click the **Predict** button to see the sales predictions.

The results will be displayed in a table format showing recommended quantity, margin, selling price, total income, and total profit.

## Screenshots

![Screenshot (173)](https://github.com/SohelMansuri12345/Fruit-Warehouse-Recommendation-System/assets/168846227/d93ab476-c129-42c0-b9eb-6929296ac63a)

![Screenshot (174)](https://github.com/SohelMansuri12345/Fruit-Warehouse-Recommendation-System/assets/168846227/167e6f8b-b537-442d-a3a8-0894ff68b575)

Thank you...

## Author 
**Sohel Mansuri**
