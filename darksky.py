import urllib2, urllib, json, config
url = "https://api.darksky.net/forecast/" + config.DARKSKY_CONFIG["apiKey"] + "/32.8927401,-79.9956252"

def getWeather():
    result = urllib2.urlopen(url).read()
    data = json.loads(result)
    return data