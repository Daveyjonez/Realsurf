#Import flask for framework
from flask import Flask
from flask import render_template
#Import scraping functions for wave height functions
from soupScraper import *

reportsFinal = []

app = Flask(__name__)

#Default route to landing page
@app.route('/')
def index():
    slReports = extractReports(slRootUrl, slUrls, slTag, slTagText)
    msReports = extractReports(msRootUrl, msUrls, msTag, msTagText)

    reportsFinal.append(slReports)
    reportsFinal.append(msReports)

    return render_template("landingPage.html")

#Route to simple about page
@app.route('/about')
def about():
    return render_template("about.html")

#Route to specific surf breaks
@app.route('/<surfBreak>')
def waveHeight(surfBreak):

    if surfBreak == 'sunsetcliffs':
        waveHeight = str(slReports[0]) + '-' + str(slReports[1])

    elif surfBreak == 'scripps':
        waveHeight = str(slReports[2]) + '-' + str(slReports[3])

    elif surfBreak == 'blacks':
        waveHeight = str(slReports[4]) + '-' + str(slReports[5])

    else:
        return render_template("unknownPage.html", name=surfBreak)

    return render_template("breakInfo.html", name=surfBreak,
        waveValues=waveHeight)

if __name__ == "__main__":
    app.run(debug=True)
