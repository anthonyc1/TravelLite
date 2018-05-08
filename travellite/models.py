from django.db import models

class User(models.Model):
	username = models.CharField(max_length=40)
	email = models.CharField(max_length=35, unique=True, primary_key=True)
	password = models.CharField(max_length=20)

class Location(models.Model):
	city = models.CharField(max_length=30)
	region = models.CharField(max_length=2)
	image = models.CharField(max_length=200)

class Review(models.Model):
	review = models.CharField(max_length=1000)
	rating = models.IntegerField()
	author = models.CharField(max_length=30)
	submissionDate = models.DateField()

class History(models.Model):
	userEmail = models.CharField(max_length=36)
	BOOKING_TYPES = [('flight', 'Flight'), ('train', 'Train'), ('hotel', 'Hotel')]
	bookingType = models.CharField(choices=BOOKING_TYPES, max_length=6)
	bookingStartDate = models.DateField()
	paymentAmount = models.DecimalField(max_digits=6,decimal_places=2)
	paymentCardNo = models.CharField(max_length=16)
	companyName = models.CharField(max_length=30, default='company')
	location = models.CharField(max_length=30, default='location')

class Flight(models.Model):
	companyName = models.CharField(max_length=30)
	sourceLocation = models.CharField(max_length=30)
	destinationLocation = models.CharField(max_length=30)
	departureDate = models.DateField()
	departureTime = models.TimeField()
	fareEconomy = models.DecimalField(max_digits=6,decimal_places=2)
	fareBusiness = models.DecimalField(max_digits=6,decimal_places=2)
	fareFirst = models.DecimalField(max_digits=6,decimal_places=2)
	numSeatsRemainingEconomy = models.IntegerField()
	numSeatsRemainingBusiness = models.IntegerField()
	numSeatsRemainingFirst = models.IntegerField()

class Train(models.Model):
	companyName = models.CharField(max_length=30)
	sourceLocation = models.CharField(max_length=30)
	destinationLocation = models.CharField(max_length=30)
	departureDate = models.DateField()
	departureTime = models.TimeField()
	fareEconomy = models.DecimalField(max_digits=6,decimal_places=2)
	fareBusiness = models.DecimalField(max_digits=6,decimal_places=2)
	fareFirst = models.DecimalField(max_digits=6,decimal_places=2)
	numSeatsRemainingEconomy = models.IntegerField()
	numSeatsRemainingBusiness = models.IntegerField()
	numSeatsRemainingFirst = models.IntegerField()

class Hotel(models.Model):
	dailyCost = models.DecimalField(max_digits=6,decimal_places=2)
	address = models.CharField(max_length=30)
	city = models.CharField(max_length=30)
	companyName = models.CharField(max_length=30,default='hotel')

class Payment(models.Model):
	PAYMENT_TYPES = [('credit', 'Credit'), ('debit', 'Debit')]
	amount = models.DecimalField(max_digits=6,decimal_places=2)
	paymentType = models.CharField(choices=PAYMENT_TYPES, max_length=6)
	cardNo = models.CharField(max_length=16)

class Attraction(models.Model):
	city = models.CharField(max_length=30, default='Stony Brook')
	attractionName = models.CharField(max_length=30)
	attractionDescription = models.CharField(max_length=1000)
	image = models.CharField(max_length=200)

# class Attraction(models.Model):
# 	#location = models.ManyToManyField(Location)

# 	attractionName = models.CharField(max_length=30)
# 	attractionDescription = models.CharField(max_length=1000)
# # 	image = models.CharField(max_length=200)

# 	# class Meta:
# 	# 	unique_together = ('city', 'region')

# class Purchase(models.Model):
# 	userID = models.ForeignKey(Booking, on_delete=models.DO_NOTHING, primary_key=True)
# 	bookingID = models.IntegerField()
# 	paymentID = models.IntegerField()