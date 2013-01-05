from django.core.management.base import BaseCommand, CommandError
from BeautifulSoup import BeautifulSoup
from viddypull.models import Viddy
import urllib2
import datetime
import json
import pprint
import requests
import time

class Command(BaseCommand):
    help = 'Update Viddys'
    def handle(self, *args, **options):

        payload = {
            'access_token':'BVlXEefJbY-LVkDSnD2lI7398Q2a_Dn2AluKehCLAYyNXPHWUy0xCZjZOPacsG8Xa4ojjnXJuTQ3GbJVwQaEzDNBQKfVj6hdHA_2G_vcQ4RscYdhhxv19e_2f8N99wy-JM0uI4f1FfLxEsaqRBsE2SSAkQLLaHqp7ILlmyQ07z1hiAn_fRRHg3q7CRYFl3PM0',
            'apikey':'exvusk5yqyaymvqyt6zvv3fc'
        }

        viddy = Viddy.objects.all()
        for v in viddy:
            time.sleep(.5)
            popular = requests.get("http://api.viddy.com/v1/media/%s" % v.video_id, params=payload)
            try:
                jsonpopular = json.loads(popular.text)
                try:
                    v.comment_count = jsonpopular['medias'][0]['comment_count']
                    v.like_count = jsonpopular['medias'][0]['like_count']
                    v.save()
                    print 'SAVED - comment count {0} - {1}'.format(jsonpopular['medias'][0]['comment_count'],
                                              unicode(jsonpopular['medias'][0]['title']).encode("utf-8"))
                except KeyError, e:
                    print "{0} is throwing KeyError.".format(v.title)
            except ValueError:
                pass
    #        pprint.pprint(popular.text)
    #        pprint.pprint(jsonpopular)


        print 'Updated all viddys'













    