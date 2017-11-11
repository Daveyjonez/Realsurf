from flask import Flask

app = Flask(__name__)

import Realsurf.views
import Realsurf.soupScraper
