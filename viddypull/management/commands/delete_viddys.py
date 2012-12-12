from django.core.management.base import BaseCommand, CommandError
from viddypull.models import Viddy

class Command(BaseCommand):
    help = 'Delete Viddys'
    def handle(self, *args, **options):

        viddy = Viddy.objects.all()
        for v in viddy:
            v.delete()
        print 'Deleted all Viddys'













