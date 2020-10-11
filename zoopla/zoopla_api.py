import json
import urllib.request

from resources import api_keys

zoopla_key = api_keys.ZOOPLA_API_KEY

if __name__ == "__main__":
    location = "London"
    url = "http://api.zoopla.co.uk/api/v1/property_listings.js?area=" + location + "&api_key=" + zoopla_key
    urlopen = urllib.request.urlopen(url)
    contents = urlopen.read()

    parsed_json = json.loads(contents)
    type(parsed_json)

    print(json.dumps(parsed_json, indent=4, sort_keys=True))
    print(len(parsed_json["listing"]))
