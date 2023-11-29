from django.contrib import admin
from .models import organizationInfo

class organizationInfoAdmin(admin.ModelAdmin):
   list_display = ["orgName", "orgEmail", "adminName", "adminEmail"]
   list_filter = ["orgName"]
   search_fields = ["orgName", "orgEmail"]


# Register your models here.
admin.site.register(organizationInfo, organizationInfoAdmin)