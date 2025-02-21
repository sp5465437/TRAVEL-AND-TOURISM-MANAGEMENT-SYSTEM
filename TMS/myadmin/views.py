from django.shortcuts import render,redirect
from myadmin.models import *
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.conf import settings
import os
from django.core.files.storage import FileSystemStorage
from myuser.models import *
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

def admin_or_login_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_staff or request.user.is_authenticated:
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponse("<h1>Please login first</h1>")
    return wrapper

@admin_or_login_required
def layout(request):
	context = {}
	return render(request,'myadmin/layout.html',context)

@admin_or_login_required
def dashboard(request):
	context = {}
	return render(request,'myadmin/dashboard.html',context)

def admin_login(request):
	context = {}
	return render(request,'myadmin/login.html',context)

@admin_or_login_required
def category(request):
	context = {}
	return render(request,'myadmin/category.html',context)

@admin_or_login_required
def viewcategory(request):
	context = {}
	return render(request,'myadmin/viewcategory.html',context)

@admin_or_login_required
def viewpackage(request):
	context = {}
	return render(request,'myadmin/viewpackage.html',context)

@admin_or_login_required
def add_state(request):
	context = {}
	return render(request,'myadmin/add_state.html',context)

@admin_or_login_required
def view_city(request):
	context = {}
	return render(request,'myadmin/view_city.html',context)

@admin_or_login_required
def view_state(request):
	context = {}
	return render(request,'myadmin/view_state.html',context)

@admin_or_login_required
def view_area(request):
	context = {}
	return render(request,'myadmin/view_area.html',context)

@admin_or_login_required
def viewuser(request):
    users = User.objects.filter(is_staff=False)
    context = {'users': users}
    return render(request, 'myadmin/viewuser.html', context)

@admin_or_login_required
def hotel(request):
    states = State.objects.all()
    cities = City.objects.all()
    areas = Area.objects.all()

    context = {
        'states': states,
        'cities': cities,
        'areas': areas,
    }
    
    return render(request, 'myadmin/hotel.html', context)

@admin_or_login_required
def viewhotel(request):
	result = Hotel.objects.all()
	result1 = HotelImage.objects.all()
	context = {'result' : result, 'result1' : result1}
	return render(request,'myadmin/viewhotel.html',context)

@admin_or_login_required
def viewhotel_image(request):
    result1 = HotelImage.objects.all()
    context = {'result1' : result1}
    return render(request,'myadmin/viewhotel_image.html',context)

@admin_or_login_required
def bookingdetail(request):
	context = {}
	return render(request,'myadmin/bookingdetail.html',context)

@admin_or_login_required
def viewfeedback(request):
	result = Feedback.objects.all()
	context = {'result' : result}
	return render(request,'myadmin/viewfeedback.html',context)

@admin_or_login_required
def payment(request):
	context = {}
	return render(request,'myadmin/payment.html',context)

@admin_or_login_required
def inquiry(request):
	result = Inquiry.objects.all()
	context = {'result' : result}
	return render(request, 'myadmin/inquiry.html', context)

@admin_or_login_required
def viewmore(request):
	context = {}
	return render(request,'myadmin/viewmore.html',context)

@admin_or_login_required
def viewinquiry(request, inquiry_id):
    inquiry = Inquiry.objects.get(id=inquiry_id)
    return render(request, 'myadmin/viewinquiry.html', {'row': inquiry})

@admin_or_login_required
def feedback(request,id):
	result = Feedback.objects.get(id=id)
	context = {'result' : result}
	return render(request,'myadmin/feedback.html',context)

@admin_or_login_required
def hoteldetail(request, hotel_id):
    result = Hotel.objects.get(id=hotel_id)
    hotel_images = HotelImage.objects.filter(hotel=result)
    context = {'result': result, 'hotel_images': hotel_images}
    return render(request, 'myadmin/hoteldetail.html', context)

@admin_or_login_required
def viewuserdetail(request):
	context = {}
	return render(request,'myadmin/viewuserdetail.html',context)

@admin_or_login_required
def booking(request):
	context = {}
	return render(request,'myadmin/booking.html',context)

