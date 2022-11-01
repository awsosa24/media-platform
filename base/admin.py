from django.contrib import admin
from .models import Channel, Content, ContentFile, ChannelGroup


# Register your models here.
admin.site.register(Channel)

admin.site.register(Content)

admin.site.register(ContentFile)

admin.site.register(ChannelGroup)
