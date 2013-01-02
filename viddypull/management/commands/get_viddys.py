from django.core.management.base import BaseCommand, CommandError
from BeautifulSoup import BeautifulSoup
from viddypull.models import Viddy
import urllib2
import datetime
import json
import pprint
import requests

class Command(BaseCommand):
    help = 'Viddy API Test'
    def handle(self, *args, **options):

        #TAG GETTER URI TO GET TAGS FOR A VIDEO         VIDEO ID BELOW
        #http://api.viddy.com/v1/media/145ca9d7-2c9f-4a02-be3e-fdc195df7a9c/tags?access_token=BVlXEefJbY-LVkDSnD2lI7398Q2a_Dn2AluKehCLAYyNXPHWUy0xCZjZOPacsG8Xa4ojjnXJuTQ3GbJVwQaEzDNBQKfVj6hdHA_2G_vcQ4RscYdhhxv19e_2f8N99wy-JM0uI4f1FfLxEsaqRBsE2SSAkQLLaHqp7ILlmyQ07z1hiAn_fRRHg3q7CRYFl3PM0&apikey=exvusk5yqyaymvqyt6zvv3fc

        #UPDATER: TO GET THE LIKE COUNT FOR A VIDEOS    VIDEO ID BELOW
        #http://api.viddy.com/v1/media/64d48814-4fbf-4b57-9039-000fa1894477?access_token=BVlXEefJbY-LVkDSnD2lI7398Q2a_Dn2AluKehCLAYyNXPHWUy0xCZjZOPacsG8Xa4ojjnXJuTQ3GbJVwQaEzDNBQKfVj6hdHA_2G_vcQ4RscYdhhxv19e_2f8N99wy-JM0uI4f1FfLxEsaqRBsE2SSAkQLLaHqp7ILlmyQ07z1hiAn_fRRHg3q7CRYFl3PM0&apikey=exvusk5yqyaymvqyt6zvv3fc

        payload = {
            'access_token':'BVlXEefJbY-LVkDSnD2lI7398Q2a_Dn2AluKehCLAYyNXPHWUy0xCZjZOPacsG8Xa4ojjnXJuTQ3GbJVwQaEzDNBQKfVj6hdHA_2G_vcQ4RscYdhhxv19e_2f8N99wy-JM0uI4f1FfLxEsaqRBsE2SSAkQLLaHqp7ILlmyQ07z1hiAn_fRRHg3q7CRYFl3PM0',
            'apikey':'exvusk5yqyaymvqyt6zvv3fc'
        }

        popular = requests.get("http://api.viddy.com/v1/media/popular", params=payload)
        jsonpopular = json.loads(popular.text)
#        pprint.pprint(popular.text)
#        pprint.pprint(jsonpopular['medias'][0]['comment_count'])

        for count, item in enumerate(jsonpopular['medias']):

            datestring = jsonpopular['medias'][count]['unix_timestamp']
            dt = datetime.datetime.fromtimestamp(float(datestring))

            try:
                vid = Viddy.objects.get(video_id=jsonpopular['medias'][count]['id'])
                vid.comment_count = jsonpopular['medias'][count]['comment_count']
                vid.like_count = jsonpopular['medias'][count]['like_count']
                vid.save()
                print 'already got it'
            except Viddy.DoesNotExist, e:
                print 'missing viddy'
                vid = Viddy(
                    title = jsonpopular['medias'][count]['title'],
                    comment_count = jsonpopular['medias'][count]['comment_count'],
                    publish_date = dt,
                    thumbnail = jsonpopular['medias'][count]['thumbnail']['url'],
                    like_count = jsonpopular['medias'][count]['like_count'],
                    video_id = jsonpopular['medias'][count]['id'],
                    video_source = jsonpopular['medias'][count]['source'],
                    video_description = jsonpopular['medias'][count]['description'],
                    viddy_user = jsonpopular['medias'][count]['user']['username'],
                    viddy_user_id = jsonpopular['medias'][count]['user']['id'],
                    viddy_user_profile = jsonpopular['medias'][count]['user']['profile'],
                    viddy_user_thumbnail = jsonpopular['medias'][count]['user']['thumbnail']['url'],
                )
                vid.save()

        print 'Got all viddys for today'








        


  