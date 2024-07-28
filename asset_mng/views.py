from django.contrib.auth import logout,authenticate
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
#from django.contrib.auth.decorators import login_required
from . models import UserDetails,Asset_Table,AssetOwner_Privilege,Department,Employee,LocTable,Category,CISO_Privilege,Head_Privilege
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import csv
#import json


# Create your views here.
def home(request):
    return render(request,'home.html')
def prpty_mng(request):       
    return render(request,'prpty_mng.html')

def admin_dashboard(request):
    total_users = UserDetails.objects.count()
    total_assets = Asset_Table.objects.count()
    total_dept=Department.objects.count()
    total_emp=Employee.objects.count()
    username =request.session.get('username',None)
    name = request.session.get('name',None)
    if not username:
        return redirect('asset_login')
    return render(request, 'asset_mng/admin_dashboard.html',{'username':username, 'name':name, 'total_users':total_users,'total_assets':total_assets, 'total_dept': total_dept, 'total_emp': total_emp })
def head_dashboard(request):
    total_users = UserDetails.objects.count()
    total_assets = Asset_Table.objects.count()
    total_dept = Department.objects.count()
    total_emp = Employee.objects.count()
    username = request.session.get('username', None)
    user_role = request.session.get('role', None)
    name = request.session.get('name', None)

    if not username:
        return redirect('asset_login')

    user = UserDetails.objects.get(username=username)
    head_privileges = Head_Privilege.objects.filter(user=user)

    head_privilege_update = head_privileges.filter(head_privilege_update=True).exists()
    head_report_download = head_privileges.filter(head_report_download=True).exists()
    head_view_user = head_privileges.filter(head_view_user=True).exists()
    head_view_employee = head_privileges.filter(head_view_employee=True).exists()
    head_view_location = head_privileges.filter(head_view_location=True).exists()
    head_view_category = head_privileges.filter(head_view_category=True).exists()
    head_view_department = head_privileges.filter(head_view_department=True).exists()
    head_view_roles = head_privileges.filter(head_view_roles=True).exists()

    context = {
        'username': username,
        'user_role': user_role,
        'name': name,
        'head_privilege_update': head_privilege_update,
        'head_report_download': head_report_download,
        'head_view_user': head_view_user,
        'head_view_employee': head_view_employee,
        'head_view_location': head_view_location,
        'head_view_category': head_view_category,
        'head_view_department': head_view_department,
        'head_view_roles':head_view_roles,
        'total_users': total_users,
        'total_assets': total_assets,
        'total_dept': total_dept,
        'total_emp': total_emp,
    }
    return render(request,'asset_mng/head_dashboard.html',context)

def ciso_dashboard(request):
    total_users = UserDetails.objects.count()
    total_assets = Asset_Table.objects.count()
    total_dept=Department.objects.count()
    total_emp=Employee.objects.count()
    username = request.session.get('username',None)
    user_role = request.session.get('role',None)
    name = request.session.get('name',None)

    if not username:
        return redirect('asset_login')
    user = UserDetails.objects.get(username=username)
    ciso_privileges = CISO_Privilege.objects.filter(user=user)

    ciso_privilege_update = ciso_privileges.filter(ciso_privilege_update=True).exists()
    ciso_report_download = ciso_privileges.filter(ciso_report_download=True).exists()
    ciso_view_user = ciso_privileges.filter(ciso_view_user =True).exists()
    ciso_view_employee = ciso_privileges.filter(ciso_view_employee =True).exists()
    ciso_view_location = ciso_privileges.filter(ciso_view_location = True).exists()
    ciso_view_category = ciso_privileges.filter(ciso_view_category = True).exists()
    ciso_view_department = ciso_privileges.filter(ciso_view_department = True).exists()
    ciso_view_roles = ciso_privileges.filter(ciso_view_roles = True).exists()

    context = {
        'username': username,
        'user_role': user_role,
        'name': name,
        'ciso_privilege_update': ciso_privilege_update,
        'ciso_report_download': ciso_report_download,
        'ciso_view_user' : ciso_view_user,
        #'add_user' : add_user,
        'ciso_view_employee' : ciso_view_employee,
        'ciso_view_location' : ciso_view_location,
        'ciso_view_category' : ciso_view_category,
        'ciso_view_department' : ciso_view_department,
        'ciso_view_roles':ciso_view_roles,
        'total_users' : total_users,
        'total_assets' : total_assets,
        'total_dept' : total_dept,
        'total_emp' : total_emp,


    }
    return render(request,'asset_mng/ciso_dashboard.html', context)


def asset_owner_dashboard(request):
    total_users = UserDetails.objects.count()
    total_assets = Asset_Table.objects.count()
    total_dept=Department.objects.count()
    total_emp=Employee.objects.count()
    username = request.session.get('username',None)
    user_role = request.session.get('role',None)
    name = request.session.get('name',None)

    if not username:
        return redirect('asset_login')
    user = UserDetails.objects.get(username=username)
    privileges = AssetOwner_Privilege.objects.filter(user=user)

    privilege_update = privileges.filter(privilege_update=True).exists()
    report_download = privileges.filter(report_download=True).exists()
    view_user = privileges.filter(view_user =True).exists()
    #add_user = privileges.filter(add_user =True).exists()
    view_employee = privileges.filter(view_employee =True).exists()
    view_location = privileges.filter(view_location = True).exists()
    view_category = privileges.filter(view_category = True).exists()
    view_department = privileges.filter(view_department = True).exists()
    view_roles = privileges.filter(view_roles = True).exists()

    context = {
        'username': username,
        'user_role': user_role,
        'name': name,
        'privilege_update': privilege_update,
        'report_download': report_download,
        'view_user' : view_user,
        #'add_user' : add_user,
        'view_employee' : view_employee,
        'view_location' : view_location,
        'view_category' : view_category,
        'view_department' : view_department,
        'view_roles':view_roles,
        'total_users' : total_users,
        'total_assets' : total_assets,
        'total_dept' : total_dept,
        'total_emp' : total_emp,

    }

    return render(request, 'asset_mng/asset_owner.html', context)

