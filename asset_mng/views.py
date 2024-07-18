from django.contrib.auth import login,logout,authenticate
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . models import UserDetails,Asset_Table,AssetOwner_Privilege
#from django . http import JsonResponse
#from .models import UserPreference
from django.views.decorators.csrf import csrf_exempt
import json


# Create your views here.
def home(request):
    return render(request,'home.html')
def prpty_mng(request):       
    return render(request,'prpty_mng.html')
def amc_mng(request):
    return render(request,'amc_mng.html')
def store_mng(request):
    return render(request,'store_mng.html')
def rem_schedule(request):
    return render(request,'rem_schedule.html')
def vehicle_mng(request):
    return render(request,'vehicle_mng.html')
def build_mnt(request):
    return render(request,'build_mnt.html')
def iso_mng(request):
    return render(request,'iso_mng.html')
def house_mng(request):
    return render(request,'house_mng.html')
def purchase_mng(request):
    return render(request,'purchase_mng.html')
def tax_building(request):
    return render(request,'tax_building.html')
def tenant_mng(request):
    return render(request,'tenant_mng.html')

def admin_dashboard(request):
    username =request.session.get('username',None)
    if not username:
        return redirect('asset_login')
    return render(request, 'asset_mng/admin_dashboard.html',{'username':username})
def head_dashboard(request):
    return render(request,'asset_mng/head.html')

def ciso_dashboard(request):
    return render(request,'asset_mng/ciso.html')

def asset_owner_dashboard(request):
    username = request.session.get('username',None)
    user_role = request.session.get('role',None)

    if not username:
        return redirect('asset_login')
    return render(request, 'asset_mng/asset_owner.html',{'username':username,'user_role':user_role})


def asset_login(request):
    if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request,username=username,password=password)
            try:
                user = UserDetails.objects.get(username=username, password=password)
                if user is not None:
                    request.session['username'] = user.username
                    request.session['role'] = user.role     #pass the user's role to the template
                    print(f"Session Data: {request.session['username']}, {request.session['role']}")  # Debugging statement
                    if user.role == 'admin':
                        return redirect('admin_dashboard')
                    elif user.role == 'head':
                        return redirect('head_dashboard')
                    elif user.role == 'asset_owner':
                        return redirect('asset_owner_dashboard')
                    elif user.role == 'ciso':
                        return redirect('ciso_dashboard')
                    else:
                        messages.error(request, 'Unknown user role')
                else:
                    messages.error(request, 'Invalid username or password')
            except UserDetails.DoesNotExist:
                messages.error(request, 'Invalid username or password')
    
    return render(request, 'asset_mng/asset_mng.html')


def roles(request):
    return render(request,'asset_mng/roles.html')


def privileges(request):
    username =request.session.get('username',None)
    if not username:
        return redirect('asset_login')
    return render(request,'asset_mng/privileges.html',{'username':username})

def privilege_admin(request):
    username =request.session.get('username',None)
    if not username:
        return redirect('asset_login')
    return render(request,'asset_mng/privilege_admin.html',{'username':username})

def privilege_ciso(request):
    username =request.session.get('username',None)
    if not username:
        return redirect('asset_login')
    return render(request,'asset_mng/privilege_ciso.html',{'username':username})


def privilege_head(request):
    username =request.session.get('username',None)
    if not username:
        return redirect('asset_login')
    return render(request,'asset_mng/privilege_head.html',{'username':username})
'''
@csrf_exempt
def privilege_asset_owner(request):
    username =request.session.get('username',None)
    if not username:
        return redirect('asset_login')
    user = UserDetails.objects.get(username = username)
    asset_owner, created = AssetOwner_Privilege.objects.get_or_create(user=user)
    if request.method == 'POST':
        add_asset = request.POST.get('add_asset') == 'on'
        asset_owner.add_asset = add_asset
        asset_owner.save()

        return redirect('privilege_asset_owner')

    return render(request, 'asset_mng/privilege_asset_owner.html', {
        'username': username,
        'add_asset': asset_owner.add_asset,
    })
'''
@csrf_exempt
def privilege_asset_owner(request):
    username = request.session.get('username', None)
    if not username:
        return redirect('asset_login')
    
    user = UserDetails.objects.get(username=username)
    
    if request.method == 'POST':
        add_asset = request.POST.get('add_asset') == 'on'
        AssetOwner_Privilege.objects.all().update(add_asset=add_asset)
        return redirect('privilege_asset_owner')
    
    # Check if any asset owner has add_asset set to True to set the checkbox state
    any_add_asset = AssetOwner_Privilege.objects.filter(add_asset=True).exists()

    return render(request, 'asset_mng/privilege_asset_owner.html', {
        'username': username,
        'add_asset': any_add_asset,
    })