@admin_or_login_required
def cat_edit(request):
	context = {}
	return render(request,'myadmin/cat_edit.html',context)

@admin_or_login_required
def cat_store(request):
    if request.method == 'POST':
        mycatname = request.POST.get('category_name')
        if mycatname:
            Category.objects.create(category_name=mycatname)
            messages.success(request, 'Category added successfully')
        else:
            messages.error(request, 'Category name cannot be empty')
    else:
        messages.error(request, 'Invalid request method')
    return redirect('/myadmin/category')

@admin_or_login_required
def viewcategory(request):  
    result = Category.objects.all()  
    return render(request,"myadmin/viewcategory.html",{'result':result})

@admin_or_login_required
def cat_delete(request,id):
	result = Category.objects.get(pk=id)
	result.delete()
	return redirect('/myadmin/viewcategory')

@admin_or_login_required
def cat_edit(request,id):
	result = Category.objects.get(pk=id)
	context = {'result':result}
	return render(request,'myadmin/cat_edit.html',context)

@admin_or_login_required
def cat_update(request,id):
	mycatname = request.POST['category_name']

	data = {
			'category_name':mycatname,
	}

	Category.objects.update_or_create(pk=id,defaults=data)
	return redirect('/myadmin/viewcategory')

@admin_or_login_required
def state_store(request):
	mystatename = request.POST['state_name']

	#insert
	State.objects.create(state_name=mystatename)
	return redirect('/myadmin/add_state')

@admin_or_login_required
def view_state(request):  
    result = State.objects.all()  
    return render(request,"myadmin/view_state.html",{'result':result})

@admin_or_login_required
def state_delete(request,id):
	result = State.objects.get(pk=id)
	result.delete()
	return redirect('/myadmin/view_state')

@admin_or_login_required
def state_edit(request,id):
	result = State.objects.get(pk=id)
	context = {'result':result}
	return render(request,'myadmin/state_edit.html',context)

@admin_or_login_required
def state_update(request,id):
	mystatename = request.POST['state_name']

	data = {
			'state_name': mystatename,
	}

	State.objects.update_or_create(pk=id,defaults=data)
	return redirect('/myadmin/view_state')

@admin_or_login_required
def add_city(request):
    result1 = State.objects.all()
    context = {'result1': result1}
    return render(request, 'myadmin/add_city.html', context)

@admin_or_login_required
def city_store(request):
    mycityname = request.POST['city_name']
    mystate_id = request.POST['state']  

    mystate = State.objects.get(pk=mystate_id)

    City.objects.create(city_name=mycityname, state=mystate)
    return redirect('/myadmin/add_city')

@admin_or_login_required
def view_city(request):
	result = City.objects.all()
	context = {'result':result}
	return render(request,'myadmin/view_city.html',context)

@admin_or_login_required
def city_delete(request,id):
	result = City.objects.get(pk=id)
	result.delete()
	return redirect('/myadmin/view_city')

@admin_or_login_required
def city_edit(request,id):
	result = City.objects.get(pk=id)
	result1 = State.objects.all()
	context = {'result':result,'result1':result1}
	return render(request,'myadmin/city_edit.html',context)

@admin_or_login_required
def city_update(request,id):
	mycityname = request.POST['city_name']
	mystate_id = request.POST['state']

	data = {
		'city_name':mycityname,
		'state_id':mystate_id,
	}

	City.objects.update_or_create(pk=id,defaults=data)
	return redirect('/myadmin/view_city')

@admin_or_login_required
def add_area(request):
    result1 = City.objects.all()
    context = {'result1': result1}
    return render(request, 'myadmin/add_area.html', context)

@admin_or_login_required
def area_store(request):
    myareaname = request.POST['area_name']
    mycity_id = request.POST['city']

    mycity = City.objects.get(pk=mycity_id)

    Area.objects.create(area_name=myareaname, city=mycity)
    return redirect('/myadmin/add_area')

@admin_or_login_required
def view_area(request):
    result = Area.objects.all()
    context = {'result': result}
    return render(request, 'myadmin/view_area.html', context)

@admin_or_login_required
def area_delete(request, id):
    result = Area.objects.get(pk=id)
    result.delete()
    return redirect('/myadmin/view_area')

