from flask import Flask

app = Flask(__name__)

#import soupScraper
from Realsurf import soupScraper
from Realsurf import views