def asset_login(request):
    if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request,username=username,password=password)
            try:
                user = UserDetails.objects.get(username=username, password=password)
                if user is not None:
                    request.session['name'] = user.name
                    request.session['username'] = user.username
                    request.session['role'] = user.role     #pass the user's role to the template
                    #print(f"Session Data: {request.session['username']}, {request.session['role']}")  # Debugging statement
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
    username = request.session.get('username', None)
    user_role = request.session.get('role',None)
    name = request.session.get('name',None)
    view_user = False
    add_user = False
    edit_user = False
    delete_user = False
    privilege_update = False
    report_download = False
    view_employee = False
    view_location = False
    view_category = False
    view_department = False
    view_roles = False

    ciso_view_user = False
    ciso_add_user = False
    ciso_edit_user = False
    ciso_delete_user = False
    ciso_privilege_update = False
    ciso_report_download = False
    ciso_view_employee = False
    ciso_view_location = False
    ciso_view_category = False
    ciso_view_department = False
    ciso_view_roles = False

    head_view_user = False
    head_add_user = False
    head_edit_user = False
    head_delete_user = False
    head_privilege_update = False
    head_report_download = False
    head_view_employee = False
    head_view_location = False
    head_view_category = False
    head_view_department = False
    head_view_roles = False



    if user_role == 'asset_owner':      # Check if the logged-in user is an asset owner
        username = request.session.get('username',None)
        if username:
            try:
                user = UserDetails.objects.get(username=username)
                #print(f"User found: {user}")  # Debugging statement
                privileges = AssetOwner_Privilege.objects.filter(user=user)
                if privileges.exists():
                    add_user = privileges.filter(add_user = True).exists()
                    view_user = privileges.filter(view_user = True).exists()
                    edit_user = privileges.filter(edit_user = True).exists()
                    delete_user = privileges.filter(delete_user = True).exists()

                    privilege_update = privileges.filter(privilege_update=True).exists()
                    report_download = privileges.filter(report_download=True).exists()
                    view_employee = privileges.filter(view_employee = True).exists()
                    view_location = privileges.filter(view_location = True).exists()
                    view_category = privileges.filter(view_category = True).exists()
                    view_department = privileges.filter(view_department = True).exists()
                    view_roles = privileges.filter(view_roles = True).exists()
                #print(f"Privilege found: {privilege}, add_asset: {add_asset}")  # Debugging statement
            except UserDetails.DoesNotExist:
                print(f"UserDetails.DoesNotExist: {username}")
            except AssetOwner_Privilege.DoesNotExist:
                print(f"AssetOwner_Privilege.DoesNotExist for user: {user}")

    elif user_role == 'ciso':      # Check if the logged-in user is an ciso
        username = request.session.get('username',None)
        if username:
            try:
                user = UserDetails.objects.get(username=username)
                #print(f"User found: {user}")  # Debugging statement
                ciso_privileges = CISO_Privilege.objects.filter(user=user)
                if ciso_privileges.exists():
                    ciso_add_user = ciso_privileges.filter(ciso_add_user = True).exists()
                    ciso_view_user = ciso_privileges.filter(ciso_view_user = True).exists()
                    ciso_edit_user = ciso_privileges.filter(ciso_edit_user = True).exists()
                    ciso_delete_user = ciso_privileges.filter(ciso_delete_user = True).exists()

                    ciso_privilege_update = ciso_privileges.filter(ciso_privilege_update=True).exists()
                    ciso_report_download = ciso_privileges.filter(ciso_report_download=True).exists()
                    ciso_view_employee = ciso_privileges.filter(ciso_view_employee = True).exists()
                    ciso_view_location = ciso_privileges.filter(ciso_view_location = True).exists()
                    ciso_view_category = ciso_privileges.filter(ciso_view_category = True).exists()
                    ciso_view_department = ciso_privileges.filter(ciso_view_department = True).exists()
                    ciso_view_roles = ciso_privileges.filter(ciso_view_roles = True).exists()

                #print(f"Privilege found: {privilege}, add_asset: {add_asset}")  # Debugging statement
            except UserDetails.DoesNotExist:
                print(f"UserDetails.DoesNotExist: {username}")
            except AssetOwner_Privilege.DoesNotExist:
                print(f"AssetOwner_Privilege.DoesNotExist for user: {user}")  

    elif user_role == 'head':      # Check if the logged-in user is an head
        username = request.session.get('username',None)
        if username:
            try:
                user = UserDetails.objects.get(username=username)
                #print(f"User found: {user}")  # Debugging statement
                head_privileges = Head_Privilege.objects.filter(user=user)
                if head_privileges.exists():
                    head_add_user = head_privileges.filter(head_add_user = True).exists()
                    head_view_user = head_privileges.filter(head_view_user = True).exists()
                    head_edit_user = head_privileges.filter(head_edit_user = True).exists()
                    head_delete_user = head_privileges.filter(head_delete_user = True).exists()

                    head_privilege_update = head_privileges.filter(head_privilege_update=True).exists()
                    head_report_download = head_privileges.filter(head_report_download=True).exists()
                    head_view_employee = head_privileges.filter(head_view_employee = True).exists()
                    head_view_location = head_privileges.filter(head_view_location = True).exists()
                    head_view_category = head_privileges.filter(head_view_category = True).exists()
                    head_view_department = head_privileges.filter(head_view_department = True).exists()
                    head_view_roles = head_privileges.filter(head_view_roles = True).exists()
                #print(f"Privilege found: {privilege}, add_asset: {add_asset}")  # Debugging statement
            except UserDetails.DoesNotExist:
                print(f"UserDetails.DoesNotExist: {username}")
            except AssetOwner_Privilege.DoesNotExist:
                print(f"AssetOwner_Privilege.DoesNotExist for user: {user}")                        

    return render(request,'asset_mng/user.html',{'users':users,'departments': departments,'locations':locations, 'user_role': user_role,
                                                 'name':name, 'view_user':view_user, 'add_user' : add_user, 'edit_user' : edit_user, 'delete_user': delete_user,
                                                 'privilege_update':privilege_update,'view_roles':view_roles,
                                                 'report_download':report_download, 'view_employee': view_employee,'view_location':view_location,'view_category':view_category,'view_department':view_department,

                                                 'ciso_add_user':ciso_add_user,'ciso_view_user':ciso_view_user,'ciso_edit_user':ciso_edit_user,'ciso_delete_user':ciso_delete_user,
                                                 'ciso_privilege_update':ciso_privilege_update,'ciso_report_download':ciso_report_download,'ciso_view_roles':ciso_view_roles,
                                                 'ciso_view_employee':ciso_view_employee,'ciso_view_location':ciso_view_location,'ciso_view_category':ciso_view_category,'ciso_view_department':ciso_view_department,
                                                 
                                                 'head_add_user':head_add_user,'head_view_user':head_view_user,'head_edit_user':head_edit_user,'head_delete_user':head_delete_user,
                                                 'head_privilege_update':head_privilege_update,'head_report_download':head_report_download,'head_view_roles':head_view_roles,
                                                 'head_view_employee':head_view_employee,'head_view_location':head_view_location,'head_view_category':head_view_category,'head_view_department':head_view_department,
                                                 })

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

            if role == 'asset_owner':                              #add user's id to respective privileges model to set permission
                AssetOwner_Privilege.objects.create(user=new_user)
            elif role == 'ciso':
                CISO_Privilege.objects.create(user=new_user) 
            elif role == 'head':
                Head_Privilege.objects.create(user = new_user)       


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
    username = request.session.get('username', None)
    user_role = request.session.get('role',None)
    name = request.session.get('name',None)
    view_department = False
    add_department = False
    edit_department = False
    delete_department = False
    privilege_update = False
    report_download = False

    view_user = False
    view_location = False
    view_category = False
    view_employee = False
    view_roles = False
    

    ciso_add_department = False
    ciso_view_department = False
    ciso_edit_department = False
    ciso_delete_department = False
    ciso_privilege_update = False
    ciso_report_download = False

    ciso_view_user = False
    ciso_view_location = False
    ciso_view_category = False
    ciso_view_employee = False
    ciso_view_roles = False

    head_view_department = False
    head_add_department = False
    head_edit_department = False
    head_delete_department = False
    head_privilege_update = False
    head_report_download = False

    head_view_user = False
    head_view_location = False
    head_view_category = False
    head_view_employee = False
    head_view_roles = False

    if user_role == 'asset_owner':      # Check if the logged-in user is an asset owner
        username = request.session.get('username',None)
        if username:
            try:
                user = UserDetails.objects.get(username=username)
                #print(f"User found: {user}")  # Debugging statement
                privileges = AssetOwner_Privilege.objects.filter(user=user)
                if privileges.exists():
                    add_department = privileges.filter(add_department = True).exists()
                    view_department = privileges.filter(view_department = True).exists()
                    edit_department = privileges.filter(edit_department = True).exists()
                    delete_department = privileges.filter(delete_department = True).exists()

                    privilege_update = privileges.filter(privilege_update=True).exists()
                    report_download = privileges.filter(report_download=True).exists()
                    view_user = privileges.filter(view_user=True).exists()
                    view_location = privileges.filter(view_location = True).exists()
                    view_category = privileges.filter(view_category = True).exists()
                    view_employee = privileges.filter(view_employee = True).exists()
                    view_roles = privileges.filter(view_roles = True).exists()

                #print(f"Privilege found: {privilege}, add_asset: {add_asset}")  # Debugging statement
            except UserDetails.DoesNotExist:
                print(f"UserDetails.DoesNotExist: {username}")
            except AssetOwner_Privilege.DoesNotExist:
                print(f"AssetOwner_Privilege.DoesNotExist for user: {user}")
    elif user_role == 'ciso':      # Check if the logged-in user is an asset owner
        username = request.session.get('username',None)
        if username:
            try:
                user = UserDetails.objects.get(username=username)
                #print(f"User found: {user}")  # Debugging statement
                ciso_privileges = CISO_Privilege.objects.filter(user=user)
                if ciso_privileges.exists():
                    ciso_add_department = ciso_privileges.filter(ciso_add_department = True).exists()
                    ciso_view_department = ciso_privileges.filter(ciso_view_department = True).exists()
                    ciso_edit_department = ciso_privileges.filter(ciso_edit_department = True).exists()
                    ciso_delete_department = ciso_privileges.filter(ciso_delete_department = True).exists()

                    ciso_privilege_update = ciso_privileges.filter(ciso_privilege_update=True).exists()
                    ciso_report_download = ciso_privileges.filter(ciso_report_download=True).exists()
                    ciso_view_user = ciso_privileges.filter(ciso_view_user=True).exists()
                    ciso_view_location = ciso_privileges.filter(ciso_view_location = True).exists()
                    ciso_view_category = ciso_privileges.filter(ciso_view_category = True).exists()
                    ciso_view_employee = ciso_privileges.filter(ciso_view_employee = True).exists()
                    ciso_view_roles = ciso_privileges.filter(ciso_view_roles = True).exists()

                #print(f"Privilege found: {privilege}, add_asset: {add_asset}")  # Debugging statement
            except UserDetails.DoesNotExist:
                print(f"UserDetails.DoesNotExist: {username}")
            except AssetOwner_Privilege.DoesNotExist:
                print(f"AssetOwner_Privilege.DoesNotExist for user: {user}")      
    elif user_role == 'head':      # Check if the logged-in user is an asset owner
        username = request.session.get('username',None)
        if username:
            try:
                user = UserDetails.objects.get(username=username)
                #print(f"User found: {user}")  # Debugging statement
                head_privileges = Head_Privilege.objects.filter(user=user)
                if head_privileges.exists():
                    head_add_department = head_privileges.filter(head_add_department = True).exists()
                    head_view_department = head_privileges.filter(head_view_department = True).exists()
                    head_edit_department = head_privileges.filter(head_edit_department = True).exists()
                    head_delete_department = head_privileges.filter(head_delete_department = True).exists()

                    head_privilege_update = head_privileges.filter(head_privilege_update=True).exists()
                    head_report_download = head_privileges.filter(head_report_download=True).exists()
                    head_view_user = head_privileges.filter(head_view_user=True).exists()
                    head_view_location = head_privileges.filter(head_view_location = True).exists()
                    head_view_category = head_privileges.filter(head_view_category = True).exists()
                    head_view_employee = head_privileges.filter(head_view_employee = True).exists()
                    head_view_roles = head_privileges.filter(head_view_roles = True).exists()

                #print(f"Privilege found: {privilege}, add_asset: {add_asset}")  # Debugging statement
            except UserDetails.DoesNotExist:
                print(f"UserDetails.DoesNotExist: {username}")
            except AssetOwner_Privilege.DoesNotExist:
                print(f"AssetOwner_Privilege.DoesNotExist for user: {user}")                  


    return render(request, 'asset_mng/department_list.html', {'departments': departments,  'user_role': user_role,'name': name,
                                                       'add_department': add_department, 'view_department': view_department, 'edit_department': edit_department, 'delete_department': delete_department,
                                                       'privilege_update': privilege_update, 'report_download': report_download,'view_roles':view_roles,
                                                       'view_user': view_user,'view_location':view_location, 'view_category': view_category,'view_employee':view_employee,
                                                       
                                                       'ciso_add_department':ciso_add_department,'ciso_view_department':ciso_view_department,'ciso_edit_department':ciso_edit_department,'ciso_delete_department':ciso_delete_department,
                                                       'ciso_privilege_update':ciso_privilege_update,'ciso_report_download':ciso_report_download,'ciso_view_user':ciso_view_user,'ciso_view_location':ciso_view_location,
                                                       'ciso_view_category':ciso_view_category,'ciso_view_employee':ciso_view_employee,'ciso_view_roles':ciso_view_roles,
                                                       
                                                       'head_add_department':head_add_department,'head_view_department':head_view_department,'head_edit_department':head_edit_department,'head_delete_department':head_delete_department,
                                                       'head_privilege_update':head_privilege_update,'head_report_download':head_report_download,'head_view_roles':head_view_roles,
                                                       'head_view_user':head_view_user,'head_view_location':head_view_location,'head_view_category':head_view_category,'head_view_employee':head_view_employee,
                                                       })

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
    username = request.session.get('username', None)
    user_role = request.session.get('role',None)
    name = request.session.get('name',None)
    view_location = False
    add_location = False
    edit_location = False
    delete_location = False
    privilege_update = False
    report_download = False
    view_user = False
    view_employee = False
    view_category = False
    view_department = False
    view_roles = False

    ciso_view_location = False
    ciso_add_location = False
    ciso_edit_location = False
    ciso_delete_location = False
    ciso_privilege_update = False
    ciso_report_download = False
    ciso_view_user = False
    ciso_view_employee = False
    ciso_view_category = False
    ciso_view_department = False
    ciso_view_roles = False

    head_view_location = False
    head_add_location = False
    head_edit_location = False
    head_delete_location = False
    head_privilege_update = False
    head_report_download = False
    head_view_user = False
    head_view_employee = False
    head_view_category = False
    head_view_department = False
    head_view_roles = False

    

    if user_role == 'asset_owner':      # Check if the logged-in user is an asset owner
        username = request.session.get('username',None)
        if username:
            try:
                user = UserDetails.objects.get(username=username)
                #print(f"User found: {user}")  # Debugging statement
                privileges = AssetOwner_Privilege.objects.filter(user=user)
                if privileges.exists():
                    add_location = privileges.filter(add_location = True).exists()
                    view_location = privileges.filter(view_location = True).exists()
                    edit_location = privileges.filter(edit_location = True).exists()
                    delete_location = privileges.filter(delete_location = True).exists()

                    privilege_update = privileges.filter(privilege_update=True).exists()
                    report_download = privileges.filter(report_download=True).exists()
                    view_user = privileges.filter(view_user=True).exists()
                    view_employee = privileges.filter(view_employee = True).exists()
                    view_category = privileges.filter(view_category = True).exists()
                    view_department = privileges.filter(view_department = True).exists()
                    view_roles = privileges.filter(view_roles = True).exists()



                #print(f"Privilege found: {privilege}, add_asset: {add_asset}")  # Debugging statement
            except UserDetails.DoesNotExist:
                print(f"UserDetails.DoesNotExist: {username}")
            except AssetOwner_Privilege.DoesNotExist:
                print(f"AssetOwner_Privilege.DoesNotExist for user: {user}")
    elif user_role == 'ciso':      # Check if the logged-in user is an ciso
        username = request.session.get('username',None)
        if username:
            try:
                user = UserDetails.objects.get(username=username)
                #print(f"User found: {user}")  # Debugging statement
                ciso_privileges = CISO_Privilege.objects.filter(user=user)
                if ciso_privileges.exists():
                    ciso_add_location = ciso_privileges.filter(ciso_add_location = True).exists()
                    ciso_view_location = ciso_privileges.filter(ciso_view_location = True).exists()
                    ciso_edit_location = ciso_privileges.filter(ciso_edit_location = True).exists()
                    ciso_delete_location = ciso_privileges.filter(ciso_delete_location = True).exists()

                    ciso_privilege_update = ciso_privileges.filter(ciso_privilege_update=True).exists()
                    ciso_report_download = ciso_privileges.filter(ciso_report_download=True).exists()
                    ciso_view_user = ciso_privileges.filter(ciso_view_user=True).exists()
                    ciso_view_employee = ciso_privileges.filter(ciso_view_employee = True).exists()
                    ciso_view_category = ciso_privileges.filter(ciso_view_category = True).exists()
                    ciso_view_department = ciso_privileges.filter(ciso_view_department = True).exists()
                    ciso_view_roles = ciso_privileges.filter(ciso_view_roles = True).exists()

                #print(f"Privilege found: {privilege}, add_asset: {add_asset}")  # Debugging statement
            except UserDetails.DoesNotExist:
                print(f"UserDetails.DoesNotExist: {username}")
            except AssetOwner_Privilege.DoesNotExist:
                print(f"AssetOwner_Privilege.DoesNotExist for user: {user}")  

    elif user_role == 'head':      # Check if the logged-in user is an asset owner
        username = request.session.get('username',None)
        if username:
            try:
                user = UserDetails.objects.get(username=username)
                #print(f"User found: {user}")  # Debugging statement
                head_privileges = Head_Privilege.objects.filter(user=user)
                if head_privileges.exists():
                    head_add_location = head_privileges.filter(head_add_location = True).exists()
                    head_view_location = head_privileges.filter(head_view_location = True).exists()
                    head_edit_location = head_privileges.filter(head_edit_location = True).exists()
                    head_delete_location = head_privileges.filter(head_delete_location = True).exists()

                    head_privilege_update = head_privileges.filter(head_privilege_update=True).exists()
                    head_report_download = head_privileges.filter(head_report_download=True).exists()
                    head_view_user = head_privileges.filter(head_view_user=True).exists()
                    head_view_employee = head_privileges.filter(head_view_employee = True).exists()
                    head_view_category = head_privileges.filter(head_view_category = True).exists()
                    head_view_department = head_privileges.filter(head_view_department = True).exists()
                    head_view_roles = head_privileges.filter(head_view_roles = True).exists()



                #print(f"Privilege found: {privilege}, add_asset: {add_asset}")  # Debugging statement
            except UserDetails.DoesNotExist:
                print(f"UserDetails.DoesNotExist: {username}")
            except AssetOwner_Privilege.DoesNotExist:
                print(f"AssetOwner_Privilege.DoesNotExist for user: {user}")                      

    return render(request,'asset_mng/location_pro.html',{'users':users, 'user_role': user_role,'name': name,
                                                       'add_location': add_location, 'view_location': view_location, 'edit_location': edit_location, 'delete_location': delete_location,
                                                       'privilege_update': privilege_update, 'report_download': report_download,'view_roles':view_roles,
                                                       'view_user': view_user,'view_employee':view_employee,'view_category':view_category,'view_department':view_department,

                                                       'ciso_add_location':ciso_add_location,'ciso_view_location':ciso_view_location,'ciso_edit_location':ciso_edit_location,'ciso_delete_location':ciso_delete_location,
                                                       'ciso_privilege_update':ciso_privilege_update,'ciso_report_download':ciso_report_download,'ciso_view_roles':ciso_view_roles,
                                                       'ciso_view_user':ciso_view_user,'ciso_view_employee':ciso_view_employee,'ciso_view_category':ciso_view_category,'ciso_view_department':ciso_view_department,
                                                       
                                                       'head_add_location':head_add_location,'head_view_location':head_view_location,'head_edit_location':head_edit_location,'head_delete_location':head_delete_location,
                                                       'head_privilege_update':head_privilege_update,'head_report_download':head_report_download,'head_view_roles':head_view_roles,
                                                       'head_view_user':head_view_user,'head_view_employee':head_view_employee,'head_view_category':head_view_category,'head_view_department':head_view_department,
                                                       })


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
    username = request.session.get('username', None)
    user_role = request.session.get('role',None)
    name = request.session.get('name',None)
    view_category = False
    add_category = False
    edit_category = False
    delete_category = False
    privilege_update = False
    report_download = False
    view_user = False
    view_location = False
    view_employee = False
    view_department = False
    view_roles = False

    ciso_view_category = False
    ciso_add_category = False
    ciso_edit_category = False
    ciso_delete_category = False
    ciso_privilege_update = False
    ciso_report_download = False
    ciso_view_user = False
    ciso_view_location = False
    ciso_view_employee = False
    ciso_view_department = False
    ciso_view_roles = False

    head_view_category = False
    head_add_category = False
    head_edit_category = False
    head_delete_category = False
    head_privilege_update = False
    head_report_download = False
    head_view_user = False
    head_view_location = False
    head_view_employee = False
    head_view_department = False
    head_view_roles = False



    if user_role == 'asset_owner':      # Check if the logged-in user is an asset owner
        username = request.session.get('username',None)
        if username:
            try:
                user = UserDetails.objects.get(username=username)
                #print(f"User found: {user}")  # Debugging statement
                privileges = AssetOwner_Privilege.objects.filter(user=user)
                if privileges.exists():
                    add_category = privileges.filter(add_category = True).exists()
                    view_category = privileges.filter(view_category = True).exists()
                    edit_category = privileges.filter(edit_category = True).exists()
                    delete_category = privileges.filter(delete_category = True).exists()

                    privilege_update = privileges.filter(privilege_update=True).exists()
                    report_download = privileges.filter(report_download=True).exists()
                    view_user = privileges.filter(view_user=True).exists()
                    view_location = privileges.filter(view_location = True).exists()
                    view_employee = privileges.filter(view_employee = True).exists()
                    view_department = privileges.filter(view_department = True).exists()
                    view_roles = privileges.filter(view_roles = True).exists()

                #print(f"Privilege found: {privilege}, add_asset: {add_asset}")  # Debugging statement
            except UserDetails.DoesNotExist:
                print(f"UserDetails.DoesNotExist: {username}")
            except AssetOwner_Privilege.DoesNotExist:
                print(f"AssetOwner_Privilege.DoesNotExist for user: {user}")

    elif user_role == 'ciso':      # Check if the logged-in user is an asset owner
        username = request.session.get('username',None)
        if username:
            try:
                user = UserDetails.objects.get(username=username)
                #print(f"User found: {user}")  # Debugging statement
                ciso_privileges = CISO_Privilege.objects.filter(user=user)
                if ciso_privileges.exists():
                    ciso_add_category = ciso_privileges.filter(ciso_add_category = True).exists()
                    ciso_view_category = ciso_privileges.filter(ciso_view_category = True).exists()
                    ciso_edit_category = ciso_privileges.filter(ciso_edit_category = True).exists()
                    ciso_delete_category = ciso_privileges.filter(ciso_delete_category = True).exists()

                    ciso_privilege_update = ciso_privileges.filter(ciso_privilege_update=True).exists()
                    ciso_report_download = ciso_privileges.filter(ciso_report_download=True).exists()
                    ciso_view_user = ciso_privileges.filter(ciso_view_user=True).exists()
                    ciso_view_location = ciso_privileges.filter(ciso_view_location = True).exists()
                    ciso_view_employee = ciso_privileges.filter(ciso_view_employee = True).exists()
                    ciso_view_department = ciso_privileges.filter(ciso_view_department = True).exists()
                    ciso_view_roles = ciso_privileges.filter(ciso_view_roles = True).exists()

                #print(f"Privilege found: {privilege}, add_asset: {add_asset}")  # Debugging statement
            except UserDetails.DoesNotExist:
                print(f"UserDetails.DoesNotExist: {username}")
            except AssetOwner_Privilege.DoesNotExist:
                print(f"AssetOwner_Privilege.DoesNotExist for user: {user}")       

    elif user_role == 'head':      # Check if the logged-in user is an asset owner
        username = request.session.get('username',None)
        if username:
            try:
                user = UserDetails.objects.get(username=username)
                #print(f"User found: {user}")  # Debugging statement
                head_privileges = Head_Privilege.objects.filter(user=user)
                if head_privileges.exists():
                    head_add_category = head_privileges.filter(head_add_category = True).exists()
                    head_view_category = head_privileges.filter(head_view_category = True).exists()
                    head_edit_category = head_privileges.filter(head_edit_category = True).exists()
                    head_delete_category = head_privileges.filter(head_delete_category = True).exists()

                    head_privilege_update = head_privileges.filter(head_privilege_update=True).exists()
                    head_report_download = head_privileges.filter(head_report_download=True).exists()
                    head_view_user = head_privileges.filter(head_view_user=True).exists()
                    head_view_location = head_privileges.filter(head_view_location = True).exists()
                    head_view_employee = head_privileges.filter(head_view_employee = True).exists()
                    head_view_department = head_privileges.filter(head_view_department = True).exists()
                    head_view_roles = head_privileges.filter(head_view_roles = True).exists()

                #print(f"Privilege found: {privilege}, add_asset: {add_asset}")  # Debugging statement
            except UserDetails.DoesNotExist:
                print(f"UserDetails.DoesNotExist: {username}")
            except AssetOwner_Privilege.DoesNotExist:
                print(f"AssetOwner_Privilege.DoesNotExist for user: {user}")                 

    return render(request, 'asset_mng/category.html', {'categories': categories, 'user_role': user_role,'name': name,
                                                       'add_category': add_category, 'view_category': view_category, 'edit_category': edit_category, 'delete_category': delete_category,
                                                       'privilege_update': privilege_update, 'report_download': report_download,'view_roles':view_roles,
                                                       'view_user': view_user,'view_location':view_location,'view_employee': view_employee,'view_department':view_department,

                                                       'ciso_add_category':ciso_add_category,'ciso_view_category':ciso_view_category,'ciso_edit_category':ciso_edit_category,'ciso_delete_category':ciso_delete_category,'ciso_view_roles':ciso_view_roles,
                                                       'ciso_privilege_update':ciso_privilege_update,'ciso_report_download':ciso_report_download,'ciso_view_user':ciso_view_user,'ciso_view_location':ciso_view_location,'ciso_view_employee':ciso_view_employee,'ciso_view_department':ciso_view_department,
                                                       
                                                       'head_add_category':head_add_category,'head_view_category':head_view_category,'head_edit_category':head_edit_category,'head_delete_category':head_delete_category,
                                                       'head_privilege_update':head_privilege_update,'head_report_download':head_report_download,'head_view_roles':head_view_roles,
                                                       'head_view_user':head_view_user,'head_view_location':head_view_location,'head_view_employee':head_view_employee,'head_view_department':head_view_department,
                                                       })


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


