from django.db import models
from mezzanine.core.models import Displayable, RichTextField
from mezzanine.generic.fields import CommentsField, RatingField
from django.utils.translation import ugettext_lazy as _

class Viddy(Displayable):
#    user = models.ForeignKey(User)
    comment_count = models.IntegerField(blank=True, null=True, verbose_name="Comment Count")
    like_count = models.IntegerField(blank=True, null=True, verbose_name="Like Count")
    video_id = models.CharField(max_length=400, verbose_name="Video ID", blank=True, null=True)
    thumbnail = models.CharField(max_length=400, verbose_name="Thumbnail", blank=True, null=True)
    size = models.CharField(max_length=400, verbose_name="Size", blank=True)
    additional_instructions = models.TextField(verbose_name="Additional Notes", blank=True)
    order_submission_status = models.CharField(max_length=40, verbose_name="Submission Status", blank=True, null=True)
    viddy_user = models.CharField(max_length=200, verbose_name="Viddy Username", blank=True, null=True)
    viddy_user_id = models.CharField(max_length=200, verbose_name="Viddy User ID", blank=True, null=True)
    viddy_user_thumbnail = models.CharField(max_length=200, verbose_name="Viddy User", blank=True, null=True)
    viddy_user_profile = models.CharField(max_length=200, verbose_name="Viddy User Profile", blank=True, null=True)


    def __unicode__(self):
        return self.title
