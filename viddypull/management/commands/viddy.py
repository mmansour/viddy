from django.core.management.base import BaseCommand, CommandError
from BeautifulSoup import BeautifulSoup
import urllib2
import datetime
import json
import pprint
import requests

class Command(BaseCommand):
    help = 'Viddy API Test'
    def handle(self, *args, **options):

        #CONVERT UNIX TIMESTAMP TO HUMAN DATETIME
        datestring = "1277722499.82"
        dt = datetime.datetime.fromtimestamp(float(datestring))
        print "Formatted Date: {0}".format(dt)


        #URI TO GET TAGS FOR A VIDEO                Video ID Below
        #http://api.viddy.com/v1/media/145ca9d7-2c9f-4a02-be3e-fdc195df7a9c/tags?access_token=BVlXEefJbY-LVkDSnD2lI7398Q2a_Dn2AluKehCLAYyNXPHWUy0xCZjZOPacsG8Xa4ojjnXJuTQ3GbJVwQaEzDNBQKfVj6hdHA_2G_vcQ4RscYdhhxv19e_2f8N99wy-JM0uI4f1FfLxEsaqRBsE2SSAkQLLaHqp7ILlmyQ07z1hiAn_fRRHg3q7CRYFl3PM0&apikey=exvusk5yqyaymvqyt6zvv3fc


        payload = {
            'access_token':'BVlXEefJbY-LVkDSnD2lI7398Q2a_Dn2AluKehCLAYyNXPHWUy0xCZjZOPacsG8Xa4ojjnXJuTQ3GbJVwQaEzDNBQKfVj6hdHA_2G_vcQ4RscYdhhxv19e_2f8N99wy-JM0uI4f1FfLxEsaqRBsE2SSAkQLLaHqp7ILlmyQ07z1hiAn_fRRHg3q7CRYFl3PM0',
            'apikey':'exvusk5yqyaymvqyt6zvv3fc'
        }
        popular = requests.get("http://api.viddy.com/v1/media/popular", params=payload)

#        pprint.pprint(popular.text)
        jsonpopular = json.loads(popular.text)
        pprint.pprint(jsonpopular)
        


  