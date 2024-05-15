import http.client
import json
import pandas

#Free data one
#connection = http.client.HTTPConnection('api.football-data.org')
#headers = { 'X-Auth-Token': 'bf0a4045ba524fe883bedd2062bed8b4' }
#connection.request('GET', '/v2/matches', None, headers )
#response = json.loads(connection.getresponse().read().decode())

#print (response)

#Football-API
conn = http.client.HTTPSConnection("v3.football.api-sports.io")

headers = {
    'x-rapidapi-host': "v3.football.api-sports.io",
    'x-rapidapi-key': "4785325c3dc544ee1c1da8c690049dbe"
    }

conn.request("GET", "/leagues?country=australia", headers=headers)

res = conn.getresponse()
data = res.read()
print(type(data))

dataLoad = json.loads(data.decode("utf-8"))

listdata = dataLoad.get("response")

df = pandas.DataFrame()

df.to_csv('leagues.csv')
