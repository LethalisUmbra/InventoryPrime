from django.db import models
from django.core.validators import *

################## PRIMARY ##################
class Rifle(models.Model): # Barrel, Receiver, Stock
	id_rifle = models.AutoField(primary_key=True)
	name_rifle = models.CharField(max_length=50, validators=[MaxLengthValidator(150), MinLengthValidator(4)])
	blueprint_rifle = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	barrel_rifle = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	receiver_rifle = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	stock_rifle = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	owned_rifle = models.BooleanField(default=False)
	user_rifle = models.CharField(max_length=150, validators=[MaxLengthValidator(150), MinLengthValidator(4)])

	def __str__(self):
		return self.name_rifle

class Shotgun(models.Model): # Barrel, Receiver, Stock
	id_shotgun = models.AutoField(primary_key=True)
	name_shotgun = models.CharField(max_length=50, validators=[MaxLengthValidator(150), MinLengthValidator(4)])
	blueprint_shotgun = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	barrel_shotgun = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	receiver_shotgun = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	stock_shotgun = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	owned_shotgun = models.BooleanField(default=False)
	user_shotgun = models.CharField(max_length=150, validators=[MaxLengthValidator(150), MinLengthValidator(4)])

	def __str__(self):
		return self.name_shotgun

class Sniper(models.Model): # Barrel, Receiver, Stock
	id_sniper = models.AutoField(primary_key=True)
	name_sniper = models.CharField(max_length=50, validators=[MaxLengthValidator(150), MinLengthValidator(4)])
	blueprint_sniper = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	barrel_sniper = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	receiver_sniper = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	stock_sniper = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	owned_sniper = models.BooleanField(default=False)
	user_sniper = models.CharField(max_length=150, validators=[MaxLengthValidator(150), MinLengthValidator(4)])

	def __str__(self):
		return self.name_sniper

class Bow(models.Model): # Upper Limb, Lower Limb, Grip, String
	id_bow = models.AutoField(primary_key=True)
	name_bow = models.CharField(max_length=50, validators=[MaxLengthValidator(150), MinLengthValidator(4)])
	blueprint_bow = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	upper_bow = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	lower_bow = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	grip_bow = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	string_bow = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	owned_bow = models.BooleanField(default=False)
	user_bow = models.CharField(max_length=150, validators=[MaxLengthValidator(150), MinLengthValidator(4)])

	def __str__(self):
		return self.name_bow

class Zhuge(models.Model): # Grip, String, Barrel, Receiver
	id_zhuge = models.AutoField(primary_key=True)
	name_zhuge = models.CharField(max_length=50, validators=[MaxLengthValidator(150), MinLengthValidator(4)])
	blueprint_zhuge = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	grip_zhuge = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	string_zhuge = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	barrel_zhuge = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	receiver_zhuge = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	owned_zhuge = models.BooleanField(default=False)
	user_zhuge = models.CharField(max_length=150, validators=[MaxLengthValidator(150), MinLengthValidator(4)])

	def __str__(self):
		return self.name_zhuge