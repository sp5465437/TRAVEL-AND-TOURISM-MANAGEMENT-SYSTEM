from django.shortcuts import render,redirect
from myuser.models import *
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from myadmin.models import *
from django.shortcuts import get_object_or_404
import io
from django.template.loader import get_template
from django.template import Context
from xhtml2pdf import pisa
from django.utils import timezone
from django.http import HttpResponse
from django.utils.encoding import smart_str
from django.utils.html import escape
from django.templatetags.static import static
import razorpay
from django.http import JsonResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import os
from django.db.models.functions import Random
from django.http import JsonResponse

# Create your views here.
def index(request):
    # Retrieve all packages and order them randomly
    random_packages = Package.objects.all().order_by(Random())

    # Select the first four randomly ordered packages
    four_random_packages = random_packages[:4]

    # Retrieve all package places
    package_places = Package_Place.objects.all()

    # Pass the randomly selected four packages and package places to the template context
    context = {'packages': four_random_packages, 'package_places': package_places}

    # Render the template with the context
    return render(request, 'myuser/index.html', context)

def familypackage(request):
    package = Package.objects.all()
    package_places = Package_Place.objects.all()
    context = {'package': package, 'package_places': package_places }
    return render(request, 'myuser/familypackage.html', context)

def login(request):
	context = {}
	return render(request,'myuser/login.html',context)

def register(request):
	context = {}
	return render(request,'myuser/register.html',context)

def hotelslist(request):
	context = {}
	return render(request,'myuser/hotelslist.html',context)

def hoteldetail(request):
	context = {}
	return render(request,'myuser/hoteldetail.html',context)

def contact(request):
	context = {}
	return render(request,'myuser/contact.html',context)

def booking(request):
	context = {}
	return render(request,'myuser/booking.html',context)

def about(request):
	context = {}
	return render(request,'myuser/about.html',context)

def places(request):
	context = {}
	return render(request,'myuser/places.html',context)

def places1(request):
	context = {}
	return render(request,'myuser/places1.html',context)

def places2(request):
	context = {}
	return render(request,'myuser/places2.html',context)

def tourdetails(request, id):
    package = get_object_or_404(Package, id=id)
    package_places = Package_Place.objects.filter(package_id=id)
    packageimage = PackageImage.objects.filter(package_id=id)
    travel = get_object_or_404(Travel, package=package)
    hotel = get_object_or_404(Hotel, id=id)
    hotel_images = HotelImage.objects.filter(hotel=hotel)
    
    context = {
        'package': package,
        'package_places': package_places,
        'packageimage': packageimage,
        'hotel': hotel,
        'hotel_images': hotel_images,
        'travel': travel
    }
    return render(request, 'myuser/tourdetails.html', context)

def bookingtourpackage(request):
	context = {}
	return render(request,'myuser/bookingtourpackage.html',context)

def bookinghotel(request):
	context = {}
	return render(request,'myuser/bookinghotel.html',context)

def allpackage(request):
	context = {}
	return render(request,'myuser/allpackage.html',context)

def honeymoonpackage(request):
	context = {}
	return render(request,'myuser/honeymoonpackage.html',context)

def regularpackage(request):
	context = {}
	return render(request,'myuser/regularpackage.html',context)

def weekendpackage(request):
	context = {}
	return render(request,'myuser/weekendpackage.html',context)

def grouppackage(request):
	context = {}
	return render(request,'myuser/grouppackage.html',context)

def dashboard(request):
	context = {}
	return render(request,'myuser/dashboard.html',context)

def dbtravelbooking(request):
    user_id = request.user.id
    bookings = Booking.objects.filter(user_id=user_id)
    context = {'bookings': bookings}
    return render(request, 'myuser/dbtravelbooking.html', context)