def roles(request):
    users=UserDetails.objects.all()
    name = request.session.get('name', None)
    username = request.session.get('username', None)
    user_role = request.session.get('role',None)
    view_roles = False
    edit_roles = False
    privilege_update = False
    report_download = False
    view_employee = False
    view_location = False
    view_category = False
    view_department = False
    view_user = False

    ciso_view_roles = False
    ciso_edit_roles = False
    ciso_view_user = False
    ciso_privilege_update = False
    ciso_report_download = False
    ciso_view_employee = False
    ciso_view_location = False
    ciso_view_category = False
    ciso_view_department = False

    head_view_roles = False
    head_edit_roles = False
    head_view_user = False
    head_privilege_update = False
    head_report_download = False
    head_view_employee = False
    head_view_location = False
    head_view_category = False
    head_view_department = False

    if user_role == 'asset_owner':  # Check if the logged-in user is an asset owner
        username = request.session.get('username', None)
        if username:
            try:
                user = UserDetails.objects.get(username=username)
                privileges = AssetOwner_Privilege.objects.filter(user=user)
                if privileges.exists():
                    report_download = privileges.filter(report_download=True).exists()
                    privilege_update = privileges.filter(privilege_update=True).exists()
                    view_user = privileges.filter(view_user=True).exists()
                    view_employee = privileges.filter(view_employee=True).exists()
                    view_location = privileges.filter(view_location = True).exists()
                    view_category = privileges.filter(view_category = True).exists()
                    view_department = privileges.filter(view_department = True).exists()
                    view_roles = privileges.filter(view_roles = True).exists()
                    edit_roles = privileges.filter(edit_roles = True).exists()

            except UserDetails.DoesNotExist:
                print(f"UserDetails.DoesNotExist: {username}")
            except AssetOwner_Privilege.DoesNotExist:
                print(f"AssetOwner_Privilege.DoesNotExist for user: {user}")
    elif user_role == 'ciso':  # Check if the logged-in user is an ciso
        username = request.session.get('username', None)
        if username:
            try:
                user = UserDetails.objects.get(username=username)
                ciso_privileges = CISO_Privilege.objects.filter(user=user)
                if ciso_privileges.exists():
                    ciso_report_download = ciso_privileges.filter(ciso_report_download=True).exists()
                    ciso_privilege_update = ciso_privileges.filter(ciso_privilege_update=True).exists()
                    ciso_view_user = ciso_privileges.filter(ciso_view_user=True).exists()
                    ciso_view_employee = ciso_privileges.filter(ciso_view_employee=True).exists()
                    ciso_view_location = ciso_privileges.filter(ciso_view_location = True).exists()
                    ciso_view_category = ciso_privileges.filter(ciso_view_category = True).exists()
                    ciso_view_department = ciso_privileges.filter(ciso_view_department = True).exists()
                    ciso_view_roles = ciso_privileges.filter(ciso_view_roles = True).exists()
                    ciso_edit_roles = ciso_privileges.filter(ciso_edit_roles = True).exists()
                    

            except UserDetails.DoesNotExist:
                print(f"UserDetails.DoesNotExist: {username}")
            except AssetOwner_Privilege.DoesNotExist:
                print(f"AssetOwner_Privilege.DoesNotExist for user: {user}")  

    elif user_role == 'head':  # Check if the logged-in user is an asset owner
        username = request.session.get('username', None)
        if username:
            try:
                user = UserDetails.objects.get(username=username)
                head_privileges = Head_Privilege.objects.filter(user=user)
                if head_privileges.exists():
                    head_report_download = head_privileges.filter(head_report_download=True).exists()
                    head_privilege_update = head_privileges.filter(head_privilege_update=True).exists()
                    head_view_user = head_privileges.filter(head_view_user=True).exists()
                    head_view_employee = head_privileges.filter(head_view_employee=True).exists()
                    head_view_location = head_privileges.filter(head_view_location = True).exists()
                    head_view_category = head_privileges.filter(head_view_category = True).exists()
                    head_view_department = head_privileges.filter(head_view_department = True).exists()
                    head_view_roles = head_privileges.filter(head_view_roles = True).exists()
                    head_edit_roles = head_privileges.filter(head_edit_roles = True).exists()

            except UserDetails.DoesNotExist:
                print(f"UserDetails.DoesNotExist: {username}")
            except AssetOwner_Privilege.DoesNotExist:
                print(f"AssetOwner_Privilege.DoesNotExist for user: {user}")  

    context = { 
        'name': name,'users': users,'username':username,'user_role':user_role,'view_roles':view_roles,'edit_roles':edit_roles,
        'privilege_update':privilege_update,'report_download':report_download,'view_employee':view_employee,'view_location':view_location,'view_category':view_category,'view_department':view_department,'view_user':view_user,

        'ciso_view_roles':ciso_view_roles,'ciso_edit_roles':ciso_edit_roles,'ciso_view_user':ciso_view_user,'ciso_privilege_update':ciso_privilege_update,'ciso_report_download':ciso_report_download,
        'ciso_view_employee':ciso_view_employee,'ciso_view_location':ciso_view_location,'ciso_view_category':ciso_view_category,'ciso_view_department':ciso_view_department,

        'head_view_roles':head_view_roles,'head_edit_roles':head_edit_roles,'head_view_user':head_view_user,'head_privilege_update':head_privilege_update,'head_report_download':head_report_download,
        'head_view_employee':head_view_employee,'head_view_location':head_view_location,'head_view_category':head_view_category,'head_view_department':head_view_department,
    }
    return render(request,'asset_mng/roles.html',context)


