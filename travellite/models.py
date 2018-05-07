from django.db import models

class User(models.Model):
	username = models.CharField(max_length=40)
	email = models.CharField(max_length=35, unique=True, primary_key=True)
	password = models.CharField(max_length=20)

class Location(models.Model):
	city = models.CharField(max_length=30)
	region = models.CharField(max_length=2)
	country = models.CharField(max_length=2)
	image = models.CharField(max_length=200)

	class Meta:
		unique_together = ('city', 'region', 'country')

class Booking(models.Model):
	startDate = models.DateField()

class Transportation(models.Model):
	id = models.ForeignKey(Booking, on_delete=models.CASCADE,primary_key=True)
	sourceLocation = models.OneToOneField(Location, on_delete=models.DO_NOTHING, related_name='source')
	destinationLocation = models.OneToOneField(Location, on_delete=models.DO_NOTHING, related_name='destination')
	startDate = models.DateField()
	departureTime = models.TimeField()
	fareEconomy = models.DecimalField(max_digits=6,decimal_places=2)
	fareBusiness = models.DecimalField(max_digits=6,decimal_places=2)
	fareFirst = models.DecimalField(max_digits=6,decimal_places=2)
	numSeatsRemainingEconomy = models.IntegerField()
	numSeatsRemainingBusiness = models.IntegerField()
	numSeatsRemainingFirst = models.IntegerField()


	def clean(self):
		if fare <= 0:
			raise ValidationError('Fare must be greater than 0')

class Flight(models.Model):
	id = models.OneToOneField(Transportation, on_delete=models.DO_NOTHING, primary_key=True)
	airline = models.CharField(max_length=30)

class Train(models.Model):
	id = models.OneToOneField(Transportation, on_delete=models.DO_NOTHING, primary_key=True)
	railroad = models.CharField(max_length=30)

class Hotel(models.Model):
	id = models.OneToOneField(Booking, on_delete=models.DO_NOTHING, primary_key=True)
	startDate = models.DateField()
	dailyCost = models.DecimalField(max_digits=6,decimal_places=2)
	address = models.CharField(max_length=30)
	location = models.OneToOneField(Location, on_delete=models.DO_NOTHING)

	def clean(self):
		if dailyCost <= 0:
			raise ValidationError('Daily cost must be greater than 0')

class Payment(models.Model):
	PAYMENT_TYPES = [('credit', 'Credit'), ('debit', 'Debit')]
	amount = models.DecimalField(max_digits=6,decimal_places=2)
	paymentType = models.CharField(choices=PAYMENT_TYPES, max_length=6)
	cardNo = models.CharField(max_length=16)

	def clean(self):
		if amount <= 0:
			raise ValidationError('Amount must be greater than 0')

class Attraction(models.Model):
	city = models.CharField(max_length=30, default='Stony Brook')
	region = models.CharField(max_length=2, default='NY')
	attractionName = models.CharField(max_length=30)
	attractionDescription = models.CharField(max_length=1000)
	image = models.CharField(max_length=200)

# class Attraction(models.Model):
# 	#location = models.ManyToManyField(Location)

# 	attractionName = models.CharField(max_length=30)
# 	attractionDescription = models.CharField(max_length=1000)
# 	image = models.CharField(max_length=200)

	# class Meta:
	# 	unique_together = ('city', 'region')

class Purchase(models.Model):
	userID = models.ForeignKey(Booking, on_delete=models.DO_NOTHING, primary_key=True)
	bookingID = models.IntegerField()
	paymentID = models.IntegerField()