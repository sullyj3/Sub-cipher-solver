import requests
url = "http://www.dictionaryapi.com/api/v1/references/collegiate/xml/"

with open('apikey.txt') as keyfile:
    key = keyfile.read().strip()

def geturl(word):
    return url + word + "?key=" + key

def lookup(word):
    url = geturl(word)
    r = requests.get(url)
    return r

#TODO: parse xml. Should be pretty simple to check whether a string is a word
