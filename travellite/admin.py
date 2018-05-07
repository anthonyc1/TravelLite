from django.contrib import admin
from .models import User, Location

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
	list_display = ['username', 'email']

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
	list_display = ['city', 'region']