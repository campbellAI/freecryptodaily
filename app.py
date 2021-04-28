from flask import Flask, request, render_template, session, redirect
import numpy as np
from pineapple import *

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.route('/', methods=("POST", "GET"))
def run():

	starting_hand, deck = deal_starting_hand()

	starting_hand_imgs = [CARD_IMAGE_MAP[c] for c in starting_hand]

	return render_template('index.html', starting_hand_imgs=starting_hand_imgs)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