@admin_or_login_required
def area_edit(request, id):
    result = Area.objects.get(pk=id)
    result1 = City.objects.all()
    context = {'result': result, 'result1': result1}
    return render(request, 'myadmin/area_edit.html', context)

@admin_or_login_required
def area_update(request, id):
    myareaname = request.POST['area_name']
    mycity_id = request.POST['city']

    data = {
        'area_name': myareaname,
        'city': City.objects.get(pk=mycity_id),
    }

    Area.objects.update_or_create(pk=id, defaults=data)
    return redirect('/myadmin/view_area')

def login_check(request):
    if request.method == 'POST':
        myusername = request.POST.get('username')
        mypassword = request.POST.get('password')

        user = auth.authenticate(username=myusername, password=mypassword)
        if user is not None and user.is_active:
            if user.is_staff:
                auth.login(request, user)
                return redirect('/myadmin/dashboard')
            else:
                auth.login(request, user)
                messages.success(request, 'Invalid Username or Password')
                return redirect('/myadmin/login')
        else:
            messages.error(request, "Invalid Username or Password")
            return redirect('/myadmin/login')
    else:
        return redirect('/myadmin/login')

@admin_or_login_required
def logout(request):
	auth.logout(request)
	return redirect('/myadmin/login')

@admin_or_login_required
def package(request):
    result1 = Category.objects.all()
    result = Hotel.objects.all()
    result3 = HotelImage.objects.all()
    result2 = Travel.objects.all()
    context = {'result1': result1 , 'result' : result , 'result2' : result2 , 'result3' : result3}
    return render(request, 'myadmin/package.html', context)

@admin_or_login_required
def package_store(request):
    if request.method == 'POST':
        # Retrieve form data
        category_id = request.POST.get('category')
        from_date = request.POST.get('from_date')
        to_date = request.POST.get('to_date')
        description = request.POST.get('description')
        hotel_id = request.POST.get('hotel')
        travel_id = request.POST.get('travel')
        price = request.POST.get('price')
        myfile = request.FILES.get('f')
        days = request.POST.get('days')
        
        if myfile:
            # Save uploaded files
            obj = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'upload'))
            filename = obj.save(myfile.name, myfile)

            # Create and save Package object
            package = Package.objects.create(
                category_id=category_id,
                from_date=from_date,
                to_date=to_date,
                description=description,
                hotel_id=hotel_id,
                travel_id=travel_id,
                price=price,
                image=filename,
                days=days,
            )
            
        return redirect('/myadmin/package') 
    return render(request, '/myadmin/package')

@admin_or_login_required
def viewpackage(request):
    result = Package.objects.all()
    context = {'result': result}
    return render(request,'myadmin/viewpackage.html',context)

def package_delete(request, id):
    pass

@admin_or_login_required
def package_edit(request, id):
    package = Package.objects.get(pk=id)
    category = Category.objects.all()
    hotel = Hotel.objects.all()
    travel = Travel.objects.all()
    context = {'hotel': hotel, 'package': package, 'category': category , 'travel' : travel}
    return render(request, 'myadmin/package_edit.html', context)

@admin_or_login_required
def package_update(request, id):
    if request.method == 'POST':
        # Retrieve the Package object from the database
        package = Package.objects.get(pk=id)
        
        # Retrieve form data
        category_id = request.POST.get('category')
        from_date = request.POST.get('from_date')
        to_date = request.POST.get('to_date')
        description = request.POST.get('description')
        hotel_id = request.POST.get('hotel')
        travel_id = request.POST.get('travel')
        price = request.POST.get('price')
        days = request.POST.get('days')
        
        # Update the Package object with new information
        package.category_id = category_id
        package.from_date = from_date
        package.to_date = to_date
        package.description = description
        package.hotel_id = hotel_id
        package.travel_id = travel_id
        package.price = price
        package.days =days

        try:
            myfile = request.FILES.get('f')
            if myfile:
                obj = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'upload'))
                filename = obj.save(myfile.name, myfile)
                package.image = filename
        except:
            pass
        # Save the changes
        package.save()
        
        # Redirect to a success page or view
        return redirect('/myadmin/viewpackage')
    
    # Handle GET request here if needed
    return render(request, '/myadmin/package_edit.html')

