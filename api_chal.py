import requests
from json import loads
import dateutil.parser
import datetime
import iso8601
import json
from urllib2 import urlopen

# Hello, greetings from Santa Ana, CA, just wanted to thank you(person checking out my work) ahead of time
# and for looking over my application

# Stage 0: registration
info = { "email" : "eandres1@berkeley.com", "github" : "https://github.com/ErickAndres/code2040.git"}
url = "http://challenge.code2040.org/api/register"
token = requests.post(url, data=json.dumps(info)) #json.dumps(info))
#tokenData = token.json()
next = token.json()
codeiD = next['result']
info = {'token': codeiD}
print info

# Stage 1: Reverse
getstring = 'http://challenge.code2040.org/api/getstring'
result1 = requests.post(getstring, data=json.dumps(info))
string = result1.json().get('result')
print "This is the current string: " + string

def reverse(string):
	return string[::-1]

reversedString = reverse(string)

print "This is the reversed string: " + reversedString
data2 = {'token':'p5loYNOEHs', 'string': reversedString}
validStr = 'http://challenge.code2040.org/api/validatestring'
result1= requests.post(validStr, data=json.dumps(data2))
tokenData = result1.json()

# Stage 2: Haystack
hay = 'http://challenge.code2040.org/api/haystack'
result2 = requests.post(hay, data=json.dumps(info))	#was data
jsonData = result2.json()
haystack = jsonData['result']['haystack']
needle = jsonData['result']['needle']

def haystackPos(needle, haystack):
	return haystack.index(needle)

result = haystackPos(needle, haystack)
print "This is result2: " + str(result)
data3 = {'token': 'p5loYNOEHs', 'needle': result}
valid = 'http://challenge.code2040.org/api/validateneedle'
result3 = requests.post(valid, data=json.dumps(data3))
tokenData2 = result3.json()

# Stage 3: Prefix
prefix = 'http://challenge.code2040.org/api/prefix'
result3 = requests.post(prefix, data=json.dumps(info))
jsonData = result3.json()
prefix = jsonData['result']['prefix']
words = jsonData['result']['array']

def notPrefix(prefix, array):
	lst = []
	for el in array:
		if el.startswith(prefix) == False:
			lst.append(el) #word does not match prefix so we add to lst that we are going to return
	return lst

prefixRes = notPrefix(prefix, words)
data3 = {'token': 'p5loYNOEHs', 'array': prefixRes}
validPrefix = 'http://challenge.code2040.org/api/validateprefix'
result3 = requests.post(validPrefix, data=json.dumps(data3))
tokenData3 = result3.json()
print(tokenData3)

# Stage 4: The dating game
time = 'http://challenge.code2040.org/api/time'
result4 = requests.post(time, data=json.dumps(info)) #info was data
jsonData = result4.json()
date = jsonData['result']['datestamp']
interval = jsonData['result']['interval']

def finaldate(datestamp, interval):
	#interval = int(interval) casting to int to make sure arithmetic works
	date = iso8601.parse_date(datestamp) # parses common form of ISO 8601 date strings into datetime objects
	interval = datetime.timedelta(0, interval) #new interval value that represents diff between dates
	final = date + interval #adding the interval to date as specified
	final = final.isoformat() # convert string representation of date back to iso format
	format1 = final.split('+')[0] #split up iso date into a list
	format1 += '.000Z' #to fit format specified
	return format1 

finalResult = finaldate(date, interval)
print "This is the last: " + finalResult
finalData = {'token': 'p5loYNOEHs', 'datestamp': finalResult}
validDate = 'http://challenge.code2040.org/api/validatetime'
result4 = requests.post(validDate, data=json.dumps(finalData))
tokenData4 = result4.json()
print(tokenData4)

#Checking my grades
check_grades = requests.post('http://challenge.code2040.org/api/status', json=info)
grades = check_grades.json()
print grades



