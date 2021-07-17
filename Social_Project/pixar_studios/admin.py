from django.contrib import admin
from pixar_studios.models import UserInfo, WebSites, DisneyPlusBlogs, TheatricalShorts

# Register your models here.
admin.site.register(UserInfo)
admin.site.register(WebSites)
admin.site.register(DisneyPlusBlogs)
admin.site.register(TheatricalShorts)
