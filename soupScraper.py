#Author: David Owens
#File name: soupScraper.py
#Description: html scraper that takes surf reports from various websites

import csv
import requests
from bs4 import BeautifulSoup

NUM_SITES = 2

reportsFinal = []

####################### SURFLINE URL STRINGS AND TAG ###########################

slRootUrl = 'http://www.surfline.com/surf-report/'
slSunsetCliffs = 'sunset-cliffs-southern-california_4254/'
slScrippsUrl = 'scripps-southern-california_4246/'
slBlacksUrl = 'blacks-southern-california_4245/'
slCardiffUrl = 'cardiff-southern-california_4786/'

slTagText = 'observed-wave-range'
slTag = 'id'

#list of surfline URL endings
slUrls = [slSunsetCliffs, slScrippsUrl, slBlacksUrl]

################################################################################


##################### MAGICSEAWEED URL STRINGS AND TAG #########################

msRootUrl = 'http://magicseaweed.com/'
msSunsetCliffs = 'Sunset-Cliffs-Surf-Report/4211/'
msScrippsUrl = 'Scripps-Pier-La-Jolla-Surf-Report/296/'
msBlacksUrl = 'Torrey-Pines-Blacks-Beach-Surf-Report/295/'

msTagText = 'rating-text'
msTag = 'li'

#list of magicseaweed URL endings
msUrls = [msSunsetCliffs, msScrippsUrl, msBlacksUrl]

################################################################################

'''
This class represents a surf break. It contains all wave, wind, & tide data
associated with that break relevant to the website
'''
class surfBreak:
	def __init__(self, name, low, high, wind, tide):
		self.name = name
		self.low = low
		self.high = high
		self.wind = wind
		self.tide = tide

	#toString method
	def __str__(self):
		return '{0}: Wave height: {1}-{2} Wind: {3} Tide: {4}'.format(
                self.name, self.low, self.high, self.wind, self.tide)
#END CLASS

'''
This returns the proper attribute from the surf report sites
'''
def reportTagFilter(tag):
    return (tag.has_attr('class') and 'rating-text' in tag['class']) \
    	or (tag.has_attr('id') and tag['id'] == 'observed-wave-range')
#END METHOD

'''
This method checks if the parameter is of type int
'''
def representsInt(s):
    try:
        int(s)
        return True

    except ValueError:
        return False
#END METHOD

'''
This method extracts all ints from a list of reports

reports: The list of surf reports from a single website

returns: reportNums - A list of ints of the wave heights
'''
def extractInts(reports):
	reportNums = []
	num = 0

	#extract all ints from the reports and ditch the rest
	for report in reports:
		for char in report:
			if representsInt(char) == True:

				num = int(char)
				reportNums.append(num)

	return reportNums
#END METHOD

'''
This method iterates through a list of urls and extracts the surf report from
the webpage dependent upon its tag location

rootUrl: The root url of each surf website
urlList: A list of specific urls to be appended to the root url for each
		 break

tag:	 the html tag where the actual report lives on the page

returns: a list of strings of each breaks surf report
'''
def extractReports(rootUrl, urlList, tag, tagText):
	#empty list to hold reports
	reports = []
	reportNums = []
	index = 0

	#loop thru URLs
	for url in urlList:
		try:
			index += 1
			#request page
			request = requests.get(rootUrl + url)

			#turn into soup
			soup = BeautifulSoup(request.content, 'lxml')

			#get the tag where surf report lives
			reportTag = soup.findAll(reportTagFilter)[0]

			reports.append(reportTag.text.strip())

		#notify if fail
		except:
			print ('scrape failure at URL {}'.format(index))
			pass

	reportNums = extractInts(reports)

	return reportNums
#END METHOD

'''
This method calculates the average of the wave heights
'''
'''
def calcAverages(reportList):
	#empty list to hold averages
	finalAverages = []
	listIndex = 0
	waveIndex = 0

	#loop thru list of reports to calc each breaks ave low and high
	for x in range(0, 6):
			#get low ave
			average = (reportList[listIndex][waveIndex]
				+ reportList[listIndex+1][waveIndex]) / NUM_SITES

			finalAverages.append(average)

			waveIndex += 1

	return finalAverages
#END METHOD
'''
slReports = extractReports(slRootUrl, slUrls, slTag, slTagText)
msReports = extractReports(msRootUrl, msUrls, msTag, msTagText)

reportsFinal.append(slReports)
reportsFinal.append(msReports)

print ('Surfline:     {}'.format(slReports))
print ('Magicseaweed: {}'.format(msReports))