def asset_list(request):
    users = Asset_Table.objects.all()
    user_role = request.session.get('role',None)
    add_asset = False                    # Default value for add_asset privilege

    if user_role == 'asset_owner':      # Check if the logged-in user is an asset owner
        username = request.session.get('username',None)
        if username:
            try:
                user = UserDetails.objects.get(username=username)
                #print(f"User found: {user}")  # Debugging statement
                privilege = AssetOwner_Privilege.objects.get(user=user)
                add_asset = privilege.add_asset
                #print(f"Privilege found: {privilege}, add_asset: {add_asset}")  # Debugging statement
            except UserDetails.DoesNotExist:
                print(f"UserDetails.DoesNotExist: {username}")
            except AssetOwner_Privilege.DoesNotExist:
                print(f"AssetOwner_Privilege.DoesNotExist for user: {user}")
    #print(f"user_role = {user_role}, add_asset = {add_asset}")  # Debugging statement
    return render(request, 'asset_mng/asset_pro.html', {
        'users': users,'user_role':user_role,'add_asset':add_asset,
    })


def add_asset(request):
    if request.method == 'POST':
        asset_type = request.POST.get('Asset_type')
        asset_name = request.POST.get('Asset_name')
        serial_number = request.POST.get('Serial_number')
        model_number = request.POST.get('Model_number')
        item_code = request.POST.get('Item_code')
        assigned_to = request.POST.get('Assigned_To')
        machine_os_configuration = request.POST.get('Machine_OS_configuration')
        movable_nonmovable = request.POST.get('Movable_nonmovable')
        status = request.POST.get('Status')
        vender_supplier = request.POST.get('Vender_Supplier')
        maintenance = request.POST.get('Maintenance')
        price = request.POST.get('price')
        year_of_purchasing = request.POST.get('Year_of_purchasing')
        year_of_expiry = request.POST.get('Year_of_expiry')
        age_life = request.POST.get('Age_life')
        supporting_docs = request.FILES.get('Supporting_docs')
        images = request.FILES.get('images')
        notes = request.POST.get('Notes')

        asset = Asset_Table(
            Asset_name=asset_name,
            Asset_type=asset_type,
            Serial_number=serial_number,
            Model_number=model_number,
            Item_code=item_code,
            Assigned_To = assigned_to,
            Machine_OS_configuration=machine_os_configuration,
            Movable_nonmovable=movable_nonmovable,
            Status=status,
            Vender_Supplier=vender_supplier,
            Maintenance=maintenance,
            price=price,
            Year_of_purchasing=year_of_purchasing,
            Year_of_expiry=year_of_expiry,
            Age_life=age_life,
            Supporting_docs=supporting_docs,
            images=images,
            Notes=notes
        )
        asset.save()
        assets = Asset_Table.objects.all().order_by('id')
        for index, asset in enumerate(assets, start=1):
            Asset_Table.objects.filter(pk=asset.pk).update(sl_num=index)
        return redirect('asset_list')

    return render(request, 'asset_mng/add_asset.html')


def delete_asset(request, user_id):
    user = get_object_or_404(Asset_Table, id=user_id)
    if request.method == 'POST':
        user.delete()

        assets = Asset_Table.objects.all().order_by('id')
        for index, asset in enumerate(assets, start=1):
            Asset_Table.objects.filter(pk=asset.pk).update(sl_num=index)

        messages.success(request, 'Asset deleted successfully.')
        return redirect('asset_list')
    else:
        messages.error(request, 'Invalid request method.')
        return redirect('asset_list')
    
def view_asset(request, user_id):
    asset = get_object_or_404(Asset_Table, id=user_id)
    return render(request, 'asset_mng/view_asset.html', {'asset': asset})    


def edit_asset(request,asset_id):
    asset = get_object_or_404(Asset_Table, pk=asset_id)
    if request.method == 'POST':
        asset.Asset_type = request.POST.get('Asset_type')
        asset.Asset_name = request.POST.get('Asset_name')
        asset.Serial_number = request.POST.get('Serial_number')
        asset.Model_number = request.POST.get('Model_number')
        asset.Item_code = request.POST.get('Item_code')
        asset.Machine_OS_configuration = request.POST.get('Machine_OS_configuration')
        asset.Movable_nonmovable = request.POST.get('Movable_nonmovable')
        asset.Status = request.POST.get('Status')
        asset.Vender_Supplier = request.POST.get('Vender_Supplier')
        asset.Maintenance = request.POST.get('Maintenance')
        asset.price = request.POST.get('price')
        asset.Year_of_purchasing = request.POST.get('Year_of_purchasing')
        asset.Year_of_expiry = request.POST.get('Year_of_expiry')
        asset.Age_life = request.POST.get('Age_life')
        asset.Supporting_docs = request.FILES.get('Supporting_docs')
        asset.images = request.FILES.get('images')
        asset.Notes = request.POST.get('Notes')
        asset.save()
        messages.success(request, 'Asset updated successfully.')
        return redirect('asset_list')  # Redirect to user list page
    else:
        asset.Year_of_purchasing = asset.Year_of_purchasing.strftime('%Y-%m-%d')
        asset.Year_of_expiry = asset.Year_of_expiry.strftime('%Y-%m-%d')
        return redirect('asset_list')    



def logout_view(request):
    logout(request)
    return redirect('asset_login')


