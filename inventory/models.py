from django.db import models
from django.core.validators import *

################## SECONDARY ##################
class Ballista(models.Model): # Upper Limb, Lower Limb, String, Receiver
	id_ballista = models.AutoField(primary_key=True)
	name_ballista = models.CharField(max_length=50, validators=[MaxLengthValidator(150), MinLengthValidator(4)])
	blueprint_ballista = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	upper_ballista = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	lower_ballista = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	string_ballista = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	receiver_ballista = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	owned_ballista = models.BooleanField()

	def __str__(self):
		return self.name_ballista

class AK(models.Model): # 2x Barrel, 2x Receiver, Link
	id_ak = models.AutoField(primary_key=True)
	name_ak = models.CharField(max_length=50, validators=[MaxLengthValidator(150), MinLengthValidator(4)])
	blueprint_ak = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	barrel_ak = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	receiver_ak = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	link_ak = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	owned_ak = models.BooleanField()

	def __str__(self):
		return self.name_ak

class Dual(models.Model): # 2x Single Weapon, Link
	id_dual = models.AutoField(primary_key=True)
	name_dual = models.CharField(max_length=50, validators=[MaxLengthValidator(150), MinLengthValidator(4)])
	single_dual = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	link_dual = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	owned_dual = models.BooleanField()

	def __str__(self):
		return self.name_dual

class Thrown(models.Model): # 2x Pouch, 2x Stars
	id_thrown = models.AutoField(primary_key=True)
	name_thrown = models.CharField(max_length=50, validators=[MaxLengthValidator(150), MinLengthValidator(4)])
	blueprint_thrown = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	pouch_thrown = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	starts_thrown = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	owned_thrown = models.BooleanField()

	def __str__(self):
		return self.name_thrown

class Shotgun_Sidearm(models.Model): # Barrel, Receiver
	id_sidearm = models.AutoField(primary_key=True)
	name_sidearm = models.CharField(max_length=50, validators=[MaxLengthValidator(150), MinLengthValidator(4)])
	blueprint_sidearm = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	barrel_sidearm = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	receiver_sidearm = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	owned_sidearm = models.BooleanField()

	def __str__(self):
		return self.name_sidearm

class Pistol(models.Model): # Barrel, Receiver
	id_pistol = models.AutoField(primary_key=True)
	name_pistol = models.CharField(max_length=50, validators=[MaxLengthValidator(150), MinLengthValidator(3)])
	blueprint_pistol = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	barrel_pistol = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	receiver_pistol = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	owned_pistol = models.BooleanField()

	def __str__(self):
		return self.name_pistol


################## MELEE ##################
class Fist(models.Model): # 2x Blade, 2x Gauntlet
	id_fist = models.AutoField(primary_key=True)
	name_fist = models.CharField(max_length=50, validators=[MaxLengthValidator(150), MinLengthValidator(4)])
	blueprint_fist = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	blade_fist = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	guantlet_fist = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	owned_fist = models.BooleanField()

	def __str__(self):
		return self.name_fist

class Claws(models.Model): # 2x Blade, 2x Gauntlet
	id_claws = models.AutoField(primary_key=True)
	name_claws = models.CharField(max_length=50, validators=[MaxLengthValidator(150), MinLengthValidator(4)])
	blueprint_claws = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	blade_claws = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	guantlet_claws = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	owned_claws = models.BooleanField()

	def __str__(self):
		return self.name_claws

class Staff(models.Model): # 2x Ornament, Handle
	id_staff = models.AutoField(primary_key=True)
	name_staff = models.CharField(max_length=50, validators=[MaxLengthValidator(150), MinLengthValidator(2)])
	blueprint_staff = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	ornament_staff = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	handle_staff = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	owned_staff = models.BooleanField()

	def __str__(self):
		return self.name_staff

class Sword(models.Model): # Blade, Handle
	id_sword = models.AutoField(primary_key=True)
	name_sword = models.CharField(max_length=50, validators=[MaxLengthValidator(150), MinLengthValidator(4)])
	blueprint_sword = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	blade_sword = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	handle_sword = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	owned_sword = models.BooleanField()

	def __str__(self):
		return self.name_sword