@admin_or_login_required
def viewuserdetail(request, user_id):
    user = User.objects.get(pk=user_id)
    context = {'user': user}
    return render(request, 'myadmin/viewuserdetail.html', context)

@admin_or_login_required
def travels(request):
	context = {}
	return render(request,'myadmin/travels.html',context)

@admin_or_login_required
def viewtravels(request):
    result = Travel.objects.all()
    context = {'result': result}
    return render(request, 'myadmin/viewtravels.html', context)

@admin_or_login_required
def hotel_store(request):
    if request.method == 'POST':
        # Retrieve data from POST request
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        address = request.POST.get('address')
        state_id = request.POST.get('state')
        city_id = request.POST.get('city')
        area_id = request.POST.get('area')
        status = request.POST.get('status')
        myfile = request.FILES.get('f')
        
        if myfile:
            # Save uploaded files
            obj = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'upload'))
            filename = obj.save(myfile.name, myfile)
            
            mystate = State.objects.get(pk=state_id)
            mycity = City.objects.get(pk=city_id)
            myarea = Area.objects.get(pk=area_id)

            # Create hotel object
            hotel = Hotel.objects.create(
                name=name,
                email=email,
                contact=contact,
                address=address,
                state=mystate,
                city=mycity,
                area=myarea,
                status=status,
                image=filename
            )

            return redirect('/myadmin/hotel')
        else:
            # Handle error if files are not provided
            return HttpResponse('Error: Please provide both images.')
    else:
        # Handle non-POST requests
        return HttpResponse('Error: This view only accepts POST requests.')

@admin_or_login_required
def hotel_image_store(request):
    hotel_id = request.POST.get('hotel')
    room_type = request.POST.get('room_type')
    ac_type = request.POST.get('ac_type')
    myfile1 = request.FILES.get('f1')

    if myfile1:
        obj = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'upload'))
        filename1 = obj.save(myfile1.name, myfile1)

        # Fetch the Hotel instance
        myhotel = Hotel.objects.get(pk=hotel_id)

        # Create hotel image object
        HotelImage.objects.create(
            hotel=myhotel,  # Assign the Hotel instance here
            room_type=room_type,
            ac_type=ac_type,
            image=filename1
        )

        return redirect('/myadmin/hotel_image')
    else:
        pass

@admin_or_login_required
def hotel_delete(request,id):
	result = Hotel.objects.get(pk=id)
	result.delete()
	return redirect('/myadmin/viewhotel')

@admin_or_login_required
def hotel_image_delete(request):
    result1 = HotelImage.objects.get(pk=id)
    result1.delete()
    return render('/myadmin/viewhotel_image')

@admin_or_login_required
def hotel_edit(request, id):
    hotel = Hotel.objects.get(pk=id)
    states = State.objects.all()
    areas = Area.objects.all()
    cities = City.objects.all()
    context = {'hotel': hotel, 'states': states, 'areas': areas , 'cities' : cities}
    return render(request, 'myadmin/hotel_edit.html', context)

@admin_or_login_required
def hotel_image_edit(request, id):
    hotel_image = HotelImage.objects.get(pk=id)
    hotels = Hotel.objects.all()
    context = {'hotels': hotels, 'hotel_image': hotel_image}
    return render(request, 'myadmin/hotel_image_edit.html', context)

@admin_or_login_required
def hotel_image_update(request, id):
    if request.method == 'POST':
        hotel_id = request.POST.get('hotel')
        room_type = request.POST.get('room_type')
        ac_type = request.POST.get('ac_type')

        myhotel = Hotel.objects.get(pk=hotel_id)
        hotel_image = HotelImage.objects.get(pk=id)
        hotel_image.hotel = myhotel
        hotel_image.room_type = room_type
        hotel_image.ac_type = ac_type

        try:
            myfile1 = request.FILES.get('f1')
            if myfile1:
                obj = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'upload'))
                filename1 = obj.save(myfile1.name, myfile1)
                hotel_image.image = filename1
        except:
            pass
        
        hotel_image.save()
        return redirect('/myadmin/viewhotel_image')
    else:
        return HttpResponse("This view only accepts POST requests.")

