# ---------------------------- IMPORTS ------------------------------- #

import os
from PIL import Image  
import numpy as np  
from sklearn.cluster import KMeans  
from flask import Flask, render_template, request
app = Flask(__name__)

n=10
IMAGE_SAMPLE = "static/sample.jpg"
UPLOAD_FOLDER = "static/uploads"

# ---------------------------- ALLOWED IMAGE EXTENSIONS ------------------------------- #

ALLOWED_EXTENSIONS = {"jpg", "jpeg", "png"}

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


# ---------------------------- GET TOP COLORS FUNCTION ------------------------------- #

"""
Using K-Means since it was recommended by the AI in order for faster processing.
Hey, at least I'm honest :)))
"""

def get_top_colors(image_path, n=10):  

    # OPEN IMAGE
    img = Image.open(image_path).convert('RGB')  
    img.thumbnail((300, 300))  # Decided to resize for speed. HD images can be quite big and could take a lot of time
    pixels = np.array(img)  
    pixel_list = pixels.reshape(-1, 3) # Flatten to a 3D Grid for better view and for K-Means

    # K-MEANS for faster processing
    kmeans = KMeans(n_clusters=n, random_state=42, n_init=10)  
    kmeans.fit(pixel_list)  # Clusters pixels by RGB distance 
    labels = kmeans.labels_  # Which cluster each pixel belongs to (array of ints 0-9)  
    centroids = kmeans.cluster_centers_.astype(int)  # N rows x 3 cols RGB (0-255)

    # CALCULATE COLOR SHARE
    counts = np.bincount(labels)  # pixels per cluster [e.g. [2000, 1500, ...]]  
    percentages = counts / len(labels) * 100

    # Build output list and sort by %
    colors = []  
    for i in range(n):  
        rgb = tuple(int(x) for x in centroids[i]) # (255, 0, 0)  
        # Hex: format each byte as 2-digit hex, uppercase
        hex_color = f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}".upper()  
        colors.append({  
            'rgb': rgb,  
            'hex': hex_color,  
            'percent': float(percentages[i])
        })  
    return sorted(colors, key=lambda x: x['percent'], reverse=True)  

    """
    colors = get_top_colors(HERE/"static/sample.jpg", 10)

    for i, c in enumerate(colors, 1):  
        print(f"{i}. {c['hex']} ({c['rgb']}) {c['percent']:.1f}%")
    
    """

# ---------------------------- FLASK ROUTES ------------------------------- #

# HOME
@app.route("/")
def index():
    sample_colors = get_top_colors("static/sample.jpg")
    
    # Clean uploads folder on every return to home
    for f in os.listdir(UPLOAD_FOLDER):
        os.remove(os.path.join(UPLOAD_FOLDER, f))

    return render_template("upload.html", sample_colors=sample_colors)

# UPLOAD PICTURE
@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["image"]
    if file and allowed_file(file.filename):
        save_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(save_path)
        colors = get_top_colors(save_path)
        return render_template("results.html", colors=colors, filename=file.filename)
    return "Invalid file!", 400

# MAIN
if __name__ == "__main__":
    app.run(debug=True)