class Rapier(models.Model): # Blade, Handle
	id_rapier = models.AutoField(primary_key=True)
	name_rapier = models.CharField(max_length=50, validators=[MaxLengthValidator(150), MinLengthValidator(4)])
	blueprint_rapier = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	blade_rapier = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	handle_rapier = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	owned_rapier = models.BooleanField()

	def __str__(self):
		return self.name_rapier

class Heavy_Blade(models.Model): # Blade, Handle
	id_heavy = models.AutoField(primary_key=True)
	name_heavy = models.CharField(max_length=50, validators=[MaxLengthValidator(150), MinLengthValidator(4)])
	blueprint_heavy = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	blade_heavy = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	handle_heavy = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	owned_heavy = models.BooleanField()

	def __str__(self):
		return self.name_heavy

class Dagger(models.Model): # Blade, Handle
	id_dagger = models.AutoField(primary_key=True)
	name_dagger = models.CharField(max_length=50, validators=[MaxLengthValidator(150), MinLengthValidator(4)])
	blueprint_dagger = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	blade_dagger = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	handle_dagger = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	owned_dagger = models.BooleanField()

	def __str__(self):
		return self.name_dagger

class Gunblade(models.Model): # Blade, Handle
	id_gunblade = models.AutoField(primary_key=True)
	name_gunblade = models.CharField(max_length=50, validators=[MaxLengthValidator(150), MinLengthValidator(4)])
	blueprint_gunblade = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	blade_gunblade = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	handle_gunblade = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	owned_gunblade = models.BooleanField()

	def __str__(self):
		return self.name_gunblade

class Scythe(models.Model): # Blade, Handle
	id_scythe = models.AutoField(primary_key=True)
	name_scythe = models.CharField(max_length=50, validators=[MaxLengthValidator(150), MinLengthValidator(4)])
	blueprint_scythe = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	blade_scythe = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	handle_scythe = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	owned_scythe = models.BooleanField()

	def __str__(self):
		return self.name_scythe

class Dual_Swords(models.Model): # 2x Blade, 2x Handle
	id_dual_swords = models.AutoField(primary_key=True)
	name_dual_swords = models.CharField(max_length=50, validators=[MaxLengthValidator(150), MinLengthValidator(4)])
	blueprint_dual_swords = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	blade_dual_swords = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	handle_dual_swords = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	owned_dual_swords = models.BooleanField()

	def __str__(self):
		return self.name_dual_swords

class Dual_Dagger(models.Model): # 2x Blade, 2x Handle
	id_dual_dagger = models.AutoField(primary_key=True)
	name_dual_dagger = models.CharField(max_length=50, validators=[MaxLengthValidator(150), MinLengthValidator(4)])
	blueprint_dual_dagger = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	blade_dual_dagger = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	handle_dual_dagger = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	owned_dual_dagger = models.BooleanField()

	def __str__(self):
		return self.name_dual_dagger

class Tonfa(models.Model): # 2x Blade, 2x Handle
	id_tonfa = models.AutoField(primary_key=True)
	name_tonfa = models.CharField(max_length=50, validators=[MaxLengthValidator(150), MinLengthValidator(4)])
	blueprint_tonfa = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	blade_tonfa = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	handle_tonfa = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	owned_tonfa = models.BooleanField()

	def __str__(self):
		return self.name_tonfa

class Hammer(models.Model): # Head, Handle
	id_hammer = models.AutoField(primary_key=True)
	name_hammer = models.CharField(max_length=50, validators=[MaxLengthValidator(150), MinLengthValidator(4)])
	blueprint_hammer = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	head_hammer = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	handle_hammer = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	owned_hammer = models.BooleanField()

	def __str__(self):
		return self.name_hammer

class Glaive(models.Model): # 2x Blade, Disc
	id_glaive = models.AutoField(primary_key=True)
	name_glaive = models.CharField(max_length=50, validators=[MaxLengthValidator(150), MinLengthValidator(4)])
	blueprint_glaive = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	blade_glaive = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	disc_glaive = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	owned_glaive = models.BooleanField()

	def __str__(self):
		return self.name_glaive