@admin_or_login_required
def hotel_update(request, id):
    name = request.POST.get('name')
    email = request.POST.get('email')
    contact = request.POST.get('contact')
    address = request.POST.get('address')
    state_id = request.POST.get('state')
    city_id = request.POST.get('city')
    area_id = request.POST.get('area')
    status = request.POST.get('status')

    mystate = State.objects.get(pk=state_id)
    mycity = City.objects.get(pk=city_id)
    myarea = Area.objects.get(pk=area_id)

    # Update hotel object
    hotel = Hotel.objects.get(pk=id)
    hotel.name = name
    hotel.email = email
    hotel.contact = contact
    hotel.address = address
    hotel.state = mystate
    hotel.city = mycity
    hotel.area = myarea
    hotel.status = status

    try:
        myfile = request.FILES.get('f')
        if myfile:
            obj = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'upload'))
            filename = obj.save(myfile.name, myfile)
            hotel.image = filename
    except:
        pass
    
    hotel.save()
    return redirect('/myadmin/viewhotel')

@admin_or_login_required
def travel_store(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        contact = request.POST.get('contact')
        vehicle_number = request.POST.get('vehicle_number')
        number_of_seats = request.POST.get('number_of_seats')
        travel_type = request.POST.get('travel_type')
        myfile = request.FILES.get('f')
        myfile1 = request.FILES.get('f1')

        if myfile and myfile1:
            # Save uploaded files
            obj = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'upload'))
            filename = obj.save(myfile.name, myfile)
            filename1 = obj.save(myfile1.name, myfile1)

            Travel.objects.create(
                name=name,
                contact=contact,
                vehicle_number=vehicle_number,
                number_of_seats=number_of_seats,
                travel_type=travel_type,
                image=filename,
                photo=filename1
            )

            return redirect('/myadmin/travels')
        else:
            # Handle error if files are not provided
            return HttpResponse('Error: Please provide both images.')
    else:
        # Handle non-POST requests
        return HttpResponse('Error: This view only accepts POST requests.')

@admin_or_login_required
def travel_delete(request,id):
    result = Travel.objects.get(pk=id)
    result.delete()
    return redirect('/myadmin/viewtravels')

@admin_or_login_required
def traveldetail(request,id):
    result = Travel.objects.get(id=id)
    context = {'result': result}
    return render(request, 'myadmin/traveldetail.html', context)

@admin_or_login_required
def packagedetail(request, id):
    package = Package.objects.get(id=id)
    package_places = Package_Place.objects.filter(package_id=id)
    context = {'package': package, 'package_places': package_places}
    return render(request, 'myadmin/packagedetail.html', context)

@admin_or_login_required
def package_delete(request,id):
    result = Package.objects.get(pk=id)
    result.delete()
    return redirect('/myadmin/viewpackage')

@admin_or_login_required
def hotel_image(request):
    result = Hotel.objects.all()
    context = {'result' : result}
    return render(request,'myadmin/hotel_image.html',context)

@admin_or_login_required
def travel_edit(request, id):
    travel = Travel.objects.get(pk=id)
    context = {'travel': travel}
    return render(request, 'myadmin/travel_edit.html', context)

@admin_or_login_required
def travel_update(request, id):
    if request.method == 'POST':
        # Retrieve the Travel object from the database
        travel = Travel.objects.get(pk=id)
        
        # Retrieve form data
        name = request.POST.get('name')
        contact = request.POST.get('contact')
        vehicle_number = request.POST.get('vehicle_number')
        number_of_seats = request.POST.get('number_of_seats')
        travel_type = request.POST.get('travel_type')

        # Update the Travel object with new information
        travel.name = name
        travel.contact = contact
        travel.vehicle_number = vehicle_number
        travel.number_of_seats = number_of_seats
        travel.travel_type = travel_type
        
        try:
            myfile = request.FILES.get('f')
            myfile1 = request.FILES.get('f1')

            if myfile:
                obj = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'upload'))
                filename = obj.save(myfile.name, myfile)
                travel.photo = filename

            if myfile1:
                obj = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'upload'))
                filename1 = obj.save(myfile1.name, myfile1)
                travel.image = filename1
        except:
            pass


        # Save the changes
        travel.save()
            
        # Redirect to a success page or view
        return redirect('/myadmin/viewtravels')
        
        # Handle GET request here if needed
    return render(request, '/myadmin/travel_edit.html')

