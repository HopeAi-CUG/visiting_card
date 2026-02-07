import os
from flask import Flask, request, jsonify, render_template
from services.openai_extractor import extract_visiting_card
from services.google_sheets import append_to_sheet

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return render_template("upload.html")

@app.route("/save-card", methods=["POST"])
def save_card():
    data = request.json
    append_to_sheet(data)
    return jsonify({"status": "success"})

@app.route("/extract-card", methods=["POST"])
def extract_card():
    image = request.files["image"]
    image_path = os.path.join("uploads", image.filename)
    image.save(image_path)

    data = extract_visiting_card(image_path)

    return jsonify({
        "status": "success",
        "extracted_data": data
    })


@app.route("/health")
def health():
    return jsonify({"status": "running"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
