from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('property_management/',views.prpty_mng,name='property_management'),
    path('asset/',views.asset_login,name='asset_login'),

    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('asset_owner_dashboard/', views.asset_owner_dashboard, name='asset_owner_dashboard'),
    path('head_dashboard/',views.head_dashboard,name='head_dashboard'),
    path('ciso_dashboard/',views.ciso_dashboard,name='ciso_dashboard'),

    path('privileges/',views.privileges,name='privileges'),
    
    path('privilege_admin/',views.privilege_admin,name='privilege_admin'),
    path('privilege_ciso/',views.privilege_ciso,name='privilege_ciso'),
    path('privilege_head/',views.privilege_head,name='privilege_head'),
    path('privilege_asset_owner/',views.privilege_asset_owner,name='privilege_asset_owner'),

    path('logout_view/', views.logout_view, name='logout_view'),

    path('asset_list/',views.asset_list,name='asset_list'),
    path('add/', views.add_asset, name='add_asset'),
    path('delete_asset/<int:user_id>/',views.delete_asset,name='delete_asset'),
    path('view/<int:user_id>/', views.view_asset, name='view_asset'),
    path('edit_asset/<int:asset_id>/', views.edit_asset, name='edit_asset'),
    
    path('user_list/',views.user_list,name='user_list'),
    path('save_user/', views.save_user, name='save_user'),
    path('edit_user/<int:user_id>/', views.edit_user, name='edit_user'),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),

    path('reports/', views.reports_view, name='reports'),

    path('roles/',views.roles,name='roles'),
    path('edit_roles/<int:user_id>/', views.edit_roles, name='edit_roles'),

    path('categories/', views.category_list, name='category_list'),
    path('save_category/', views.save_category, name='save_category'),
    path('categories/edit/<int:category_id>/', views.edit_category, name='edit_category'),
    path('categories/delete/<int:category_id>/', views.delete_category, name='delete_category'),

    path('departments/', views.department_list, name='department'),  
    path('edit_department/<int:department_id>/', views.edit_department, name='edit_department'),
    path('delete-department/<int:department_id>/', views.delete_department, name='delete_department'),
    path('department/add/', views.add_department, name='add_department'),

    path('employees/',views.employee,name='employee'),
    path('delete-employee/<int:employee_id>/', views.delete_employee, name='delete_employee'),
    path('edit_employee/<int:employee_id>/', views.edit_employee, name='edit_employee'),
    path('add_employee/', views.add_employee, name='add_employee'),

    path('location_list/',views.location_list,name='location_list'),
    path('add_location/', views.add_location, name='add_location'),
    path('delete_loc/<int:location_id>/',views.delete_loc,name='delete_loc'),
    path('location_list/edit/<int:location_id>/', views.edit_location, name='edit_location'),

]