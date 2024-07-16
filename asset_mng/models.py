from django.db import models
from django.contrib.auth.models import User


class UserDetails(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)  # Ideally, this should be hashed
    role = models.CharField(max_length=45)

    def __str__(self):
        return self.username
    


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
    
class UserPreference(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    show_assets = models.BooleanField(default=True)    

class AssetOwner_Privilege(models.Model):
    user = models.ForeignKey(UserDetails, on_delete=models.CASCADE)
    add_asset = models.BooleanField(default=False)