def edit_roles(request,user_id):
    if request.method == 'POST':
        user_id = request.POST.get('id')
        user = get_object_or_404(UserDetails, pk=user_id)
        user.name = request.POST.get('name')
        
        user.status = request.POST.get('status')
        user.role = request.POST.get('role')
      
        user.save()
        messages.success(request, 'User updated successfully.')
        return redirect('roles')  # Redirect to user list page
    else:
        return redirect('roles')  # Redirect if not a POST request



def employee(request):
    employees = Employee.objects.all()
    username = request.session.get('username', None)
    user_role = request.session.get('role',None)
    name = request.session.get('name',None)
    view_employee = False
    add_employee = False
    edit_employee = False
    delete_employee = False
    privilege_update = False
    report_download = False
    view_user = False
    view_location = False
    view_category = False
    view_department = False
    view_roles = False

    ciso_view_employee = False
    ciso_add_employee = False
    ciso_edit_employee = False
    ciso_delete_employee = False
    ciso_privilege_update = False
    ciso_report_download = False
    ciso_view_user = False
    ciso_view_location = False
    ciso_view_category = False
    ciso_view_department = False
    ciso_view_roles = False

    head_view_employee = False
    head_add_employee = False
    head_edit_employee = False
    head_delete_employee = False
    head_privilege_update = False
    head_report_download = False
    head_view_user = False
    head_view_location = False
    head_view_category = False
    head_view_department = False
    head_view_roles = False

    if user_role == 'asset_owner':      # Check if the logged-in user is an asset owner
        username = request.session.get('username',None)
        if username:
            try:
                user = UserDetails.objects.get(username=username)
                #print(f"User found: {user}")  # Debugging statement
                privileges = AssetOwner_Privilege.objects.filter(user=user)
                if privileges.exists():
                    add_employee = privileges.filter(add_employee = True).exists()
                    view_employee = privileges.filter(view_employee = True).exists()
                    edit_employee = privileges.filter(edit_employee = True).exists()
                    delete_employee = privileges.filter(delete_employee = True).exists()

                    privilege_update = privileges.filter(privilege_update=True).exists()
                    report_download = privileges.filter(report_download=True).exists()
                    view_user = privileges.filter(view_user=True).exists()
                    view_location = privileges.filter(view_location = True).exists()
                    view_category = privileges.filter(view_category = True).exists()
                    view_department = privileges.filter(view_department = True).exists()
                    view_roles = privileges.filter(view_roles = True).exists()

                #print(f"Privilege found: {privilege}, add_asset: {add_asset}")  # Debugging statement
            except UserDetails.DoesNotExist:
                print(f"UserDetails.DoesNotExist: {username}")
            except AssetOwner_Privilege.DoesNotExist:
                print(f"AssetOwner_Privilege.DoesNotExist for user: {user}")

    elif user_role == 'ciso':      # Check if the logged-in user is an ciso

        username = request.session.get('username',None)
        if username:
            try:
                user = UserDetails.objects.get(username=username)
                #print(f"User found: {user}")  # Debugging statement
                ciso_privileges = CISO_Privilege.objects.filter(user=user)
                if ciso_privileges.exists():
                    ciso_add_employee = ciso_privileges.filter(ciso_add_employee = True).exists()
                    ciso_view_employee = ciso_privileges.filter(ciso_view_employee = True).exists()
                    ciso_edit_employee = ciso_privileges.filter(ciso_edit_employee = True).exists()
                    ciso_delete_employee = ciso_privileges.filter(ciso_delete_employee = True).exists()

                    ciso_privilege_update = ciso_privileges.filter(ciso_privilege_update=True).exists()
                    ciso_report_download = ciso_privileges.filter(ciso_report_download=True).exists()
                    ciso_view_user = ciso_privileges.filter(ciso_view_user=True).exists()
                    ciso_view_location = ciso_privileges.filter(ciso_view_location = True).exists()
                    ciso_view_category = ciso_privileges.filter(ciso_view_category = True).exists()
                    ciso_view_department = ciso_privileges.filter(ciso_view_department = True).exists()
                    ciso_view_roles = ciso_privileges.filter(ciso_view_roles = True).exists()    
            except UserDetails.DoesNotExist:
                print(f"UserDetails.DoesNotExist: {username}")
            except AssetOwner_Privilege.DoesNotExist:
                print(f"AssetOwner_Privilege.DoesNotExist for user: {user}")   
    elif user_role == 'head':      # Check if the logged-in user is an asset owner
        username = request.session.get('username',None)
        if username:
            try:
                user = UserDetails.objects.get(username=username)
                #print(f"User found: {user}")  # Debugging statement
                head_privileges = Head_Privilege.objects.filter(user=user)
                if head_privileges.exists():
                    head_add_employee = head_privileges.filter(head_add_employee = True).exists()
                    head_view_employee = head_privileges.filter(head_view_employee = True).exists()
                    head_edit_employee = head_privileges.filter(head_edit_employee = True).exists()
                    head_delete_employee = head_privileges.filter(head_delete_employee = True).exists()

                    head_privilege_update = head_privileges.filter(head_privilege_update=True).exists()
                    head_report_download = head_privileges.filter(head_report_download=True).exists()
                    head_view_user = head_privileges.filter(head_view_user=True).exists()
                    head_view_location = head_privileges.filter(head_view_location = True).exists()
                    head_view_category = head_privileges.filter(head_view_category = True).exists()
                    head_view_department = head_privileges.filter(head_view_department = True).exists()
                    head_view_roles = head_privileges.filter(head_view_roles = True).exists()

                #print(f"Privilege found: {privilege}, add_asset: {add_asset}")  # Debugging statement
            except UserDetails.DoesNotExist:
                print(f"UserDetails.DoesNotExist: {username}")
            except AssetOwner_Privilege.DoesNotExist:
                print(f"AssetOwner_Privilege.DoesNotExist for user: {user}")
                                     

    return render(request, 'asset_mng/employee.html', {'employees': employees, 'user_role': user_role,'name': name,
                                                       'add_employee': add_employee, 'view_employee': view_employee, 'edit_employee': edit_employee, 'delete_employee': delete_employee,
                                                       'privilege_update': privilege_update, 'report_download': report_download,'view_roles':view_roles,
                                                       'view_user': view_user,'view_location':view_location, 'view_category': view_category, 'view_department':view_department,

                                                        'ciso_add_employee':ciso_add_employee,'ciso_view_employee':ciso_view_employee,'ciso_edit_employee':ciso_edit_employee,
                                                       'ciso_delete_employee':ciso_delete_employee,'ciso_privilege_update':ciso_privilege_update,'ciso_view_roles':ciso_view_roles,
                                                       'ciso_report_download':ciso_report_download,'ciso_view_user':ciso_view_user,'ciso_view_location':ciso_view_location,
                                                       'ciso_view_category':ciso_view_category,'ciso_view_department':ciso_view_department,
                                                       
                                                       'head_add_employee':head_add_employee,'head_view_employee':head_view_employee,'head_edit_employee':head_edit_employee,'head_delete_employee':head_delete_employee,
                                                       'head_privilege_update':head_privilege_update,'head_report_download':head_report_download,'head_view_roles':head_view_roles,
                                                       'head_view_user':head_view_user,'head_view_location':head_view_location,'head_view_category':head_view_category,'head_view_department':head_view_department,

                                                       })

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
    name = request.session.get('name', None)
    user_role = request.session.get('role', None)
    
    # Default value for report_download privilege
    report_download = False
    privilege_update = False
    view_user = False
    view_employee = False
    view_location = False
    view_category = False
    view_department = False
    view_roles = False

    ciso_report_download = False
    ciso_privilege_update = False
    ciso_view_user = False
    ciso_view_employee = False
    ciso_view_location = False
    ciso_view_category = False
    ciso_view_department = False
    ciso_view_roles = False

    head_report_download = False
    head_privilege_update = False
    head_view_user = False
    head_view_employee = False
    head_view_location = False
    head_view_category = False
    head_view_department = False
    head_view_roles = False


    if user_role == 'asset_owner':  # Check if the logged-in user is an asset owner
        username = request.session.get('username', None)
        if username:
            try:
                user = UserDetails.objects.get(username=username)
                privileges = AssetOwner_Privilege.objects.filter(user=user)
                if privileges.exists():
                    report_download = privileges.filter(report_download=True).exists()
                    privilege_update = privileges.filter(privilege_update=True).exists()
                    view_user = privileges.filter(view_user=True).exists()
                    view_employee = privileges.filter(view_employee=True).exists()
                    view_location = privileges.filter(view_location = True).exists()
                    view_category = privileges.filter(view_category = True).exists()
                    view_department = privileges.filter(view_department = True).exists()
                    view_roles = privileges.filter(view_roles = True).exists()

            except UserDetails.DoesNotExist:
                print(f"UserDetails.DoesNotExist: {username}")
            except AssetOwner_Privilege.DoesNotExist:
                print(f"AssetOwner_Privilege.DoesNotExist for user: {user}")
    elif user_role == 'ciso':  # Check if the logged-in user is an asset owner
        username = request.session.get('username', None)
        if username:
            try:
                user = UserDetails.objects.get(username=username)
                ciso_privileges = CISO_Privilege.objects.filter(user=user)
                if ciso_privileges.exists():
                    ciso_report_download = ciso_privileges.filter(ciso_report_download=True).exists()
                    ciso_privilege_update = ciso_privileges.filter(ciso_privilege_update=True).exists()
                    ciso_view_user = ciso_privileges.filter(ciso_view_user=True).exists()
                    ciso_view_employee = ciso_privileges.filter(ciso_view_employee=True).exists()
                    ciso_view_location = ciso_privileges.filter(ciso_view_location = True).exists()
                    ciso_view_category = ciso_privileges.filter(ciso_view_category = True).exists()
                    ciso_view_department = ciso_privileges.filter(ciso_view_department = True).exists()
                    ciso_view_roles = ciso_privileges.filter(ciso_view_roles = True).exists()

            except UserDetails.DoesNotExist:
                print(f"UserDetails.DoesNotExist: {username}")
            except AssetOwner_Privilege.DoesNotExist:
                print(f"AssetOwner_Privilege.DoesNotExist for user: {user}")  

    elif user_role == 'head':  # Check if the logged-in user is an asset owner
        username = request.session.get('username', None)
        if username:
            try:
                user = UserDetails.objects.get(username=username)
                head_privileges = Head_Privilege.objects.filter(user=user)
                if head_privileges.exists():
                    head_report_download = head_privileges.filter(head_report_download=True).exists()
                    head_privilege_update = head_privileges.filter(head_privilege_update=True).exists()
                    head_view_user = head_privileges.filter(head_view_user=True).exists()
                    head_view_employee = head_privileges.filter(head_view_employee=True).exists()
                    head_view_location = head_privileges.filter(head_view_location = True).exists()
                    head_view_category = head_privileges.filter(head_view_category = True).exists()
                    head_view_department = head_privileges.filter(head_view_department = True).exists()
                    head_view_roles = head_privileges.filter(head_view_roles = True).exists()

            except UserDetails.DoesNotExist:
                print(f"UserDetails.DoesNotExist: {username}")
            except AssetOwner_Privilege.DoesNotExist:
                print(f"AssetOwner_Privilege.DoesNotExist for user: {user}")                      

    context = {
        'tables': ['UserDetails', 'Department'],
        'data': None,
        'selected_table': None,
        'user_role': user_role,
        'name': name,
        'report_download': report_download,'view_roles':view_roles,
        'privilege_update': privilege_update,'view_user':view_user, 'view_employee':view_employee,'view_location':view_location,'view_category':view_category,'view_department':view_department,

        'ciso_report_download':ciso_report_download,'ciso_privilege_update':ciso_privilege_update,'ciso_view_roles':ciso_view_roles,
        'ciso_view_user':ciso_view_user,'ciso_view_employee':ciso_view_employee,'ciso_view_location':ciso_view_location,'ciso_view_category':ciso_view_category,'ciso_view_department':ciso_view_department,

        'head_report_download':head_report_download,'head_privilege_update':head_privilege_update,'head_view_roles':head_view_roles,
        'head_view_user':head_view_user,'head_view_employee':head_view_employee,'head_view_location':head_view_location,'head_view_category':head_view_category,'head_view_department':head_view_department,

    }
    
    if request.method == 'POST':
        selected_table = request.POST.get('table')
        if selected_table == 'UserDetails':
            context['data'] = UserDetails.objects.all()
            context['selected_table'] = 'UserDetails'
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