class Sparring(models.Model): # 2x Gauntlet, 2x Boot
	id_sparring = models.AutoField(primary_key=True)
	name_sparring = models.CharField(max_length=50, validators=[MaxLengthValidator(150), MinLengthValidator(4)])
	blueprint_sparring = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	gauntlet_sparring = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	boot_sparring = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	owned_sparring = models.BooleanField()

	def __str__(self):
		return self.name_sparring

class Nikana(models.Model): # Hilt, Blade
	id_nikana = models.AutoField(primary_key=True)
	name_nikana = models.CharField(max_length=50, validators=[MaxLengthValidator(150), MinLengthValidator(4)])
	blueprint_nikana = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	hilt_nikana = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	blade_nikana = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	owned_nikana = models.BooleanField()

	def __str__(self):
		return self.name_nikana

class Nunchaku(models.Model): # 2x Handle, Chain
	id_nunchaku = models.AutoField(primary_key=True)
	name_nunchaku = models.CharField(max_length=50, validators=[MaxLengthValidator(150), MinLengthValidator(4)])
	blueprint_nunchaku = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	handle_nunchaku = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	chain_nunchaku = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	owned_nunchaku = models.BooleanField()

	def __str__(self):
		return self.name_nunchaku

class Polearm(models.Model): # 2x Blade, Handle
	id_polearm = models.AutoField(primary_key=True)
	name_polearm = models.CharField(max_length=50, validators=[MaxLengthValidator(150), MinLengthValidator(4)])
	blueprint_polearm = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	blade_polearm = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	handle_polearm = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	owned_polearm = models.BooleanField()

	def __str__(self):
		return self.name_polearm

class Sword_Shield(models.Model): # Blade, Guard, Hilt
	id_shield = models.AutoField(primary_key=True)
	name_shield = models.CharField(max_length=50, validators=[MaxLengthValidator(150), MinLengthValidator(4)])
	blueprint_shield = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	blade_shield = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	guard_shield = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	hilt_shield = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	owned_shield = models.BooleanField()

	def __str__(self):
		return self.name_shield


################## COMPANION ##################
class Sentinel(models.Model): # Cerebrum, Carapace, Systems
	id_sentinel = models.AutoField(primary_key=True)
	name_sentinel = models.CharField(max_length=50, validators=[MaxLengthValidator(150), MinLengthValidator(4)])
	blueprint_sentinel = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	cerebrum_sentinel = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	carapace_sentinel = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	systems_sentinel = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	owned_sentinel = models.BooleanField()

	def __str__(self):
		return self.name_sentinel

class Collar(models.Model): # Band, Buckle
	id_collar = models.AutoField(primary_key=True)
	name_collar = models.CharField(max_length=50, validators=[MaxLengthValidator(150), MinLengthValidator(4)])
	blueprint_collar = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	band_collar = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	buckle_collar = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	owned_collar = models.BooleanField()

	def __str__(self):
		return self.name_collar


################## ARCHWING ##################
class Archwing(models.Model): # Harness, Wings, Systems
	id_archwing = models.AutoField(primary_key=True)
	name_archwing = models.CharField(max_length=50, validators=[MaxLengthValidator(150), MinLengthValidator(4)])
	blueprint_archwing = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	harness_archwing = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	wings_archwing = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	systems_archwing = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	owned_archwing = models.BooleanField()

	def __str__(self):
		return self.name_archwing


################## WARFRAME ##################
class Warframe(models.Model): # Neuroptics, Chassis, Systems
	id_warframe = models.AutoField(primary_key=True)
	name_warframe = models.CharField(max_length=50, validators=[MaxLengthValidator(150), MinLengthValidator(3)])
	blueprint_warframe = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	neuroptics_warframe = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	chassis_warframe = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	systems_warframe = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(0)])
	owned_warframe = models.BooleanField()

	def __str__(self):
		return self.name_warframe
