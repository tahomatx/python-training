"""
$env:FLASK_APP = "main.py"
$env:FLASK_DEBUG = 1
flask run
"""

import tensorflow as tf
from flask import Flask, jsonify, request
from PIL import Image
import io, logging
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


# @app.route('/healthcheck')
# def healthcheck():
#     return jsonify({
#       'status': 'ok'
#     })


global model, graph

sess = tf.compat.v1.Session()
tf.keras.backend.set_session(sess)
model = tf.keras.models.load_model('model.h5', compile=False)
model._make_predict_function()
graph = tf.compat.v1.get_default_graph()

labels = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

print(labels[np.argmax(model.predict(np.random.random((1, 32, 32, 3)).astype(np.float32)), axis=1)[0]])

@app.route('/', methods=['POST'])
def predict():
  try:
    image = Image.open(io.BytesIO(request.data))
    image = image.convert("RGB")
    image = image.resize((32, 32))
    image = np.array(image)[np.newaxis] / 255.

    with graph.as_default():
      tf.keras.backend.set_session(sess)
      pred = model.predict(image)

      return jsonify({
        'predict': labels[np.argmax(pred, axis=1)[0]]
      })
  except Exception as e:
    logging.exception(e)
    return jsonify({
      'error': {
        'title': 'Unexpected error'
      }
    }), 500

if __name__=="__main__":
  app.run(host='0.0.0.0')
