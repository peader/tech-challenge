from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

moose_facts = [
    "Moose are the largest members of the deer family.",
    "Moose are found in northern regions of North America, Europe, and Asia.",
    "Moose have long legs and can run fast.",
    "Moose are herbivores and eat plants, fruits, and vegetation.",
    "Moose are solitary animals and only come together during mating season.",
    "Moose are one of the most intelligent animals in the world."
]

import random

@app.route("/random-moose-fact", methods=["GET"])
def get_random_moose_fact():
    return jsonify(random.choice(moose_facts))

@app.route("/moose-facts", methods=["GET"])
def get_moose_facts():
    return jsonify(moose_facts)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
