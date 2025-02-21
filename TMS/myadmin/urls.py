"""
URL configuration for TMS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from myadmin import views

urlpatterns = [
    path('layout',views.layout,name='layout'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('login',views.admin_login,name='myadmin_login'),
    path('category',views.category,name='category'),
    path('cat_store',views.cat_store,name='cat_store'),
    path('package',views.package,name='package'),
    path('viewcategory',views.viewcategory,name='viewcategory'),
    path('viewpackage',views.viewpackage,name='viewpackage'),
    path('add_city',views.add_city,name='add_city'),
    path('add_state',views.add_state,name='add_state'),
    path('add_area',views.add_area,name='add_area'),
    path('view_city',views.view_city,name='view_city'),
    path('view_state',views.view_state,name='view_state'),
    path('view_area',views.view_area,name='view_area'),
    path('viewuser',views.viewuser,name='viewuser'),
    path('hotel',views.hotel,name='hotel'),
    path('viewhotel',views.viewhotel,name='viewhotel'),
    path('bookingdetail',views.bookingdetail,name='bookingdetail'),
    path('viewfeedback',views.viewfeedback,name='viewfeedback'),
    path('payment',views.payment,name='payment'),
    path('hotel_image',views.hotel_image,name='hotel_image'),
    path('hotel_image_edit/<int:id>/',views.hotel_image_edit,name='hotel_image_edit'),
    path('hotel_image_update/<int:id>/',views.hotel_image_update,name='hotel_image_update'),
    path('viewhotel_image',views.viewhotel_image,name='viewhotel_image'),
    path('hotel_image_store',views.hotel_image_store,name='hotel_image_store'),
    path('inquiry',views.inquiry,name='inquiry'),
    path('viewinquiry/<int:inquiry_id>/', views.viewinquiry, name='viewinquiry'),
    path('viewmore',views.viewmore,name='viewmore'),
    path('feedback/<int:id>',views.feedback,name='feedback'),
    path('hoteldetail/<hotel_id>',views.hoteldetail,name='hoteldetail'),
    path('packagedetail/<int:id>',views.packagedetail,name='packagedetail'),
    path('viewuserdetail/<int:user_id>',views.viewuserdetail,name='viewuserdetail'),
    path('booking',views.booking,name='booking'),
    path('hotel_image_delete/<int:id>',views.hotel_image_delete, name='hotel_image_delete'),
    path('cat_delete/<int:id>',views.cat_delete, name='cat_delete'),
    path('cat_edit/<int:id>',views.cat_edit, name='cat_edit'),
    path('cat_update/<int:id>',views.cat_update, name='cat_update'),
    path('state_store',views.state_store,name='state_store'),
    path('state_delete/<int:id>',views.state_delete, name='state_delete'),
    path('state_edit/<int:id>',views.state_edit, name='state_edit'),
    path('state_update/<int:id>',views.state_update, name='state_update'),
    path('city_store',views.city_store,name='city_store'),
    path('city_delete/<int:id>',views.city_delete, name='city_delete'),
    path('city_edit/<int:id>',views.city_edit, name='city_edit'),
    path('city_update/<int:id>',views.city_update, name='city_update'),
    path('area_store',views.area_store,name='area_store'),
    path('area_delete/<int:id>',views.area_delete, name='area_delete'),
    path('area_edit/<int:id>',views.area_edit, name='area_edit'),
    path('area_update/<int:id>',views.area_update, name='area_update'),
    path('login_check', views.login_check, name='login_check'),
    path('logout', views.logout, name='logout'),
    path('package_store',views.package_store,name='package_store'),
    path('package_delete/<int:id>',views.package_delete, name='package_delete'),
    path('package_edit/<int:id>/',views.package_edit, name='package_edit'),
    path('package_update/<int:id>/',views.package_update, name='package_update'),
    path('travels',views.travels,name='travels'),
    path('viewtravels',views.viewtravels,name='viewtravels'),
    path('traveldetail/<int:id>',views.traveldetail,name='traveldetail'),
    path('hotel_store',views.hotel_store,name='hotel_store'),
    path('hotel_delete/<int:id>',views.hotel_delete, name='hotel_delete'),
    path('travel_store',views.travel_store,name='travel_store'),
    path('travel_delete/<int:id>',views.travel_delete, name='travel_delete'),
    path('package_delete/<int:id>',views.package_delete, name='package_delete'),
    path('hotel_edit/<int:id>',views.hotel_edit, name='hotel_edit'),
    path('hotel_update/<int:id>',views.hotel_update, name='hotel_update'),
    path('travel_edit/<int:id>',views.travel_edit, name='travel_edit'),
    path('travel_update/<int:id>',views.travel_update, name='travel_update'),
    path('change_password/', views.change_password, name='change_password'),
    path('update_password/', views.update_password, name='update_password'),
    path('package_place/<int:id>',views.package_place,name='package_place'),
    path('package_place_store/<int:id>',views.package_place_store,name='package_place_store'),
    path('place_store',views.place_store,name='place_store'),
    path('add_place',views.add_place,name='add_place'),
    path('view_place',views.view_place,name='view_place'),
    path('place_edit/<int:id>',views.place_edit, name='place_edit'),
    path('place_update/<int:id>',views.place_update, name='place_update'),
    path('place_delete/<int:id>',views.place_delete, name='place_delete'),
    path('add_package_image',views.add_package_image,name='add_package_image'),
    path('upload_images',views.upload_images,name='upload_images'),
]