def privileges(request):
    username =request.session.get('username',None)
    user_role = request.session.get('role',None)
    name = request.session.get('name',None)
    if not username:
        return redirect('asset_login')
    return render(request,'asset_mng/privileges.html',{'username':username,'user_role':user_role,'name':name})

def privilege_admin(request):
    username =request.session.get('username',None)
    user_role = request.session.get('role',None)
    name = request.session.get('name',None)
    if not username:
        return redirect('asset_login')
    return render(request,'asset_mng/privilege_admin.html',{'username':username,'user_role':user_role,'name':name})

def privilege_ciso(request):
    username =request.session.get('username',None)
    user_role = request.session.get('role',None)
    name = request.session.get('name',None)
    if not username:
        return redirect('asset_login')
    return render(request,'asset_mng/privilege_ciso.html',{'username':username,'user_role':user_role,'name':name})


def privilege_head(request):
    username =request.session.get('username',None)
    user_role = request.session.get('role',None)
    name = request.session.get('name',None)
    if not username:
        return redirect('asset_login')
    return render(request,'asset_mng/privilege_head.html',{'username':username,'user_role':user_role,'name':name})

@csrf_exempt
def privilege_asset_owner(request):
    username = request.session.get('username', None)
    user_role = request.session.get('role',None)
    name = request.session.get('name',None)
    if not username:
        return redirect('asset_login')
    
    user = UserDetails.objects.get(username=username)
    
    if request.method == 'POST':
        privilege_update = request.POST.get('privilege_update') == 'on'
        report_download = request.POST.get('report_download') == 'on'
        add_asset = request.POST.get('add_asset') == 'on'
        view_asset = request.POST.get('view_asset') == 'on'
        edit_asset = request.POST.get('edit_asset') == 'on'
        delete_asset = request.POST.get('delete_asset') == 'on'

        view_user = request.POST.get('view_user') == 'on'
        add_user = request.POST.get('add_user') == 'on'
        edit_user = request.POST.get('edit_user') == 'on'
        delete_user = request.POST.get('delete_user') == 'on'

        view_employee = request.POST.get('view_employee') == 'on'
        add_employee = request.POST.get('add_employee') == 'on'
        edit_employee = request.POST.get('edit_employee') == 'on'
        delete_employee = request.POST.get('delete_employee') == 'on'

        view_location = request.POST.get('view_location') == 'on'
        add_location = request.POST.get('add_location') == 'on'
        edit_location = request.POST.get('edit_location') == 'on'
        delete_location = request.POST.get('delete_location') == 'on'

        view_department = request.POST.get('view_department') == 'on'
        add_department = request.POST.get('add_department') == 'on'
        edit_department = request.POST.get('edit_department') == 'on'
        delete_department= request.POST.get('delete_department') == 'on'

        view_category = request.POST.get('view_category') == 'on'
        add_category = request.POST.get('add_category') == 'on'
        edit_category = request.POST.get('edit_category') == 'on'
        delete_category= request.POST.get('delete_category') == 'on'

        view_roles = request.POST.get('view_roles') == 'on'
        edit_roles = request.POST.get('edit_roles') == 'on'

        AssetOwner_Privilege.objects.all().update(add_asset=add_asset, view_asset = view_asset, edit_asset = edit_asset, delete_asset = delete_asset, 
                                                  report_download = report_download, privilege_update = privilege_update, 
                                                  view_user = view_user, add_user = add_user, edit_user = edit_user, delete_user = delete_user,
                                                  view_employee = view_employee, add_employee = add_employee, edit_employee = edit_employee, delete_employee = delete_employee,
                                                  view_location=view_location,add_location=add_location,edit_location=edit_location,delete_location=delete_location,
                                                  view_department = view_department, add_department = add_department, edit_department = edit_department, delete_department = delete_department,
                                                  view_category=view_category,add_category=add_category,edit_category=edit_category,delete_category=delete_category,
                                                  view_roles = view_roles,edit_roles=edit_roles,)
        return redirect('privilege_asset_owner')
    
    # Check if any asset owner has add_asset set to True to set the checkbox state
    any_privilege_update = AssetOwner_Privilege.objects.filter(privilege_update=True).exists()
    any_report_download = AssetOwner_Privilege.objects.filter(report_download=True).exists()
    any_add_asset = AssetOwner_Privilege.objects.filter(add_asset=True).exists()
    any_view_asset = AssetOwner_Privilege.objects.filter(view_asset = True).exists()
    any_edit_asset = AssetOwner_Privilege.objects.filter(edit_asset = True).exists()
    any_delete_asset = AssetOwner_Privilege.objects.filter(delete_asset=True).exists()

    any_view_user = AssetOwner_Privilege.objects.filter(view_user = True).exists()
    any_add_user = AssetOwner_Privilege.objects.filter(add_user = True).exists()
    any_edit_user = AssetOwner_Privilege.objects.filter(edit_user = True).exists()
    any_delete_user = AssetOwner_Privilege.objects.filter(delete_user = True).exists()

    any_view_employee = AssetOwner_Privilege.objects.filter(view_employee = True).exists()
    any_add_employee = AssetOwner_Privilege.objects.filter(add_employee = True).exists()
    any_edit_employee = AssetOwner_Privilege.objects.filter(edit_employee = True).exists()
    any_delete_employee = AssetOwner_Privilege.objects.filter(delete_employee = True).exists()

    any_view_location = AssetOwner_Privilege.objects.filter(view_location = True).exists()
    any_add_location= AssetOwner_Privilege.objects.filter(add_location= True).exists()
    any_edit_location= AssetOwner_Privilege.objects.filter(edit_location= True).exists()
    any_delete_location = AssetOwner_Privilege.objects.filter(delete_location = True).exists()

    any_view_department = AssetOwner_Privilege.objects.filter(view_department = True).exists()
    any_add_department= AssetOwner_Privilege.objects.filter(add_department= True).exists()
    any_edit_department= AssetOwner_Privilege.objects.filter(edit_department= True).exists()
    any_delete_department= AssetOwner_Privilege.objects.filter(delete_department = True).exists()

    any_view_category = AssetOwner_Privilege.objects.filter(view_category = True).exists()
    any_add_category= AssetOwner_Privilege.objects.filter(add_category= True).exists()
    any_edit_category= AssetOwner_Privilege.objects.filter(edit_category= True).exists()
    any_delete_category= AssetOwner_Privilege.objects.filter(delete_category = True).exists()

    any_view_roles = AssetOwner_Privilege.objects.filter(view_roles = True).exists()
    any_edit_roles = AssetOwner_Privilege.objects.filter(edit_roles = True).exists()



    return render(request, 'asset_mng/privilege_asset_owner.html', {
        'user_role': user_role,
        'username': username,
        'name': name,
        'privilege_update' : any_privilege_update,
        'report_download' : any_report_download,

        'view_roles':any_view_roles,
        'edit_roles':any_edit_roles,

        'add_asset': any_add_asset,
        'view_asset': any_view_asset,
        'edit_asset': any_edit_asset,
        'delete_asset': any_delete_asset,

        'view_user' : any_view_user,
        'add_user' : any_add_user,
        'edit_user': any_edit_user,
        'delete_user': any_delete_user,

        'view_employee' : any_view_employee,
        'add_employee' : any_add_employee,
        'edit_employee' : any_edit_employee,
        'delete_employee' : any_delete_employee,

        'view_department' : any_view_department,
        'add_department' : any_add_department,
        'edit_department': any_edit_department,
        'delete_department': any_delete_department,

        'view_location' : any_view_location,
        'add_location' : any_add_location,
        'edit_location': any_edit_location,
        'delete_location': any_delete_location,

        'view_category' : any_view_category,
        'add_category' : any_add_category,
        'edit_category': any_edit_category,
        'delete_category': any_delete_category,

    })

