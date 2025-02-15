import os
import pandas as pd
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from sklearn.ensemble import IsolationForest

app = Flask(__name__)

# Set upload folder
UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {"csv"}
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Check allowed file types
def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

# Function to detect anomalies
def detect_anomalies(filepath):
    df = pd.read_csv(filepath)
    
    # Ensure required columns exist
    required_columns = ["price", "quantity_ordered", "total"]
    for col in required_columns:
        if col not in df.columns:
            return None, f"Missing required column: {col}"

    # Select numeric features
    X = df[required_columns]

    # Train Anomaly Detection Model
    model = IsolationForest(contamination=0.05, random_state=42)
    df["anomaly_score"] = model.fit_predict(X)

    # Save flagged anomalies
    anomalies = df[df["anomaly_score"] == -1]
    anomalies.to_csv("static/anomaly_detected.csv", index=False)

    return anomalies.to_dict(orient="records"), None

@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        if "file" not in request.files:
            return "No file part"
        
        file = request.files["file"]
        if file.filename == "":
            return "No selected file"
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(filepath)

            # Process anomalies
            anomalies, error = detect_anomalies(filepath)
            if error:
                return f"Error: {error}"
            
            return render_template("dashboard.html", anomalies=anomalies)

    return render_template("upload.html")

if __name__ == "__main__":
    app.run(debug=True)
