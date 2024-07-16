from django.contrib import admin
from . models import UserDetails
from . models import Asset_Table


admin.site.site_header = 'ERP' 


class AssetDetails(admin.ModelAdmin):               #to display asset datails as a list , passed the value
    list_display = ('Asset_name','Assigned_To')

admin.site.register(UserDetails)
admin.site.register(Asset_Table,AssetDetails)

