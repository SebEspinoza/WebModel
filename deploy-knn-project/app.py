from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
model = pickle.load(open("knn.pkl", "rb"))


@app.route("/")
def modelo():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    minTemp = float(request.form["MinTemp"])
    maxTemp = float(request.form["MaxTemp"])
    rainFall = float(request.form["Rainfall"])
    h9am = float(request.form["Humidity9am"])
    h3pm = float(request.form["Humidity3pm"])
    p9am = float(request.form["Pressure9am"])
    p3pm = float(request.form["Pressure3pm"])
    t9am = float(request.form["Temp9am"])
    t3pm = float(request.form["Temp3pm"])
    prediction = model.predict(
        [[minTemp, maxTemp, rainFall, h9am, h3pm, p9am, p3pm, t9am, t3pm]]
    )
    if prediction == 0:
        prediction = "No"
    else:
        prediction = "Sí"
    return render_template("index.html", prediction_text=prediction)


if __name__ == "__main__":
    app.run()