@csrf_exempt
def privilege_ciso(request):
    username = request.session.get('username', None)
    user_role = request.session.get('role',None)
    name = request.session.get('name',None)
    if not username:
        return redirect('asset_login')
    
    user = UserDetails.objects.get(username=username)
    
    if request.method == 'POST':
        ciso_privilege_update = request.POST.get('ciso_privilege_update') == 'on'
        ciso_report_download = request.POST.get('ciso_report_download') == 'on'
        ciso_add_asset = request.POST.get('ciso_add_asset') == 'on'
        ciso_view_asset = request.POST.get('ciso_view_asset') == 'on'
        ciso_edit_asset = request.POST.get('ciso_edit_asset') == 'on'
        ciso_delete_asset = request.POST.get('ciso_delete_asset') == 'on'

        ciso_view_user = request.POST.get('ciso_view_user') == 'on'
        ciso_add_user = request.POST.get('ciso_add_user') == 'on'
        ciso_edit_user = request.POST.get('ciso_edit_user') == 'on'
        ciso_delete_user = request.POST.get('ciso_delete_user') == 'on'

        ciso_view_employee = request.POST.get('ciso_view_employee') == 'on'
        ciso_add_employee = request.POST.get('ciso_add_employee') == 'on'
        ciso_edit_employee = request.POST.get('ciso_edit_employee') == 'on'
        ciso_delete_employee = request.POST.get('ciso_delete_employee') == 'on'

        ciso_view_location = request.POST.get('ciso_view_location') == 'on'
        ciso_add_location = request.POST.get('ciso_add_location') == 'on'
        ciso_edit_location = request.POST.get('ciso_edit_location') == 'on'
        ciso_delete_location = request.POST.get('ciso_delete_location') == 'on'

        ciso_view_department = request.POST.get('ciso_view_department') == 'on'
        ciso_add_department = request.POST.get('ciso_add_department') == 'on'
        ciso_edit_department = request.POST.get('ciso_edit_department') == 'on'
        ciso_delete_department= request.POST.get('ciso_delete_department') == 'on'

        ciso_view_category = request.POST.get('ciso_view_category') == 'on'
        ciso_add_category = request.POST.get('ciso_add_category') == 'on'
        ciso_edit_category = request.POST.get('ciso_edit_category') == 'on'
        ciso_delete_category = request.POST.get('ciso_delete_category') == 'on'

        ciso_view_roles = request.POST.get('ciso_view_roles') == 'on'
        ciso_edit_roles = request.POST.get('ciso_edit_roles') == 'on'

        CISO_Privilege.objects.all().update(
            ciso_add_asset=ciso_add_asset, ciso_view_asset=ciso_view_asset, ciso_edit_asset=ciso_edit_asset, ciso_delete_asset=ciso_delete_asset, 
            ciso_report_download=ciso_report_download, ciso_privilege_update=ciso_privilege_update, 
            ciso_view_user=ciso_view_user, ciso_add_user=ciso_add_user, ciso_edit_user=ciso_edit_user, ciso_delete_user=ciso_delete_user,
            ciso_view_employee=ciso_view_employee, ciso_add_employee=ciso_add_employee, ciso_edit_employee=ciso_edit_employee, ciso_delete_employee=ciso_delete_employee,
            ciso_view_location=ciso_view_location, ciso_add_location=ciso_add_location, ciso_edit_location=ciso_edit_location, ciso_delete_location=ciso_delete_location,
            ciso_view_department=ciso_view_department, ciso_add_department=ciso_add_department, ciso_edit_department=ciso_edit_department, ciso_delete_department=ciso_delete_department,
            ciso_view_category=ciso_view_category, ciso_add_category=ciso_add_category, ciso_edit_category=ciso_edit_category, ciso_delete_category=ciso_delete_category,
            ciso_view_roles=ciso_view_roles,ciso_edit_roles=ciso_edit_roles,
        )
        return redirect('privilege_ciso')
    
    # Check if any asset owner has ciso_add_asset set to True to set the checkbox state
    any_ciso_privilege_update = CISO_Privilege.objects.filter(ciso_privilege_update=True).exists()
    any_ciso_report_download = CISO_Privilege.objects.filter(ciso_report_download=True).exists()
    any_ciso_add_asset = CISO_Privilege.objects.filter(ciso_add_asset=True).exists()
    any_ciso_view_asset = CISO_Privilege.objects.filter(ciso_view_asset=True).exists()
    any_ciso_edit_asset = CISO_Privilege.objects.filter(ciso_edit_asset=True).exists()
    any_ciso_delete_asset = CISO_Privilege.objects.filter(ciso_delete_asset=True).exists()

    any_ciso_view_user = CISO_Privilege.objects.filter(ciso_view_user=True).exists()
    any_ciso_add_user = CISO_Privilege.objects.filter(ciso_add_user=True).exists()
    any_ciso_edit_user = CISO_Privilege.objects.filter(ciso_edit_user=True).exists()
    any_ciso_delete_user = CISO_Privilege.objects.filter(ciso_delete_user=True).exists()

    any_ciso_view_employee = CISO_Privilege.objects.filter(ciso_view_employee=True).exists()
    any_ciso_add_employee = CISO_Privilege.objects.filter(ciso_add_employee=True).exists()
    any_ciso_edit_employee = CISO_Privilege.objects.filter(ciso_edit_employee=True).exists()
    any_ciso_delete_employee = CISO_Privilege.objects.filter(ciso_delete_employee=True).exists()

    any_ciso_view_location = CISO_Privilege.objects.filter(ciso_view_location=True).exists()
    any_ciso_add_location = CISO_Privilege.objects.filter(ciso_add_location=True).exists()
    any_ciso_edit_location = CISO_Privilege.objects.filter(ciso_edit_location=True).exists()
    any_ciso_delete_location = CISO_Privilege.objects.filter(ciso_delete_location=True).exists()

    any_ciso_view_department = CISO_Privilege.objects.filter(ciso_view_department=True).exists()
    any_ciso_add_department = CISO_Privilege.objects.filter(ciso_add_department=True).exists()
    any_ciso_edit_department = CISO_Privilege.objects.filter(ciso_edit_department=True).exists()
    any_ciso_delete_department = CISO_Privilege.objects.filter(ciso_delete_department=True).exists()

    any_ciso_view_category = CISO_Privilege.objects.filter(ciso_view_category=True).exists()
    any_ciso_add_category = CISO_Privilege.objects.filter(ciso_add_category=True).exists()
    any_ciso_edit_category = CISO_Privilege.objects.filter(ciso_edit_category=True).exists()
    any_ciso_delete_category = CISO_Privilege.objects.filter(ciso_delete_category=True).exists()

    any_ciso_view_roles = CISO_Privilege.objects.filter(ciso_view_roles=True).exists()
    any_ciso_edit_roles = CISO_Privilege.objects.filter(ciso_edit_roles=True).exists()

    return render(request, 'asset_mng/privilege_ciso.html', {
        'user_role': user_role,
        'username': username,
        'name': name,
        'ciso_privilege_update': any_ciso_privilege_update,
        'ciso_report_download': any_ciso_report_download,

        'ciso_view_roles':any_ciso_view_roles,
        'ciso_edit_roles':any_ciso_edit_roles,

        'ciso_add_asset': any_ciso_add_asset,
        'ciso_view_asset': any_ciso_view_asset,
        'ciso_edit_asset': any_ciso_edit_asset,
        'ciso_delete_asset': any_ciso_delete_asset,

        'ciso_view_user': any_ciso_view_user,
        'ciso_add_user': any_ciso_add_user,
        'ciso_edit_user': any_ciso_edit_user,
        'ciso_delete_user': any_ciso_delete_user,

        'ciso_view_employee': any_ciso_view_employee,
        'ciso_add_employee': any_ciso_add_employee,
        'ciso_edit_employee': any_ciso_edit_employee,
        'ciso_delete_employee': any_ciso_delete_employee,

        'ciso_view_department': any_ciso_view_department,
        'ciso_add_department': any_ciso_add_department,
        'ciso_edit_department': any_ciso_edit_department,
        'ciso_delete_department': any_ciso_delete_department,

        'ciso_view_location': any_ciso_view_location,
        'ciso_add_location': any_ciso_add_location,
        'ciso_edit_location': any_ciso_edit_location,
        'ciso_delete_location': any_ciso_delete_location,

        'ciso_view_category': any_ciso_view_category,
        'ciso_add_category': any_ciso_add_category,
        'ciso_edit_category': any_ciso_edit_category,
        'ciso_delete_category': any_ciso_delete_category,
    })

