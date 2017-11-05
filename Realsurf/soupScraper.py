#Author: David Owens
 
#File name: soupScraper.py
#Description: html scraper that takes surf reports from various websites. 
#             This data includes wave height, tide, and wind.

import csv
import re
import requests
from bs4 import BeautifulSoup

NUM_SITES = 2

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
msWindClass = 'h5 nomargin-top'
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
This returns the proper attribute for wave height from the surf report sites
'''
def waveTagFilter(tag):
    return (tag.has_attr('class') and 'rating-text' in tag['class']) \
    	or (tag.has_attr('id') and tag['id'] == 'observed-wave-range')
#END METHOD

'''
This method extracts all ints from a list of reports

reports: The list of surf reports from a single website

returns: reportNums - A list of ints of the wave heights
'''
def extractInts(reports):
	reportNums = []

	#extract all ints from the reports and ditch the rest
	for report in reports:
		for char in report:
			try :
				num = int(char)
				reportNums.append(num)
			except:
				pass

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
			reportTag = soup.findAll(waveTagFilter)[0]
			#Add string values to
			reports.append(reportTag.text.strip())
		#notify if fail
		except:
			print ('failure at URL: {}'.format(url))
			pass

	reportNums = extractInts(reports)

	return reportNums
#END METHOD

'''
This method iterates through a list of urls and extracts the wind from
the webpage dependent upon its tag location. Only uses Magiseaweed values

rootUrl: The root url of each surf website
urlList: A list of specific urls to be appended to the root url for each
		 break

tag:	 the html tag where the actual report lives on the page

returns: a list of strings of each breaks measured wind
'''
def extractWind(rootUrl, urlList):
	allWinds = []
	#Loop thru each surf break and collect the current wind reading
	for url in urlList:
		try:
			#request page
			request = requests.get(rootUrl + url)
			#turn into soup
			soup = BeautifulSoup(request.content, 'lxml')
			#get the tag/class where wind value lives
			windClass = soup.find_all('p', {'class':msWindClass})
			#extract the data and cast to int
			for element in windClass:
					data = element.getText()
					wind = int(re.findall('\d+', data)[0])
					allWinds.append(wind)

		#notify if fail
		except Exception as e:
			print('Wind scrape failure @ URL: {}'.format(url))
			print('ERROR:\n{}'.format(e))
			pass

	return allWinds

'''
This method iterates through a list of urls and extracts the tide from
the webpage dependent upon its tag location. Only uses surfline values

rootUrl: The root url of each surf website
urlList: A list of specific urls to be appended to the root url for each
		 break

returns: a list of strings of each breaks current tide
'''
def extractTide(url):
	allTides = []
	#Loop thru each surf break and collect the current wind reading
	try:
		#request page
		request = requests.get(url)
		#turn into soup
		soup = BeautifulSoup(request.content, 'lxml')
		#get the tag/class where tide value lives
		tideContent = soup.find('pre', attrs={'class':'predictions-table'}).text
		tideData = tideContent.strip().splitlines()
		print(tideData)


	#notify if fail
	except Exception as e:
		print('Tide scrape failure @ URL: {}'.format(url))
		print('ERROR:\n{}'.format(e))
		pass
	return allTides

'''
This method calculates the average of the wave heights
'''
#TODO
def calcAverages(surfBreaks):
	return
#END METHOD

#extractTide('http://tides.mobilegeographics.com/locations/5538.html')
