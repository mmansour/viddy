from viddypull.models import *
from django.contrib import admin
from mezzanine.core.admin import DisplayableAdmin

class ViddyTagInline(admin.TabularInline):
    model = Tag

class ViddyAdmin(DisplayableAdmin):

    fieldsets = [
        ("Title",                       {'fields': ['title']}),
        ("Published Date",              {'fields': ['publish_date']}),
        ("Published Status",            {'fields': ['status']}),
        ("Viddy",            {'fields': ['comment_count', 'like_count', 'video_id', 'video_source', 'thumbnail', 'size', 'video_description',
                                         'viddy_user', 'viddy_user_id', 'viddy_user_thumbnail', 'viddy_user_profile']}),
    ]

    inlines = [
        ViddyTagInline,
    ]


    list_display = ('title', 'comment_count', 'like_count', 'viddy_user', 'status')
#    list_display_links = ('user',)
#    list_editable = ('is_order_closed',)
#    list_filter = ['order_submission_status','is_order_closed', 'publish_date',]
    search_fields = ['title',]
    date_hierarchy = 'publish_date'

admin.site.register(Viddy, ViddyAdmin)