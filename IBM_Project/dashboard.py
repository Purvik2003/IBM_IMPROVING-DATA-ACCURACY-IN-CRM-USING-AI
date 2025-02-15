from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# Load detected anomalies
def load_anomalies():
    try:
        df = pd.read_csv("anomaly_detected.csv")
        return df[df["anomaly_score"] == -1].to_dict(orient="records")  # Show only anomalies
    except Exception as e:
        return []

@app.route("/")
def home():
    anomalies = load_anomalies()
    return render_template("dashboard.html", anomalies=anomalies)

if __name__ == "__main__":
    app.run(debug=True)
