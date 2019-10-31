import os
import json

from flask import Flask
from flask import render_template

# Setup the Flask application.

app = Flask(__name__)

@app.route('/')
def index():
    title = os.environ.get('HOMEROOM_TITLE', 'Workshops')
    branding = os.environ.get('HOMEROOM_BRANDING', 'openshift')
    banner_image = banner_images.get(branding, banner_images['openshift'])

    visible_workshops = list(filter_out_hidden(workshops))

    return render_template('workshops.html', title=title,
            banner_image=banner_image, workshops=visible_workshops)
