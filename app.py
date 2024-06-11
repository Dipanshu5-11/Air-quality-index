import pickle
from flask import Flask, render_template, request

app = Flask(__name__)

# Load the trained model
model_filename = 'random_forest_model.pkl'
with open(model_filename, 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the input feature values from the user's form submission
    input_features = [float(x) for x in request.form.values()]

    # Make a prediction using the loaded model
    prediction = model.predict([input_features])[0]

    # Determine the Air Quality category based on the prediction
    air_quality = 'Poor' if prediction >= 200 else 'Moderate' if prediction >= 100 else 'Good'

    return render_template('index.html', prediction_text=f'AQI Prediction: {prediction:.2f}', air_quality=air_quality)

if __name__ == '__main__':
    app.run(debug=True)