@csrf_exempt
def privilege_head(request):
    username = request.session.get('username', None)
    user_role = request.session.get('role',None)
    name = request.session.get('name',None)
    if not username:
        return redirect('asset_login')
    
    user = UserDetails.objects.get(username=username)
    
    if request.method == 'POST':
        head_privilege_update = request.POST.get('head_privilege_update') == 'on'
        head_report_download = request.POST.get('head_report_download') == 'on'
        head_add_asset = request.POST.get('head_add_asset') == 'on'
        head_view_asset = request.POST.get('head_view_asset') == 'on'
        head_edit_asset = request.POST.get('head_edit_asset') == 'on'
        head_delete_asset = request.POST.get('head_delete_asset') == 'on'

        head_view_user = request.POST.get('head_view_user') == 'on'
        head_add_user = request.POST.get('head_add_user') == 'on'
        head_edit_user = request.POST.get('head_edit_user') == 'on'
        head_delete_user = request.POST.get('head_delete_user') == 'on'

        head_view_employee = request.POST.get('head_view_employee') == 'on'
        head_add_employee = request.POST.get('head_add_employee') == 'on'
        head_edit_employee = request.POST.get('head_edit_employee') == 'on'
        head_delete_employee = request.POST.get('head_delete_employee') == 'on'

        head_view_location = request.POST.get('head_view_location') == 'on'
        head_add_location = request.POST.get('head_add_location') == 'on'
        head_edit_location = request.POST.get('head_edit_location') == 'on'
        head_delete_location = request.POST.get('head_delete_location') == 'on'

        head_view_department = request.POST.get('head_view_department') == 'on'
        head_add_department = request.POST.get('head_add_department') == 'on'
        head_edit_department = request.POST.get('head_edit_department') == 'on'
        head_delete_department= request.POST.get('head_delete_department') == 'on'

        head_view_category = request.POST.get('head_view_category') == 'on'
        head_add_category = request.POST.get('head_add_category') == 'on'
        head_edit_category = request.POST.get('head_edit_category') == 'on'
        head_delete_category = request.POST.get('head_delete_category') == 'on'

        head_view_roles = request.POST.get('head_view_roles') == 'on'
        head_edit_roles = request.POST.get('head_edit_roles') == 'on'

        Head_Privilege.objects.all().update(
            head_add_asset=head_add_asset, head_view_asset=head_view_asset, head_edit_asset=head_edit_asset, head_delete_asset=head_delete_asset, 
            head_report_download=head_report_download, head_privilege_update=head_privilege_update, 
            head_view_user=head_view_user, head_add_user=head_add_user, head_edit_user=head_edit_user, head_delete_user=head_delete_user,
            head_view_employee=head_view_employee, head_add_employee=head_add_employee, head_edit_employee=head_edit_employee, head_delete_employee=head_delete_employee,
            head_view_location=head_view_location, head_add_location=head_add_location, head_edit_location=head_edit_location, head_delete_location=head_delete_location,
            head_view_department=head_view_department, head_add_department=head_add_department, head_edit_department=head_edit_department, head_delete_department=head_delete_department,
            head_view_category=head_view_category, head_add_category=head_add_category, head_edit_category=head_edit_category, head_delete_category=head_delete_category,
            head_view_roles=head_view_roles,head_edit_roles=head_edit_roles,
        )
        return redirect('privilege_head')
    
    # Check if any asset owner has ciso_add_asset set to True to set the checkbox state
    any_head_privilege_update = Head_Privilege.objects.filter(head_privilege_update=True).exists()
    any_head_report_download = Head_Privilege.objects.filter(head_report_download=True).exists()
    any_head_add_asset = Head_Privilege.objects.filter(head_add_asset=True).exists()
    any_head_view_asset = Head_Privilege.objects.filter(head_view_asset=True).exists()
    any_head_edit_asset = Head_Privilege.objects.filter(head_edit_asset=True).exists()
    any_head_delete_asset = Head_Privilege.objects.filter(head_delete_asset=True).exists()

    any_head_view_user = Head_Privilege.objects.filter(head_view_user=True).exists()
    any_head_add_user = Head_Privilege.objects.filter(head_add_user=True).exists()
    any_head_edit_user = Head_Privilege.objects.filter(head_edit_user=True).exists()
    any_head_delete_user = Head_Privilege.objects.filter(head_delete_user=True).exists()

    any_head_view_employee = Head_Privilege.objects.filter(head_view_employee=True).exists()
    any_head_add_employee = Head_Privilege.objects.filter(head_add_employee=True).exists()
    any_head_edit_employee = Head_Privilege.objects.filter(head_edit_employee=True).exists()
    any_head_delete_employee = Head_Privilege.objects.filter(head_delete_employee=True).exists()

    any_head_view_location =  Head_Privilege.objects.filter(head_view_location=True).exists()
    any_head_add_location = Head_Privilege.objects.filter(head_add_location=True).exists()
    any_head_edit_location = Head_Privilege.objects.filter(head_edit_location=True).exists()
    any_head_delete_location =  Head_Privilege.objects.filter(head_delete_location=True).exists()

    any_head_view_department =  Head_Privilege.objects.filter(head_view_department=True).exists()
    any_head_add_department = Head_Privilege.objects.filter(head_add_department=True).exists()
    any_head_edit_department =  Head_Privilege.objects.filter(head_edit_department=True).exists()
    any_head_delete_department =  Head_Privilege.objects.filter(head_delete_department=True).exists()

    any_head_view_category =  Head_Privilege.objects.filter(head_view_category=True).exists()
    any_head_add_category = Head_Privilege.objects.filter(head_add_category=True).exists()
    any_head_edit_category = Head_Privilege.objects.filter(head_edit_category=True).exists()
    any_head_delete_category =  Head_Privilege.objects.filter(head_delete_category=True).exists()

    any_head_view_roles =  Head_Privilege.objects.filter(head_view_roles=True).exists()
    any_head_edit_roles =  Head_Privilege.objects.filter(head_edit_roles=True).exists()


    return render(request, 'asset_mng/privilege_head.html', {
        'user_role': user_role,
        'username': username,
        'name': name,
        'head_privilege_update': any_head_privilege_update,
        'head_report_download': any_head_report_download,

        'head_view_roles':any_head_view_roles,
        'head_edit_roles':any_head_edit_roles,

        'head_add_asset': any_head_add_asset,
        'head_view_asset': any_head_view_asset,
        'head_edit_asset': any_head_edit_asset,
        'head_delete_asset': any_head_delete_asset,

        'head_view_user': any_head_view_user,
        'head_add_user': any_head_add_user,
        'head_edit_user': any_head_edit_user,
        'head_delete_user': any_head_delete_user,

        'head_view_employee': any_head_view_employee,
        'head_add_employee': any_head_add_employee,
        'head_edit_employee': any_head_edit_employee,
        'head_delete_employee': any_head_delete_employee,

        'head_view_department': any_head_view_department,
        'head_add_department': any_head_add_department,
        'head_edit_department': any_head_edit_department,
        'head_delete_department': any_head_delete_department,

        'head_view_location': any_head_view_location,
        'head_add_location': any_head_add_location,
        'head_edit_location': any_head_edit_location,
        'head_delete_location': any_head_delete_location,

        'head_view_category': any_head_view_category,
        'head_add_category': any_head_add_category,
        'head_edit_category': any_head_edit_category,
        'head_delete_category': any_head_delete_category,
    }) 

