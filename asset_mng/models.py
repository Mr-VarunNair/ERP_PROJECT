from django.db import models
from django.contrib.auth.models import User


class UserDetails(models.Model):
    sl_num = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=100)
    email = models.EmailField(unique=True, blank=False, null=False)
    location = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)  # to be hashed
    role = models.CharField(max_length=45)

    def __str__(self):
        return self.username
    
class Department(models.Model):
    sl_num = models.CharField(max_length=100)
    department=models.CharField(max_length=100) 
    location=models.CharField(max_length=100) 
    status=models.CharField(max_length=100) 
   
    def __str__(self):
        return self.department  

class Employee(models.Model):
    sl_num = models.CharField(max_length=100)
    employee_name=models.CharField(max_length=100)
    phone_no=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    department=models.CharField(max_length=100)
    status=models.CharField(max_length=100)      


class Category(models.Model):
    sl_num = models.CharField(max_length=100)
    Category_type=models.CharField(max_length=100)
    Status=models.CharField(max_length=100)

    def __str__(self):
        return self.Category_type    
    

class LocTable(models.Model):
   sl_num=models.CharField(max_length=100)
   location = models.CharField(max_length=100)
   loc_status=models.CharField(max_length=50,default='Active')     

   def __str__(self):
       return self.location
    


class Asset_Table(models.Model):
    sl_num = models.CharField(max_length=100)
    Asset_name = models.CharField(max_length=100)
    Asset_type = models.CharField(max_length=100)
    Status = models.CharField(max_length=100)
    Item_code= models.CharField(max_length=100)
    Assigned_To = models.CharField(max_length=100)
    images=models.ImageField(upload_to=None,blank=True,null=True)
    Serial_number=models.CharField(max_length=100)
    Model_number=models.CharField(max_length=100)
    Machine_OS_configuration=models.CharField(max_length=100)
    Movable_nonmovable=models.CharField(max_length=100)
    Vender_Supplier=models.CharField(max_length=100)
    Maintenance=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    Year_of_purchasing=models.DateField()
    Year_of_expiry=models.DateField()
    Age_life=models.CharField(max_length=100)
    Supporting_docs=models.FileField(upload_to=None, max_length=254,blank=True,null=True)
    Notes=models.TextField(max_length=100)

    def __str__(self):
        return self.Asset_name
    
#class UserPreference(models.Model):
    #user = models.OneToOneField(User, on_delete = models.CASCADE)
    #show_assets = models.BooleanField(default=True)    

class AssetOwner_Privilege(models.Model):
    user = models.ForeignKey(UserDetails, on_delete=models.CASCADE)
    add_asset = models.BooleanField(default=False)
    view_asset = models.BooleanField(default=False)
    edit_asset = models.BooleanField(default=False)
    delete_asset = models.BooleanField(default=False)

    privilege_update = models.BooleanField(default=False)
    report_download = models.BooleanField(default=False)

    add_user = models.BooleanField(default=False)
    view_user = models.BooleanField(default=False)
    edit_user = models.BooleanField(default=False)
    delete_user = models.BooleanField(default=False)

    add_employee = models.BooleanField(default=False)
    view_employee = models.BooleanField(default=False)
    edit_employee = models.BooleanField(default=False)
    delete_employee = models.BooleanField(default=False)

    add_location = models.BooleanField(default=False)
    view_location = models.BooleanField(default=False)
    edit_location = models.BooleanField(default=False)
    delete_location = models.BooleanField(default=False)

    add_department = models.BooleanField(default=False)
    view_department = models.BooleanField(default=False)
    edit_department = models.BooleanField(default=False)
    delete_department = models.BooleanField(default=False)

    add_category = models.BooleanField(default=False)
    view_category = models.BooleanField(default=False)
    edit_category = models.BooleanField(default=False)
    delete_category = models.BooleanField(default=False)

    add_roles = models.BooleanField(default=False)
    view_roles = models.BooleanField(default=False)
    edit_roles = models.BooleanField(default=False)
    delete_roles = models.BooleanField(default=False)

class CISO_Privilege(models.Model):
    user = models.ForeignKey(UserDetails, on_delete=models.CASCADE)
    ciso_add_asset = models.BooleanField(default=False)
    ciso_view_asset = models.BooleanField(default=False)
    ciso_edit_asset = models.BooleanField(default=False)
    ciso_delete_asset = models.BooleanField(default=False)

    ciso_privilege_update = models.BooleanField(default=False)
    ciso_report_download = models.BooleanField(default=False)

    ciso_add_user = models.BooleanField(default=False)
    ciso_view_user = models.BooleanField(default=False)
    ciso_edit_user = models.BooleanField(default=False)
    ciso_delete_user = models.BooleanField(default=False)

    ciso_add_employee = models.BooleanField(default=False)
    ciso_view_employee = models.BooleanField(default=False)
    ciso_edit_employee = models.BooleanField(default=False)
    ciso_delete_employee = models.BooleanField(default=False)

    ciso_add_location = models.BooleanField(default=False)
    ciso_view_location = models.BooleanField(default=False)
    ciso_edit_location = models.BooleanField(default=False)
    ciso_delete_location = models.BooleanField(default=False)

    ciso_add_department = models.BooleanField(default=False)
    ciso_view_department = models.BooleanField(default=False)
    ciso_edit_department = models.BooleanField(default=False)
    ciso_delete_department = models.BooleanField(default=False)

    ciso_add_category = models.BooleanField(default=False)
    ciso_view_category = models.BooleanField(default=False)
    ciso_edit_category = models.BooleanField(default=False)
    ciso_delete_category = models.BooleanField(default=False)

    ciso_add_roles = models.BooleanField(default=False)
    ciso_view_roles = models.BooleanField(default=False)
    ciso_edit_roles = models.BooleanField(default=False)
    ciso_delete_roles = models.BooleanField(default=False)

class Head_Privilege(models.Model):
    user = models.ForeignKey(UserDetails, on_delete=models.CASCADE)
    head_add_asset = models.BooleanField(default=False)
    head_view_asset = models.BooleanField(default=False)
    head_edit_asset = models.BooleanField(default=False)
    head_delete_asset = models.BooleanField(default=False)

    head_privilege_update = models.BooleanField(default=False)
    head_report_download = models.BooleanField(default=False)

    head_add_user = models.BooleanField(default=False)
    head_view_user = models.BooleanField(default=False)
    head_edit_user = models.BooleanField(default=False)
    head_delete_user = models.BooleanField(default=False)

    head_add_employee = models.BooleanField(default=False)
    head_view_employee = models.BooleanField(default=False)
    head_edit_employee = models.BooleanField(default=False)
    head_delete_employee = models.BooleanField(default=False)

    head_add_location = models.BooleanField(default=False)
    head_view_location = models.BooleanField(default=False)
    head_edit_location = models.BooleanField(default=False)
    head_delete_location = models.BooleanField(default=False)

    head_add_department = models.BooleanField(default=False)
    head_view_department = models.BooleanField(default=False)
    head_edit_department = models.BooleanField(default=False)
    head_delete_department = models.BooleanField(default=False)

    head_add_category = models.BooleanField(default=False)
    head_view_category = models.BooleanField(default=False)
    head_edit_category = models.BooleanField(default=False)
    head_delete_category = models.BooleanField(default=False)

    head_add_roles = models.BooleanField(default=False)
    head_view_roles = models.BooleanField(default=False)
    head_edit_roles = models.BooleanField(default=False)
    head_delete_roles = models.BooleanField(default=False)