#Import flask for framework
from Realsurf import app
#Import scraping functions for wave height functions
from soupScraper import *

#Lists to hold break data
slFinal = []
msFinal = []
windFinal = []
tideFinal = []
slReports = []
msReports = []

slReports = extractReports(slRootUrl, slUrls, slTag, slTagText)
msReports = extractReports(msRootUrl, msUrls, msTag, msTagText)
windFinal = extractWind(msRootUrl, msUrls)

#Default route to landing page
@app.route('/')
def index():
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
        windValue = windFinal[0]

    elif surfBreak == 'scripps':
        waveHeight = str(slReports[2]) + '-' + str(slReports[3])
        windValue = windFinal[1]


    elif surfBreak == 'blacks':
        waveHeight = str(slReports[4]) + '-' + str(slReports[5])
        windValue = windFinal[2]

    else:
        return render_template("unknownPage.html", name=surfBreak)

    return render_template("breakInfo.html",
                           name=surfBreak,
                           windValue=windValue,
                           waveValues=waveHeight)

if __name__ == "__main__":
    app.run(debug=True)
