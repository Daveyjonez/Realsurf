# R E A L S U R F
The purpose of this project is build a one stop website for all surf reports that I frequent in the Southern California/San Diego area. Currently, multiple surf report websites (Surfline, Magicseaweed, Solspot, etc.) can provide differing surf reports, especially when it comes to wave height. Instead of visiting these sites individually and trying to consturct the actual wave height in my head based off of how much I trust each site,how well they have reported wave height in the past, and my own personal knowledge, I figured I could use some algorithm to calculate one "Super average" of wave height. The main surf breaks I will be using as a proof of concept are Scripps, Blacks, and Cardiff. These are the breaks I surf the most and am most interested in seeing the results for.

http://www.surfline.com/home/index.cfm

http://magicseaweed.com/

http://solspot.com/

#L A N G U A G E S

The wave height data is pulled from the surf report websites via python scraper I wrote with the help of the Beautiful Soup library.
The html of REALSURF will pull variables from this python script in order to update at regular intervals. I intend to host on Heroku and hopefully allow my friends and I to use this site as our go to surf report!

#A L G O R I T H M

The algorithm will be a simple weighted average of the low and high end wave heights with different weights applied to different sites depending upon their past accuracy in reporting wave heights. Ideally, as time goes on, I will add a validation system for these weights which would consist of me rating how accurate each site was after I went surfing. Therfore, weighting can be dynamic and constantly updating, allowing for the most accurate report on REALSURF.

#D E S I G N

The intended UI is modern and minimal which will allow users to see only the data they came to REALSURF for. This layout is also optimal for translating to a mobile platform in the future as I build this project out more. 



