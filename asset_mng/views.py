from django.contrib.auth import logout,authenticate
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
#from django.contrib.auth.decorators import login_required
from . models import UserDetails,Asset_Table,AssetOwner_Privilege,Department,Employee,LocTable,Category
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import csv
#import json


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


def user_list(request):
    users=UserDetails.objects.all()
    departments = Department.objects.all()
    locations=LocTable.objects.all()
    return render(request,'asset_mng/user.html',{'users':users,'departments': departments,'locations':locations})

def save_user(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        phone_no = request.POST.get('phone_no')
        email = request.POST.get('email') 
        location = request.POST.get('location')
        department = request.POST.get('department')
        status = request.POST.get('status')
        role = request.POST.get('role')
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        
        new_user = UserDetails(
            name=name,
            phone_no=phone_no,
            email=email,
            location=location,
            department=department,
            status=status,
            role=role,
            username=username,
            password=password
        )
        new_user.save()
        users = UserDetails.objects.all().order_by('id')
        for index, use in enumerate (users,start=1):
            UserDetails.objects.filter(pk=use.pk).update(sl_num= index)


        return redirect('user_list')  

    return render(request, 'user.html') 

def edit_user(request,user_id):
    if request.method == 'POST':
        user_id = request.POST.get('id')
        user = get_object_or_404(UserDetails, pk=user_id)
        user.name = request.POST.get('name')
        user.phone_no = request.POST.get('phone_no')
        user.email = request.POST.get('email')
        user.location = request.POST.get('location')
        user.department = request.POST.get('department')
        user.status = request.POST.get('status')
        user.role = request.POST.get('role')
        user.username = request.POST.get('username')
        user.password = request.POST.get('password')
        user.save()
        messages.success(request, 'User updated successfully.')
        return redirect('user_list')  # Redirect to user list page
    else:
        return redirect('user_list')  # Redirect if not a POST request    

def delete_user(request, user_id):
    user = get_object_or_404(UserDetails, id=user_id)
    if request.method == 'POST':
       
        user.delete()
        users = UserDetails.objects.all().order_by('id')
        for index, use in enumerate (users,start=1):
            UserDetails.objects.filter(pk=use.pk).update(sl_num= index)


        return redirect('user_list')  
    
    return redirect('user_list')

def department_list(request):
    departments = Department.objects.all()
    return render(request, 'asset_mng/department_list.html', {'departments': departments})

def edit_department(request,department_id):
    if request.method == 'POST':
        department_id = request.POST.get('id')
        department = get_object_or_404(Department, id=department_id)
        department.department = request.POST.get('department')
        department.location = request.POST.get('location')
        department.status = request.POST.get('status')
        
        department.save()
        messages.success(request, 'Department updated successfully.')
        return redirect('department')  # Redirect to user list page
    else:
        return redirect('department')  # Redirect if not a POST request 

def delete_department(request, department_id):
    department = get_object_or_404(Department, pk=department_id)
    
    if request.method == 'POST':
        department.delete()       
        
        # Update sl_num for remaining departments
        departments = Department.objects.all().order_by('id')
        for index, dept in enumerate(departments, start=1):
            Department.objects.filter(pk=dept.pk).update(sl_num=index)

        messages.success(request, 'Department deleted successfully.')
        return redirect('department')  # Replace 'department_list' with your actual URL name
    
    # Handle GET request if needed (typically to show confirmation or handle errors)
    return redirect('department')  # Redirect to a relevant page

def add_department(request):
    if request.method == 'POST':
        department_name = request.POST.get('department')
        location = request.POST.get('location')
        status = request.POST.get('status')  

        new_department = Department(
            department=department_name,
            location=location,
            status=status
        )
        new_department.save()

        departments = Department.objects.all().order_by('id')
        for index, dept in enumerate(departments, start=1):
            Department.objects.filter(pk=dept.pk).update(sl_num=index)

        return redirect('department')

    return render(request, 'asset_mng/department_list.html')


def location_list(request):
    users=LocTable.objects.all()
    return render(request,'asset_mng/location_pro.html',{'users':users})


def add_location(request):
    if request.method == 'POST':
        location = request.POST.get('location')
        loc_status = request.POST.get('loc_status')
        
        location_loc = LocTable(
            location=location,
            loc_status=loc_status,
        )
        location_loc.save()

        locations=LocTable.objects.all().order_by('id')
        for index, loc in enumerate(locations,start=1):
            LocTable.objects.filter(pk=loc.pk).update(sl_num=index)
            
        return redirect('location_list') 
      
    return render(request, 'asset_mng/location_pro.html')

def delete_loc(request, location_id):
    user = get_object_or_404(LocTable, id=location_id)
    if request.method == 'POST':
        user.delete()

        locations=LocTable.objects.all().order_by('id')
        for index, loc in enumerate(locations,start=1):
            LocTable.objects.filter(pk=loc.pk).update(sl_num=index)

        messages.success(request, 'location deleted successfully.')
        return redirect('location_list')
    else:
        messages.error(request, 'Invalid request method.')
        return redirect('location_list')


def edit_location(request,location_id):
    if request.method == 'POST':
        
        print(request.POST)
        location = get_object_or_404(LocTable, pk=location_id)
        location.location = request.POST.get('location')
        loc_status = request.POST.get('loc_status')

        if loc_status:
            location.loc_status = loc_status
        else:
            messages.error(request, 'Location status is required.')
            return redirect('location_list')

        location.save()
        messages.success(request, 'location updated successfully.')
        return redirect('location_list')
    
    return redirect('location_list')


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'asset_mng/category.html', {'categories': categories})


