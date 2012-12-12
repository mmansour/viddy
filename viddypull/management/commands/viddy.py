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

        #URI TO GET TAGS FOR A VIDEO                Video ID Below
        #http://api.viddy.com/v1/media/145ca9d7-2c9f-4a02-be3e-fdc195df7a9c/tags?access_token=BVlXEefJbY-LVkDSnD2lI7398Q2a_Dn2AluKehCLAYyNXPHWUy0xCZjZOPacsG8Xa4ojjnXJuTQ3GbJVwQaEzDNBQKfVj6hdHA_2G_vcQ4RscYdhhxv19e_2f8N99wy-JM0uI4f1FfLxEsaqRBsE2SSAkQLLaHqp7ILlmyQ07z1hiAn_fRRHg3q7CRYFl3PM0&apikey=exvusk5yqyaymvqyt6zvv3fc


        payload = {
            'access_token':'BVlXEefJbY-LVkDSnD2lI7398Q2a_Dn2AluKehCLAYyNXPHWUy0xCZjZOPacsG8Xa4ojjnXJuTQ3GbJVwQaEzDNBQKfVj6hdHA_2G_vcQ4RscYdhhxv19e_2f8N99wy-JM0uI4f1FfLxEsaqRBsE2SSAkQLLaHqp7ILlmyQ07z1hiAn_fRRHg3q7CRYFl3PM0',
            'apikey':'exvusk5yqyaymvqyt6zvv3fc'
        }
        popular = requests.get("http://api.viddy.com/v1/media/popular", params=payload)

#        pprint.pprint(popular.text)
        jsonpopular = json.loads(popular.text)
#        pprint.pprint(jsonpopular['medias'][0]['comment_count'])

        for count, item in enumerate(jsonpopular['medias']):

            #CONVERT UNIX TIMESTAMP TO HUMAN DATETIME
            datestring = jsonpopular['medias'][count]['unix_timestamp']
            dt = datetime.datetime.fromtimestamp(float(datestring))
            
            print "formatted Date: {0}".format(dt)
            print 'comment count %s' % jsonpopular['medias'][count]['comment_count']
            print 'like count %s' % jsonpopular['medias'][count]['like_count']
            print 'video id %s' % jsonpopular['medias'][count]['id']
            print 'description %s' % jsonpopular['medias'][count]['description']
            print 'location %s' % jsonpopular['medias'][count]['location']
            print 'video source %s' % jsonpopular['medias'][count]['source']
            print 'tag count %s' % jsonpopular['medias'][count]['tag_count']
            print 'thumbnail %s' % jsonpopular['medias'][count]['thumbnail']
            print 'user %s' % jsonpopular['medias'][count]['user']








        


  