#Author: David Owens
#File name: soupScraper.py
#Description: html scraper that takes surf reports from various websites

import csv
import requests
from bs4 import BeautifulSoup

SUNSET_CLIFFS_INDEX = 0
SCRIPPS_INDEX = 1
BLACKS_INDEX = 2

###################### SURFLINE URL STRINGS AND TAG ###########################

slRootUrl = 'http://www.surfline.com/surf-report/'
slSunsetCliffs = 'sunset-cliffs-southern-california_4254/'
slScrippsUrl = 'scripps-southern-california_4246/'
slBlacksUrl = 'blacks-southern-california_4245/'
slCardiffUrl = 'cardiff-southern-california_4786/'

slTagText = 'observed-wave-range'
slTag = 'id'

#list of surfline URL endings
slUrls = [slSunsetCliffs, slScrippsUrl, slBlacksUrl]

###############################################################################


#################### MAGICSEAWEED URL STRINGS AND TAG #########################

msRootUrl = 'http://magicseaweed.com/'
msSunsetCliffs = 'Sunset-Cliffs-Surf-Report/4211/'
msScrippsUrl = 'Scripps-Pier-La-Jolla-Surf-Report/296/'
msBlacksUrl = 'Torrey-Pines-Blacks-Beach-Surf-Report/295/'

msTagText = 'rating-text'
msTag = 'li'

#list of magicseaweed URL endings
msUrls = [msSunsetCliffs, msScrippsUrl, msBlacksUrl]

###############################################################################


'''
This returns the proper attribute from the surf report sites
'''
def reportTagFilter(tag):
    return (tag.has_attr('class') and 'rating-text' in tag['class']) \
    	or (tag.has_attr('id') and tag['id'] == 'observed-wave-range')


'''
This method checks if the parameter is of type int
'''
def representsInt(s):
    try: 
        int(s)
        return True
    
    except ValueError:
        return False


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
			if representsInt(char) == True:
				num = int(char)
				reportNums.append(num)

	return reportNums


'''
This method iterates through a list of urls and extracts the surf report from
the webpage dependent upon its tag location

rootUrl: The root url of each surf website
urlList: A list of specific urls to be appended to the root url for each 
		 break

tag:	 the html tag where the actual report lives on the page

returns: a list of strings of each breaks surf report
'''
def extract_Reports(rootUrl, urlList, tag, tagText):
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
			
			#get the tag where surflines report lives
			reportTag = soup.findAll(reportTagFilter)[0]
				
			reports.append(reportTag.text.strip())		

		#notify if fail	
		except:
			print 'scrape failure at URL ', index
			pass

	reportNums = extractInts(reports)

	return reportNums
#END METHOD

slReports = extract_Reports(slRootUrl, slUrls, slTag, slTagText)
msReports = extract_Reports(msRootUrl, msUrls, msTag, msTagText)

def getAverage(waveHeightList):
	for num in waveHeightList:
		



