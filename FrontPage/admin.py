from django.contrib import admin
from models import ReleaseVersion

# Register your models here.

class ReleaseAdmin(admin.ModelAdmin):
    list_display = ('mod','version','lastOnLineDate','project','remark')


admin.site.register(ReleaseVersion,ReleaseAdmin)