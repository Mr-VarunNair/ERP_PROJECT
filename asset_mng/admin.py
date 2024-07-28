from django.contrib import admin
from . models import UserDetails
from . models import UserDetails,Asset_Table,AssetOwner_Privilege,Department,Employee,LocTable,Category,CISO_Privilege,Head_Privilege
from . models import AssetOwner_Privilege


admin.site.site_header = 'ERP' 


class AssetDetails(admin.ModelAdmin):               #to display asset datails as a list , passed the value
    list_display = ('Asset_name','Assigned_To')
class AssetPrivilege(admin.ModelAdmin):
    list_display = ('id','user')    

admin.site.register(UserDetails)
admin.site.register(Asset_Table,AssetDetails)
admin.site.register(LocTable)
admin.site.register(Category)
admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(AssetOwner_Privilege,AssetPrivilege)
admin.site.register(CISO_Privilege)
admin.site.register(Head_Privilege)




