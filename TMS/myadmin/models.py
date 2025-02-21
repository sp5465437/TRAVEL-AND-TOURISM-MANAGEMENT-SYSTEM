from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name

    class Meta:
        db_table = 'Category'

class State(models.Model):
    state_name = models.CharField(max_length=50)

    def __str__(self):
        return self.state_name

    class Meta:
        db_table = 'State'

class City(models.Model):
    city_name = models.CharField(max_length=50)
    state = models.ForeignKey(State,on_delete=models.CASCADE)

    def __str__(self):
        return self.city_name

    class Meta:
        db_table = 'City'
 
class Area(models.Model):
    area_name = models.CharField(max_length=50)
    city = models.ForeignKey(City,on_delete=models.CASCADE)

    def __str__(self):
        return self.area_name

    class Meta:
        db_table = 'Area'

class Hotel(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    contact = models.CharField(max_length=10)
    image = models.CharField(max_length=200)
    address = models.TextField()
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    reg_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Hotel'

class HotelImage(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_type = models.CharField(max_length=100)
    ac_type = models.CharField(max_length=100)
    image = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.hotel.name} - {self.room_type} - {self.ac_type} - &#8377;{self.price}"

    class Meta:
        db_table = 'HotelImage'

class Travel(models.Model):
    name = models.CharField(max_length=200)
    contact = models.CharField(max_length=10)
    photo = models.CharField(max_length=200)
    vehicle_number = models.CharField(max_length=20)
    number_of_seats = models.PositiveIntegerField()
    image = models.CharField(max_length=200)
    travel_type = models.CharField(max_length=10)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Travel'

class Place(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Place'

class Package(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    from_date = models.DateField()
    to_date = models.DateField()
    description = models.TextField()
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    travel = models.ForeignKey(Travel, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.CharField(max_length=200,default=0)
    days = models.CharField(max_length=200,default=0)

    def __str__(self):
        return f"{self.category} - {self.from_date} to {self.to_date}"

    class Meta:
        db_table = 'Package'

class Package_Place(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Package_Place'

    def __str__(self):
        return f"{self.package.name} - {self.place.name}"

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    package = models.ForeignKey('Package', on_delete=models.CASCADE)
    num_children = models.IntegerField(default=0)
    num_adults = models.IntegerField(default=0)
    date = models.DateField()
    status = models.CharField(max_length=20, default='Pending')
    payment_mode = models.CharField(max_length=20)
    razorpay_order_id = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.package.name} - {self.date}"

    class Meta:
        db_table = 'Booking'

class PackageImage(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    image = models.ImageField(max_length=200)
    image1 = models.ImageField(max_length=200, blank=True, null=True)
    image2 = models.ImageField(max_length=200, blank=True, null=True)
    image3 = models.ImageField(max_length=200, blank=True, null=True)
    image4 = models.ImageField(max_length=200, blank=True, null=True)
    image5 = models.ImageField(max_length=200, blank=True, null=True)
    image6 = models.ImageField(max_length=200, blank=True, null=True)
    image7 = models.ImageField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"Images of {self.package}"

    class Meta:
        db_table = 'PackageImage'