def dbtraveldetails(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    package = get_object_or_404(Package, id=booking.package_id)  # Use booking.package_id instead of id
    package_places = Package_Place.objects.filter(package_id=booking.package_id)  # Use booking.package_id instead of id
    context = {'booking': booking , 'package': package , 'package_places' : package_places}
    return render(request, 'myuser/dbtraveldetails.html', context)
    
def dbhotelbooking(request):
	context = {}
	return render(request,'myuser/dbhotelbooking.html',context)

def dbhoteldetails(request):
	context = {}
	return render(request,'myuser/dbhoteldetails.html',context)

def dbpayment(request):
	context = {}
	return render(request,'myuser/dbpayment.html',context)

def dbmyprofile(request):
	user_id = request.user.id
	profile = Profile.objects.get(user_id=user_id)
	context = {'profile':profile}
	return render(request,'myuser/dbmyprofile.html',context)

def dballpayment(request):
	context = {}
	return render(request,'myuser/dballpayment.html',context)

def dbrefund(request):
	context = {}
	return render(request,'myuser/dbrefund.html',context)

def dbmyprofileedit(request):
    # Retrieve the user's profile data
    profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        # Update user and profile data based on form submission
        user = request.user
        user.username = request.POST['username']
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()

        profile.contact = request.POST['mobile']
        profile.dob = request.POST['dob']
        profile.gender =request.POST['gender']
        profile.save()

        return redirect('/myuser/dbmyprofile')

    context = {
        'data': profile
    }
    return render(request, 'myuser/dbmyprofileedit.html', context)

def feedback(request):
	context = {}
	return render(request,'myuser/feedback.html',context)

def inquiry(request):
	context = {}
	return render(request,'myuser/inquiry.html',context)

def store(request):
    # auth_user
    myfname     = request.POST['fname']
    mylname     = request.POST['lname']
    myemail     = request.POST['email']
    myusername  = request.POST['username']
    mypassword  = request.POST['password']
    mycpassword = request.POST['cpassword']

    #profile
    mycontact   = request.POST['contact']
    mydob   = request.POST['dob']
    mygender   = request.POST['gender']

    # Check if the username already exists
    if User.objects.filter(username=myusername).exists():
        messages.error(request, "Username already exists. Please choose another username.")
        return redirect('/myuser/register')

    if mypassword == mycpassword:
        result = User.objects.create_user(first_name=myfname,last_name=mylname,email=myemail,username=myusername,password=mypassword)
        Profile.objects.create(contact=mycontact,dob=mydob,gender=mygender,user_id=result.id)
        messages.success(request, "Registration Successfully")
        return redirect('/myuser/register')
    else:
        messages.success(request, "Mismatch Password")
        return redirect('/myuser/register')

def login_check(request):
	myusername = request.POST['username']
	mypassword = request.POST['password']

	result = auth.authenticate(username=myusername,password=mypassword)
	if result is None:
		messages.success(request, "Invalid Username or Password")
		return redirect('/myuser/login')
	else:
		auth.login(request,result)
		return redirect('/myuser/index')


def login_check(request):
    if request.method == 'POST':
        myusername = request.POST.get('username')
        mypassword = request.POST.get('password')

        user = auth.authenticate(username=myusername, password=mypassword)
        if user is not None and user.is_active:
            if user.is_staff:
                auth.login(request, user)
                messages.success(request, 'Invalid Username or Password')
                return redirect('/myuser/login')
            else:
                auth.login(request, user)
                return redirect('/myuser/index')
        else:
            messages.error(request, "Invalid Username or Password")
            return redirect('/myuser/login')
    else:
        return redirect('/myuser/login')

def dbmyprofileupdate(request, id):
    myfname = request.POST['fname']
    mylname = request.POST['lname']
    myemail = request.POST['email']
    myusername = request.POST['username']
    mycontact = request.POST['contact']
    mydob = request.POST['dob']
    mygender = request.POST['gender']

    user_data = {
        'first_name': myfname,
        'last_name': mylname,
        'email': myemail,
        'username': myusername
    }
    profile_data = {
        'contact': mycontact,
        'dob': mydob,
        'gender': mygender
    }
    User.objects.update_or_create(pk=id, defaults=user_data)  
    Profile.objects.update_or_create(pk=id, defaults=profile_data) 
    return redirect('/myuser/dbmyprofileedit')

def inquiry_store(request):
	name = request.POST['name']
	email = request.POST['email']
	contact = request.POST['contact']
	message = request.POST['message']

	Inquiry.objects.create(name=name,contact=contact,email=email,message=message)
	return redirect('/myuser/inquiry')

def feedback_store(request):
    rating = request.POST['rating']
    comment = request.POST['comment']
    user = request.user

    Feedback.objects.create(rating=rating, comment=comment, user=user)
    return redirect('/myuser/feedback')

def update_password(request):
    if request.method == "POST":
        old_password = request.POST['pwd1']
        new_password = request.POST['pwd2']
        confirm_password = request.POST['pwd3']

        user = User.objects.get(username=request.user.username)

        # Check if the old password matches the current password
        if not user.check_password(old_password):
            messages.error(request, 'Old password is incorrect.')
            return redirect("change_password")

        # Check if the new password and confirmation match
        if new_password != confirm_password:
            messages.error(request, 'New password and confirmation do not match.')
            return redirect("change_password")

        # Set and save the new password
        user.set_password(new_password)
        user.save()

        messages.success(request, 'Password changed successfully.')
        return redirect("/myuser/login")

    return render(request, 'myuser/change_password.html')

def change_password(request):
    context = {}
    return render(request,'myuser/change_password.html',context)


@login_required
def booking_store(request, package_id):
    if request.method == 'POST':
        user = request.user
        package = Package.objects.get(id=package_id)
        num_adults = int(request.POST.get('num_adults'))
        num_children = int(request.POST.get('num_children'))
        
        # Debug print statements to verify values
        print("Package Price:", package.price)
        print("Number of Adults:", num_adults)
        print("Number of Children:", num_children)

        # Assume child price is half of the adult price
        child_price = package.price / 2

        # Calculate amount based on adult and child prices
        amount = (package.price * num_adults) + (child_price * num_children)
        print("Calculated Amount:", amount)

        # Create booking
        booking = Booking.objects.create(
            user=user,
            amount=amount,
            package=package,
            date=date.today(),
            num_adults=num_adults,
            num_children=num_children, 
            status='Successfully', 
            payment_mode='Razorpay',
        )

        # Create Razorpay order
        order_data = {
            'amount': int(amount * 100),  # Razorpay expects amount in paisa
            'currency': 'INR',
            'payment_capture': '1', # Automatically capture payment when order is created
            "receipt":"OIBP",
            "notes":{
                'name' : 'AK',
                'payment_for':'OIBP Test'
            }
        }
        order = razorpay_client.order.create(data=order_data)
        order_id = order['id']
        
        # Update booking with Razorpay order ID
        booking.razorpay_order_id = order_id
        booking.save()

        # Redirect user to Razorpay payment page
        return render(request, 'myuser/payment.html', {'order_id': order_id, 'amount': amount})

    else:
        return redirect('booking_failed')

def booking_success(request):
    return render(request, 'myuser/booking_success.html')

def logout(request):
    auth.logout(request)
    return redirect('/myuser/index')

def booking(request, package_id):
    package = Package.objects.get(id=package_id)
    return render(request, 'myuser/booking.html', {'package': package})

def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = io.BytesIO()

    # Generate PDF
    pdf = pisa.pisaDocument(io.BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        # Prepare response
        response = HttpResponse(result.getvalue(), content_type='application/pdf')
        response['Content-Disposition'] = 'filename="invoice.pdf"'
        return response
    else:
        return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))

