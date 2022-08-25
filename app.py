from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)
model = joblib.load(open('final_RFModel.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        year = request.form['year']
        age = request.form['age']
        odometer = request.form['odometer']
        cylinders = request.form['cyl']
        manufacturer = request.form['manufacturer']
        vehicle_model = request.form['model']
        fuel = request.form['fuel']
        condition = request.form['condition']
        transmission = request.form['trans']
        title_status = request.form['title']
        drive = request.form['drive']
        color = request.form['paint']
        vehicle_type = request.form['type']

        features = [year, age, odometer, cylinders, manufacturer, vehicle_model, fuel, title_status, transmission,
                    condition, vehicle_type, drive, color, ]
        x = np.array([features])

        le_manufacturer = LabelEncoder()
        le_vehicle_model = LabelEncoder()
        le_fuel = LabelEncoder()
        le_title_status = LabelEncoder()
        le_transmission = LabelEncoder()
        le_condition = LabelEncoder()
        le_vehicle_type = LabelEncoder()
        le_drive = LabelEncoder()
        le_color = LabelEncoder()

        x[:, 4] = le_manufacturer.fit_transform(x[:, 4])
        x[:, 5] = le_vehicle_model.fit_transform(x[:, 5])
        x[:, 6] = le_fuel.fit_transform(x[:, 6])
        x[:, 7] = le_title_status.fit_transform(x[:, 7])
        x[:, 8] = le_transmission.fit_transform(x[:, 8])
        x[:, 9] = le_condition.fit_transform(x[:, 9])
        x[:, 10] = le_vehicle_type.fit_transform(x[:, 10])
        x[:, 11] = le_drive.fit_transform(x[:, 11])
        x[:, 12] = le_color.fit_transform(x[:, 12])

        x = x.astype(float)

        prediction = model.predict(x)
        output = round(prediction[0], 2)
        return render_template('index.html', prediction_text='Expected price is $ {}'.format(output))
    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
