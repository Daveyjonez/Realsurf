#Author: David Owens
#File name: scraper.py
#Purpose: Scrapes multiple surf report websites to obtain data about surf
#conditions

#imports
from lxml import html
import requests
import csv


#             Wave height table
#        
#           LOW_WAVE    HIGH_WAVE
#               0           1
#
#  Scripps 0 [     ]     [     ]
#  
#  Blacks  1 [     ]     [     ]
#  
#  ...     2 [     ]     [     ]

msRoot = 'http://www.magicseaweed.com/'
msContainer = """/html/body/div[2]/div[5]/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/div[1]/div/div/div/div/div[1]/div/div[2]/ul[1]/li[1]/text()"""

slRoot = 'http://www.surfline.com/surf-report/'
slContainer = '//*[@id="observed-wave-range"]'

SCRIPPS_INDEX = 0
BLACKS_INDEX = 1

LOW_WAVE = 0
HIGH_WAVE = 1

#create 2d array to hold all wave reports
width, height = 2, 2
Matrix = [[0 for x in range(width)] for y in range(height)]

#get magicseaweed  report
msScrippsPage = requests.get(msRoot+'Scripps-Pier-La-Jolla-Surf-Report/296')
msBlacksPage = requests.get(msRoot+'Torrey-Pines-Blacks-Beach-Surf-Report/295/')

#get Surfline report
slScrippsPage = requests.get(slRoot+'la-jolla-shores-southern-california_4812/')

#make tree from sites
msScrippsTree = html.fromstring(msScrippsPage.content)
slScrippsTree = html.fromstring(slScrippsPage.content)
msBlacksTree = html.fromstring(msBlacksPage.content)

#get wave size
msScrippsWave = msScrippsTree.xpath(msContainer)
slScrippsWave = slScrippsTree.xpath(slContainer)

msBlacksWave = msBlacksTree.xpath(msContainer)

#convert list to string
msScrippsString = ''.join(msScrippsWave)
slScrippsString = ''.join(slScrippsWave)

msBlacksString = ''.join(msBlacksWave)

#remove whitespaces
msScrippsWaveList = msScrippsString.strip()
slScrippsWaveList = msScrippsString.strip()

blacksWaveList = msBlacksString.strip()

#convert to char list
msScrippsWaveList = list(msScrippsWaveList)
slScrippsWaveList = list(slScrippsWaveList)


blacksWaveList = list(blacksWaveList)

#remove '-' between low and high wave report
msScrippsWaveList.pop(1)
slScrippsWaveList.pop(1)

blacksWaveList.pop(1)

#convert from char to int array
msScrippsWaveList = map(int, msScrippsWaveList)
slScrippsWaveList = map(int, slScrippsWaveList)

blacksWaveList = map(int, blacksWaveList)

#assign to wave height matrix
Matrix[SCRIPPS_INDEX][LOW_WAVE] = msScrippsWaveList[0]
Matrix[SCRIPPS_INDEX][HIGH_WAVE] = msScrippsWaveList[1]

Matrix[1][LOW_WAVE] = slScrippsWaveList[0]
Matrix[1][HIGH_WAVE] = slScrippsWaveList[1]

#Matrix[BLACKS_INDEX][LOW_WAVE] = blacksWaveList[0]
#Matrix[BLACKS_INDEX][HIGH_WAVE] = blacksWaveList[1]

print Matrix
