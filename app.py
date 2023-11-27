from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
model = pickle.load(open("modelos.pkl", "rb"))


@app.route("/", methods=["GET"])
def modelo():
    return render_template("index.html")


@app.route("/", methods=["POST"])
def predict():
    cantidad = float(request.form["cantidad"])
    mes = float(request.form["mes"])
    prediction = model.predict([[cantidad, mes]])[0]

    # Adding the prediction text
    prediction_text = f"La cantidad de stock necesaria para el siguiente mes del seleccionado es {prediction}"

    print(prediction_text)
    return render_template("index.html", prediction_text=prediction_text)


if __name__ == "__main__":
    app.run(port=5500, debug=True)
