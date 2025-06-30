from flask import Flask, render_template, request, url_for
import requests
from PIL import Image
from io import BytesIO
import os

app = Flask(__name__, static_folder="static")

# Ensure static/images directory exists
os.makedirs("static/images", exist_ok=True)

def download_image(url, filename):
    """Downloads an image from a URL and saves it locally."""
    response = requests.get(url)
    if response.status_code == 200:
        img = Image.open(BytesIO(response.content))
        img.save(f"static/images/{filename}")
        return f"static/images/{filename}"  # Return file path for rendering
    return None

@app.route("/", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        emblem_url = request.form["emblem_url"]
        logo_url = request.form["logo_url"]
        photo_url = request.form["photo_url"]
        fingerprint_url = request.form["fingerprint_url"]

        # Download and save images
        emblem_path = download_image(emblem_url, "emblem.png")
        logo_path = download_image(logo_url, "aadhaar_logo.svg")
        photo_path = download_image(photo_url, "photo.jpg")
        fingerprint_path = download_image(fingerprint_url, "fingerprint.png")

        # Generate URLs for displaying images
        image_paths = {
            "photo_url": url_for("static", filename="images/photo.jpg"),
            "aadhaar_logo": url_for("static", filename="images/aadhaar_logo.svg"),
            "fingerprint_logo": url_for("static", filename="images/fingerprint.png"),
            "emblem_logo": url_for("static", filename="images/emblem.png")
        }

        return render_template("display.html", **image_paths)

    return render_template("form.html")

if __name__ == "__main__":
    app.run(debug=True)