@login_required
def download_invoice_view(request, booking_id, package_id):
    # Retrieve booking and package details from the database
    booking = Booking.objects.get(id=booking_id)
    package = Package.objects.get(id=package_id)
    package_places = Package_Place.objects.filter(package_id=package_id)

    try:
        profile = request.user.profile
        customer_mobile = profile.contact
    except Profile.DoesNotExist:
        customer_mobile = None

    # Create a dictionary with booking, package, and profile details
    context = {
        'booking_date': booking.date,
        'customer_name': smart_str(request.user.first_name + ' ' + request.user.last_name if request.user.first_name and request.user.last_name else request.user.get_full_name()),
        'customer_email': request.user.email,
        'customer_mobile': customer_mobile,
        'num_children' : booking.num_children,
        'num_adults' : booking.num_adults,
        'amount' : booking.amount,
        'order_status': booking.status,
        'product_name': package.category,  
        'product_price': package.price,
        'from_date' : package.from_date,
        'to_date' : package.to_date,
        'image_url': package.image,
        'payment_mode' : booking.payment_mode,
        'place_name' : [place.place.name for place in package_places]
        # Add more fields as needed
    }

    # Render the PDF using the template and context
    return render_to_pdf('myuser/download_invoice.html', context)

def payment(request):
    context = {}
    return render(request,'myuser/payment.html',context)

# authorize razorpay client with API Keys.
razorpay_client = razorpay.Client(
    auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))

def update_booking_status(request):
    package_id = request.POST.get('package_id')
    status = request.POST.get('status')
    booking = Booking.objects.get(package_id=package_id)
    booking.status = status
    booking.save()
    return JsonResponse({'message': 'Booking status updated'})

