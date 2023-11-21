from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Tag)




#admin video mixin for video embeds:
from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from .models import Item

class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Item, MyModelAdmin)