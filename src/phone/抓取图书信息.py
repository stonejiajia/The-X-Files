import urllib2
import json
dota = urllib2.urlopen(r'https://api.douban.com/v2/book/1220562')
json = json.loads(dota.read())
print json['rating']
print json['images']['large']
print json['summary']
