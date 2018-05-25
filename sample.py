from flask import Flask, render_template, request, redirect, url_for
import numpy as np
import cv2

app = Flask(__name__)

@app.route("/")
def index():
    return "With love from Team sommelier..."

@app.route("/upload", methods = ["POST"])
def upload():
    stream = request.files["file"].stream
    img_array = np.asarray(np.asarray(bytearray(stream.read()),
                                      dtype=np.uint8))
    img = cv2.imdecode(img_array, 1)
    gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    cv2.imwrite("static/gray.png", gray_img)
    return "http://133.130.99.146:10020/static/gray.png"


if __name__ == "__main__":
    print(app.url_map)
    app.debug = True
    app.run(host="0.0.0.0", port=10020)
