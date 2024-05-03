from flask import Flask, request, render_template
import pandas as pd
import pickle
import numpy as np

app = Flask(__name__)

# Load the model
model = pickle.load(open('LR.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    days = int(request.form['days'])
    fruits = int(request.form['fruits'])
    fruit_cost = int(request.form['fruit_cost'])

    input_data = pd.DataFrame([[days, fruits, fruit_cost]],
                              columns=['days', 'fruits', 'fruit cost'])

    # Make prediction
    prediction = model.predict(input_data)

    # Extract values needed for further calculation from the prediction
    recommended_quantity = int(np.ceil(prediction[0][1]))  # Assume prediction[0][1] is the 'Sold Quantity'
    margin = int(np.ceil(prediction[0][3]))                              # Assume prediction[0][3] is 'Margin'
    selling_price = int(np.ceil(prediction[0][4]))                       # Assume prediction[0][4] is 'Selling Price'

    # Calculate 'Total Income' and 'Total Profit'
    total_income = selling_price * recommended_quantity
    total_profit = margin * recommended_quantity

    # Prepare the result DataFrame with the specific columns
    result_data = {
        'Recommended Quantity': [recommended_quantity],
        'Margin': [margin],
        'Selling Price': [selling_price],
        'Total Income': [total_income],
        'Total Profit': [total_profit]
    }
    result_df = pd.DataFrame(result_data)

    # Convert DataFrame to HTML, avoiding the index in the HTML table
    result_html = result_df.to_html(classes='data', index=False)

    return render_template('result.html', tables=[result_html])

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)
