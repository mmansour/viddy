from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

from mezzanine.core.views import direct_to_template

urlpatterns = patterns('viddypull.views',
    url("^$", "home", name="home"),
    url("^details/(?P<viddy_id>\d+)/$", "viddy_details", name="viddy_details"),
    url("^tag/(?P<tag_id>[\w-]+)/$", "viddys_by_tag", name="viddys_by_tag"),
)