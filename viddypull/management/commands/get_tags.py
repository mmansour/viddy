from django.core.management.base import BaseCommand, CommandError
from BeautifulSoup import BeautifulSoup
from viddypull.models import Viddy, Tag
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

#        tags = requests.get("http://api.viddy.com/v1/media/145ca9d7-2c9f-4a02-be3e-fdc195df7a9c/tags", params=payload)
#        jsontags = json.loads(tags.text)
##        pprint.pprint(jsontags.text)
#        pprint.pprint(jsontags)
#
#        for count, item in enumerate(jsontags['media_tags']):
#
#            print 'Content - {0} Media id {1}'.format(jsontags['media_tags'][count]['content'], jsontags['media_tags'][count]['media_id'])

        viddy = Viddy.objects.all()
        for v in viddy:
            time.sleep(.5)
            tags = requests.get("http://api.viddy.com/v1/media/{0}/tags".format(v.video_id), params=payload)
            jsontags = json.loads(tags.text)
            try:
                tag = Tag.objects.get(media_id=v.video_id)
            except Tag.DoesNotExist:
                for count, item in enumerate(jsontags['media_tags']):
                    tag = Tag(viddy=v, tag=jsontags['media_tags'][count]['content'], media_id=jsontags['media_tags'][count]['media_id'], tag_id=jsontags['media_tags'][count]['tag_id'])
                    tag.save()
                    print 'Saved Tag - {0} Media id {1}'.format(jsontags['media_tags'][count]['content'], jsontags['media_tags'][count]['media_id'])

        print 'Got all tags'

#            tags = requests.get("http://api.viddy.com/v1/media/%s/tags" % v.video_id, params=payload)
#            jsontags = json.loads(tags.text)
#    #        pprint.pprint(jsontags.text)
#    #        pprint.pprint(jsontags)
#            v.comment_count = jsonpopular['medias'][0]['comment_count']
#            v.like_count = jsonpopular['medias'][0]['like_count']
#            v.save()
#            print 'SAVED - comment count {0} - {1}'.format(jsonpopular['medias'][0]['comment_count'],
#                                                           unicode(jsonpopular['medias'][0]['title']).encode("utf-8"))












      