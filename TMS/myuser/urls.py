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
from django.urls import path , include ,re_path
from myuser import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('index',views.index,name='index'),
    path('store', views.store, name='store'),
    path('login',views.login,name='login'),
    path('login_check', views.login_check, name='login_check'),
    path('register',views.register,name='register'),
    path('familypackage',views.familypackage,name='familypackage'),
    path('honeymoonpackage',views.honeymoonpackage,name='honeymoonpackage'),
    path('hotelslist',views.hotelslist,name='hotelslist'),
    path('hoteldetail',views.hoteldetail,name='hoteldetail'),
    path('contact',views.contact,name='contact'),
    path('booking',views.booking,name='booking'),
    path('about',views.about,name='about'),
    path('places',views.places,name='places'),
    path('places1',views.places1,name='places1'),
    path('places2',views.places2,name='places2'),
    path('tourdetails/<int:id>',views.tourdetails,name='tourdetails'),
    path('bookingtourpackage',views.bookingtourpackage,name='bookingtourpackage'),
    path('bookinghotel',views.bookinghotel,name='bookinghotel'),
    path('allpackage',views.allpackage,name='allpackage'),
    path('regularpackage',views.regularpackage,name='regularpackage'),
    path('weekendpackage',views.weekendpackage,name='weekendpackage'),
    path('grouppackage',views.grouppackage,name='grouppackage'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('dbtravelbooking',views.dbtravelbooking,name='dbtravelbooking'),
    path('dbtraveldetails/<int:booking_id>',views.dbtraveldetails,name='dbtraveldetails'),
    path('dbhotelbooking',views.dbhotelbooking,name='dbhotelbooking'),
    path('dbhoteldetails',views.dbhoteldetails,name='dbhoteldetails'),
    path('dbpayment',views.dbpayment,name='dbpayment'),
    path('dbmyprofile',views.dbmyprofile,name='dbmyprofile'),
    path('dballpayment',views.dballpayment,name='dballpayment'),
    path('dbrefund',views.dbrefund,name='dbrefund'),
    path('dbmyprofileedit',views.dbmyprofileedit,name='dbmyprofileedit'),
    path('dbmyprofileedit/<int:id>',views.dbmyprofileedit,name='dbmyprofileedit'),
    path('dbmyprofileupdate/<int:id>',views.dbmyprofileupdate,name='dbmyprofileupdate'),
    path('feedback',views.feedback,name='feedback'),
    path('inquiry',views.inquiry,name='inquiry'),
    path('inquiry_store',views.inquiry_store,name='inquiry_store'),
    path('feedback_store',views.feedback_store,name='feedback_store'),
    path('change_password/', views.change_password, name='change_password'),
    path('update_password/', views.update_password, name='update_password'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='myuser/password_reset.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='myuser/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='myuser/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='myuser/password_reset_complete.html'), name='password_reset_complete'),
    path('booking_store/<int:package_id>/', views.booking_store, name='booking_store'),
    path('booking_success/', views.booking_success, name='booking_success'),
    path('logout',views.logout,name='logout'),
    path('booking/<int:package_id>/', views.booking, name='booking'),
    path('download-invoice/<int:package_id>/<int:booking_id>', views.download_invoice_view,name='download-invoice'),
    path('payment/', views.payment, name='payment'),
    path('update-booking-status/', views.update_booking_status, name='update_booking_status'),
]