@admin_or_login_required
def update_password(request):
    if request.method == "POST":
        old_password = request.POST['pwd1']
        new_password = request.POST['pwd2']
        confirm_password = request.POST['pwd3']

        user = User.objects.get(username=request.user.username)

        # Check if the old password matches the current password
        if not user.check_password(old_password):
            messages.error(request, 'Old password is incorrect.')

        # Check if the new password and confirmation match
        if new_password != confirm_password:
            messages.error(request, 'New password and confirmation do not match.')

        # Set and save the new password
        user.set_password(new_password)
        user.save()

        messages.success(request, 'Password changed successfully.')
        return redirect("/myadmin/dashboard")

    return render(request, 'myadmin/change_password.html')

@admin_or_login_required
def change_password(request):
    context = {}
    return render(request,'myadmin/change_password.html',context)

@admin_or_login_required
def package_place(request, id):
    result = Place.objects.all()
    package_id = id  
    try:
        result1 = Package_Place.objects.filter(package_id=package_id)
    except Package_Place.DoesNotExist:
        result1 = None

    return render(request, 'myadmin/package_place.html', {'result1': result1, 'result': result, 'package_id': package_id})

@admin_or_login_required
def package_place_store(request, id):
    if request.method == 'POST':
        package_id = id  
        place_id = request.POST.get('place')

        package_place = Package_Place.objects.create(
            package_id=package_id,
            place_id=place_id,
        )

        return redirect('/myadmin/package_place/{}'.format(package_id))
    return render(request, '/myadmin/package_place')

@admin_or_login_required
def place_store(request):
    myplacename = request.POST['place_name']

    #insert
    Place.objects.create(name=myplacename)
    return redirect('/myadmin/add_place')

@admin_or_login_required
def place_edit(request,id):
    result = Place.objects.get(pk=id)
    context = {'result':result}
    return render(request,'myadmin/place_edit.html',context)

@admin_or_login_required
def place_update(request, id):
    myplacename = request.POST['place_name']

    data = {
        'name': myplacename,  
    }

    Place.objects.update_or_create(pk=id, defaults=data)
    return redirect('/myadmin/view_place')

@admin_or_login_required
def place_delete(request,id):
    result = Place.objects.get(pk=id)
    result.delete()
    return redirect('/myadmin/view_place')

@admin_or_login_required
def add_place(request):
    context = {}
    return render(request,'myadmin/add_place.html',context)

@admin_or_login_required
def view_place(request):
    result = Place.objects.all()  
    context = {'result':result}
    return render(request,'myadmin/view_place.html',context)

@admin_or_login_required
def bookingdetail(request):
    result = Booking.objects.all()
    context = {'result' : result}
    return render(request,'myadmin/bookingdetail.html',context)

@admin_or_login_required
def upload_images(request):
    if request.method == 'POST':
        # Get the form data
        package_id = request.POST.get('package')
        package = Package.objects.get(id=package_id)

        # Create a PackageImage instance with the associated package
        package_image = PackageImage(package=package)

        # Loop through each image field and save the uploaded files
        for i in range(1, 8):
            image_field_name = f'image{i}'
            image_file = request.FILES.get(image_field_name)
            if image_file:
                setattr(package_image, image_field_name, image_file)

        # Save the PackageImage instance
        package_image.save()

        # Redirect to a success page or back to the upload page
        return redirect('/myadmin/add_package_image')

    else:
        # Render the upload form
        packages = Package.objects.all()
        return render(request, 'upload_images.html', {'packages': packages})

@admin_or_login_required
def add_package_image(request):
    packages = Package.objects.all()  # Get all packages
    print(packages)  # Print packages to console for debugging
    context = {'packages': packages}
    return render(request, 'myadmin/add_package_image.html', context)