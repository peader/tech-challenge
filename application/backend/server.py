from flask import Flask, jsonify
from flask_cors import CORS
import os 

app = Flask(__name__)
CORS(app)

moose_facts = [
    "Moose are the largest members of the deer family.",
    "Moose are found in northern regions of North America, Europe, and Asia.",
    "Moose have long legs and can run fast.",
    "Moose are herbivores and eat plants, fruits, and vegetation.",
    "Moose are solitary animals and only come together during mating season.",
    "Moose are one of the most intelligent animals in the world.",
    "Moose are twice the size of elk",
    "Moose have special noses that allows it to find water across large ranges",
    "They’re the largest deer!",
    "They can be the most dangerous animals around",
    "They have a prehensile upper lip",
    "They can run, really, really fast",
    "Moose have ‘dewlaps’ (a hanging fold of skin from their neck)",
    "They can swim",
    "Males shed their antlers"
]

import random

@app.route("/random-moose-fact", methods=["GET"])
def get_random_moose_fact():
    return jsonify(random.choice(moose_facts))

@app.route("/moose-facts", methods=["GET"])
def get_moose_facts():
    return jsonify(moose_facts)

@app.route("/image-version", methods=["GET"])
def get_image_version():
    return os.environ['image_version']

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
