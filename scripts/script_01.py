import json
import glob 
from collections import defaultdict
import geoip2.database

reader = geoip2.database.Reader('C:\\Users\\adm\Documents\\GeoLite2-Country_20240402\\GeoLite2-Country_20240402\\GeoLite2-Country.mmdb')# database localization
class AnalyzerJSON:
    def __init__(self,):
        self.files = glob.glob('cowrie.json.*')
        self.num_day = defaultdict(int)
        self.num_att = defaultdict(int)
        self.num_total = 0
        self.ses_dur = defaultdict(int)
        self.day = 1
        self.geo_loc = defaultdict(int)

    def merge(self):
        total = []
        for file in self.files:
            with open(file) as openfile:
                for line in openfile:
                    total.append(json.loads(line))

        for event in total:
            day = 1
            if event['eventid'] == '/end/':
                day += 1
            if 'cowrie.session.closed' in event['eventid']:
                country = reader.country(event['src_ip']).country.name
                self.num_att[event['src_ip']] += 1
                self.num_day[day] += 1
                self.num_total += 1
                self.ses_dur[round(int(event['duration']))] += 1
                self.geo_loc[country] += 1


    def write(self, filename):
        with open(filename, 'w') as outfile:
            outfile.write("How many times a given address connected to honeypot:\n")
            for ip, count in self.num_att.items():
                outfile.write(f"{ip}: {count}\n")

            outfile.write("\nNumber of events daily:\n")
            for day, num in self.num_day.items():
                outfile.write(f"Day {day}: {num}\n")

            outfile.write("\nSession durations:\n")
            for duration, count in self.ses_dur.items():
                outfile.write(f"{duration} sec. : {count}\n")

            outfile.write("\nGeolocalizacion ip address:\n")
            for place, count in self.geo_loc.items():
                outfile.write(f"{place} : {count}\n")

            outfile.write(f"\nNumber of all events: {self.num_total}\n")




analyzer = AnalyzerJSON()
analyzer.merge()
analyzer.write('resoults.txt')