def asset_list(request):
    users = Asset_Table.objects.all()
    username = request.session.get('username', None)
    user_role = request.session.get('role',None)
    name = request.session.get('name',None)
    add_asset = False     
    view_asset = False
    edit_asset = False
    delete_asset = False               # Default value for add_asset privilege

    view_user = False
    view_employee = False
    view_location = False
    view_category = False
    view_department = False
    view_roles = False

    privilege_update = False
    report_download = False

    ciso_add_asset = False
    ciso_view_asset = False
    ciso_edit_asset = False
    ciso_delete_asset = False               # Default value for add_asset privilege

    ciso_view_user = False
    ciso_view_employee = False
    ciso_view_location = False
    ciso_view_category = False
    ciso_view_department = False
    ciso_view_roles = False

    ciso_privilege_update = False
    ciso_report_download = False

    head_add_asset = False
    head_view_asset = False
    head_edit_asset = False
    head_delete_asset = False               # Default value for add_asset privilege

    head_view_user = False
    head_view_employee = False
    head_view_location = False
    head_view_category = False
    head_view_department = False
    head_view_roles = False

    head_privilege_update = False
    head_report_download = False
    

    if user_role == 'asset_owner':      # Check if the logged-in user is an asset owner
        username = request.session.get('username',None)
        if username:
            try:
                user = UserDetails.objects.get(username=username)
                #print(f"User found: {user}")  # Debugging statement
                privileges = AssetOwner_Privilege.objects.filter(user=user)
                if privileges.exists():
                    add_asset = privileges.filter(add_asset = True).exists()
                    view_asset = privileges.filter(view_asset = True).exists()
                    edit_asset = privileges.filter(edit_asset = True).exists()
                    delete_asset = privileges.filter(delete_asset = True).exists()

                    privilege_update = privileges.filter(privilege_update=True).exists()
                    report_download = privileges.filter(report_download=True).exists()
                    view_user = privileges.filter(view_user=True).exists()
                    view_employee = privileges.filter(view_employee=True).exists()
                    view_location = privileges.filter(view_location = True).exists()
                    view_category = privileges.filter(view_category = True).exists()
                    view_department = privileges.filter(view_department = True).exists()
                    view_roles = privileges.filter(view_roles = True).exists()

                #print(f"Privilege found: {privilege}, add_asset: {add_asset}")  # Debugging statement
            except UserDetails.DoesNotExist:
                print(f"UserDetails.DoesNotExist: {username}")
            except AssetOwner_Privilege.DoesNotExist:
                print(f"AssetOwner_Privilege.DoesNotExist for user: {user}")
    elif user_role == 'ciso':
            username = request.session.get('username',None)        
            if username:
                try:
                    user = UserDetails.objects.get(username = username)
                    ciso_privileges = CISO_Privilege.objects.filter(user=user)
                    if ciso_privileges.exists():
                        ciso_add_asset = ciso_privileges.filter(ciso_add_asset = True).exists()
                        ciso_view_asset = ciso_privileges.filter(ciso_view_asset = True).exists()
                        ciso_edit_asset = ciso_privileges.filter(ciso_edit_asset = True).exists()
                        ciso_delete_asset = ciso_privileges.filter(ciso_delete_asset = True).exists()

                        ciso_privilege_update = ciso_privileges.filter(ciso_privilege_update=True).exists()
                        ciso_report_download = ciso_privileges.filter(ciso_report_download=True).exists()
                        ciso_view_user = ciso_privileges.filter(ciso_view_user=True).exists()
                        ciso_view_employee = ciso_privileges.filter(ciso_view_employee=True).exists()
                        ciso_view_location = ciso_privileges.filter(ciso_view_location = True).exists()
                        ciso_view_category = ciso_privileges.filter(ciso_view_category = True).exists()
                        ciso_view_department = ciso_privileges.filter(ciso_view_department = True).exists()
                        ciso_view_roles = privileges.filter(ciso_view_roles = True).exists()
                except UserDetails.DoesNotExist:
                    print(f"UserDetails.DoesNotExist: {username}")
                except AssetOwner_Privilege.DoesNotExist:
                    print(f"AssetOwner_Privilege.DoesNotExist for user: {user}") 
    elif user_role == 'head':      # Check if the logged-in user is an head
        username = request.session.get('username',None)
        if username:
            try:
                user = UserDetails.objects.get(username=username)
                #print(f"User found: {user}")  # Debugging statement
                head_privileges = Head_Privilege.objects.filter(user=user)
                if head_privileges.exists():
                    head_add_asset = head_privileges.filter(head_add_asset = True).exists()
                    head_view_asset = head_privileges.filter(head_view_asset = True).exists()
                    head_edit_asset = head_privileges.filter(head_edit_asset = True).exists()
                    head_delete_asset = head_privileges.filter(head_delete_asset = True).exists()

                    head_privilege_update = head_privileges.filter(head_privilege_update=True).exists()
                    head_report_download = head_privileges.filter(head_report_download=True).exists()
                    head_view_user = head_privileges.filter(head_view_user=True).exists()
                    head_view_employee = head_privileges.filter(head_view_employee=True).exists()
                    head_view_location = head_privileges.filter(head_view_location = True).exists()
                    head_view_category = head_privileges.filter(head_view_category = True).exists()
                    head_view_department = head_privileges.filter(head_view_department = True).exists()
                    head_view_roles = privileges.filter(head_view_roles = True).exists()

                #print(f"Privilege found: {privilege}, add_asset: {add_asset}")  # Debugging statement
            except UserDetails.DoesNotExist:
                print(f"UserDetails.DoesNotExist: {username}")
            except AssetOwner_Privilege.DoesNotExist:
                print(f"AssetOwner_Privilege.DoesNotExist for user: {user}")                
               
    return render(request, 'asset_mng/asset_pro.html', {
        'users': users,'name':name,'user_role':user_role,'add_asset':add_asset,
        'view_asset':view_asset,'edit_asset':edit_asset,'delete_asset':delete_asset,
        'username':username, 'privilege_update': privilege_update, 'report_download': report_download,
        'view_user':view_user, 'view_employee':view_employee,'view_location':view_location,'view_category':view_category,'view_department':view_department,'view_roles':view_roles,

        'ciso_add_asset':ciso_add_asset,'ciso_view_asset':ciso_view_asset,'ciso_edit_asset':ciso_edit_asset,'ciso_delete_asset':ciso_delete_asset,
        'ciso_privilege_update':ciso_privilege_update,'ciso_report_download':ciso_report_download,
        'ciso_view_user':ciso_view_user,'ciso_view_employee':ciso_view_employee,'ciso_view_location':ciso_view_location,'ciso_view_category':ciso_view_category,'ciso_view_department':ciso_view_department,'ciso_view_roles':ciso_view_roles,

        'head_add_asset':head_add_asset,'head_view_asset':head_view_asset,'head_edit_asset':head_edit_asset,'head_delete_asset':head_delete_asset,
        'head_privilege_update':head_privilege_update,'head_report_download':head_report_download,
        'head_view_user':head_view_user,'head_view_employee':head_view_employee,'head_view_location':head_view_location,'head_view_category':head_view_category,'head_view_department':head_view_department,'head_view_roles':head_view_roles,
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


