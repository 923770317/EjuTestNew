from django.contrib import admin
from models import *

# Register your models here.

class ReleaseAdmin(admin.ModelAdmin):
    list_display = ('mod','version','lastOnLineDate','project','remark')

class ProductSiteAdmin(admin.ModelAdmin):
    list_display = ('modeleNmae','g4Address','g5Address','port')
    search_fields = ['modeleNmae']



admin.site.register(ReleaseVersion,ReleaseAdmin)
admin.site.register(ProdectSiste,ProductSiteAdmin)