def save_category(request):
    if request.method == 'POST':
        category_type = request.POST.get('type')
        status = request.POST.get('status')

        
        if category_type and status:
            new_category = Category(
                Category_type=category_type,
                Status=status
            )
            new_category.save()

            categories = Category.objects.all().order_by('id')
            for index, categ in enumerate(categories,start=1):
                Category.objects.filter(pk=categ.pk).update(sl_num = index)

        return redirect('category_list')

    return render(request, 'asset_mng/category.html')


def delete_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == 'POST':
        category.delete()
        categories = Category.objects.all().order_by('id')
        for index, categ in enumerate(categories,start=1):
         Category.objects.filter(pk=categ.pk).update(sl_num = index)
        return redirect('category_list')
    else:
        return render(request, 'error.html', {'error_message': 'Invalid request method.'})

def edit_category(request,category_id):
    if request.method == 'POST':
        
        category = get_object_or_404(Category, pk=category_id)
        category.Category_type = request.POST.get('type')
        category.Status = request.POST.get('status')

        category.save()
        messages.success(request, 'Category updated successfully.')
        return redirect('category_list')
    
    return redirect('category_list')



def employee(request):
    employees = Employee.objects.all()
    return render(request, 'asset_mng/employee.html', {'employees': employees})

def delete_employee(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    
    if request.method == 'POST':
        employee.delete()

        employees=Employee.objects.all().order_by('id')
        for index, emp in enumerate(employees,start=1):
            Employee.objects.filter(pk=emp.pk).update(sl_num=index)

        messages.success(request,'Employee deleted successfully.')
        return redirect('employee')  # Replace 'department_list' with your actual URL name
    
    # Handle GET request if needed (typically to show confirmation or handle errors)
    return redirect('employee') 


def edit_employee(request,employee_id):
    if request.method == 'POST':
        employee_id = request.POST.get('id')
        employee = get_object_or_404(Employee, id=employee_id)
        employee.employee_name = request.POST.get('employee_name')
        employee.phone_no = request.POST.get('phone_no')
        employee.email = request.POST.get('email')
        employee.location = request.POST.get('location')
        employee.department = request.POST.get('department')
        employee.status = request.POST.get('status')
        
        employee.save()
        messages.success(request, 'Employee updated successfully.')
        return redirect('employee')  # Redirect to employee list page
    else:
        return redirect('employee')  # Redirect if not a POST request


def add_employee(request):
    if request.method == 'POST':
        employee_name = request.POST.get('employee_name')
        phone_no = request.POST.get('phone_no')
        email = request.POST.get('email')
        location = request.POST.get('location')
        department = request.POST.get('department')
        status = request.POST.get('status')
        

        # Create a new Employee object and save it to the database
        new_employee = Employee(
            employee_name=employee_name,
            phone_no=phone_no,
            email=email,
            location=location,
            department=department,
            status=status
        )
        new_employee.save()

        employees=Employee.objects.all().order_by('id')
        for index, emp in enumerate(employees,start=1):
            Employee.objects.filter(pk=emp.pk).update(sl_num=index)

        messages.success(request, 'Employee added successfully.')
        return redirect('employee')  # Redirect to employee list page

    return render(request, 'asset_mng/employee_list.html')  # Adjust the template name as necessary


def reports_view(request):
    context = {
        'tables': ['UserTable', 'Department'],
        'data': None,
        'selected_table': None,
    }
    
    if request.method == 'POST':
        selected_table = request.POST.get('table')
        if selected_table == 'UserDetails':
            context['data'] = UserDetails.objects.all()
            context['selected_table'] = 'UserTable'
        elif selected_table == 'Department':
            context['data'] = Department.objects.all()
            context['selected_table'] = 'Department'
        
        if 'export' in request.POST:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = f'attachment; filename="{selected_table}.csv"'
            
            writer = csv.writer(response)
            if selected_table == 'UserDetails':
                writer.writerow(['Name', 'Phone No', 'Email', 'Location', 'Department', 'Status', 'Role', 'Username', 'Password'])
                for user in context['data']:
                    writer.writerow([user.name, user.phone_no, user.email, user.location, user.department, user.status, user.role])
            elif selected_table == 'Department':
                writer.writerow(['Department', 'Location', 'Status'])
                for department in context['data']:
                    writer.writerow([department.department, department.location, department.status])
            return response

    return render(request, 'asset_mng/reports.html', context)


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

@csrf_exempt
def privilege_asset_owner(request):
    username = request.session.get('username', None)
    if not username:
        return redirect('asset_login')
    
    user = UserDetails.objects.get(username=username)
    
    if request.method == 'POST':
        add_asset = request.POST.get('add_asset') == 'on'
        view_asset = request.POST.get('view_asset') == 'on'
        edit_asset = request.POST.get('edit_asset') == 'on'
        delete_asset = request.POST.get('delete_asset') == 'on'
        AssetOwner_Privilege.objects.all().update(add_asset=add_asset, view_asset = view_asset, edit_asset = edit_asset, delete_asset = delete_asset)
        return redirect('privilege_asset_owner')
    
    # Check if any asset owner has add_asset set to True to set the checkbox state
    any_add_asset = AssetOwner_Privilege.objects.filter(add_asset=True).exists()
    any_view_asset = AssetOwner_Privilege.objects.filter(view_asset = True).exists()
    any_edit_asset = AssetOwner_Privilege.objects.filter(edit_asset = True).exists()
    any_delete_asset = AssetOwner_Privilege.objects.filter(delete_asset=True).exists()

    return render(request, 'asset_mng/privilege_asset_owner.html', {
        'username': username,
        'add_asset': any_add_asset,
        'view_asset': any_view_asset,
        'edit_asset': any_edit_asset,
        'delete_asset': any_delete_asset
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


