# Generated by Django 3.1.4 on 2021-01-14 23:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bow',
            fields=[
                ('id_bow', models.AutoField(primary_key=True, serialize=False)),
                ('name_bow', models.CharField(max_length=50, validators=[django.core.validators.MaxLengthValidator(150), django.core.validators.MinLengthValidator(4)])),
                ('blueprint_bow', models.IntegerField(validators=[django.core.validators.MaxValueValidator(999), django.core.validators.MinValueValidator(0)])),
                ('upper_bow', models.IntegerField(validators=[django.core.validators.MaxValueValidator(999), django.core.validators.MinValueValidator(0)])),
                ('lower_bow', models.IntegerField(validators=[django.core.validators.MaxValueValidator(999), django.core.validators.MinValueValidator(0)])),
                ('grip_bow', models.IntegerField(validators=[django.core.validators.MaxValueValidator(999), django.core.validators.MinValueValidator(0)])),
                ('string_bow', models.IntegerField(validators=[django.core.validators.MaxValueValidator(999), django.core.validators.MinValueValidator(0)])),
                ('owned_sniper', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Rifle',
            fields=[
                ('id_rifle', models.AutoField(primary_key=True, serialize=False)),
                ('name_rifle', models.CharField(max_length=50, validators=[django.core.validators.MaxLengthValidator(150), django.core.validators.MinLengthValidator(4)])),
                ('blueprint_rifle', models.IntegerField(validators=[django.core.validators.MaxValueValidator(999), django.core.validators.MinValueValidator(0)])),
                ('barrel_rifle', models.IntegerField(validators=[django.core.validators.MaxValueValidator(999), django.core.validators.MinValueValidator(0)])),
                ('receiver_rifle', models.IntegerField(validators=[django.core.validators.MaxValueValidator(999), django.core.validators.MinValueValidator(0)])),
                ('stock_rifle', models.IntegerField(validators=[django.core.validators.MaxValueValidator(999), django.core.validators.MinValueValidator(0)])),
                ('owned_rifle', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Shotgun',
            fields=[
                ('id_shotgun', models.AutoField(primary_key=True, serialize=False)),
                ('name_shotgun', models.CharField(max_length=50, validators=[django.core.validators.MaxLengthValidator(150), django.core.validators.MinLengthValidator(4)])),
                ('blueprint_shotgun', models.IntegerField(validators=[django.core.validators.MaxValueValidator(999), django.core.validators.MinValueValidator(0)])),
                ('barrel_shotgun', models.IntegerField(validators=[django.core.validators.MaxValueValidator(999), django.core.validators.MinValueValidator(0)])),
                ('receiver_shotgun', models.IntegerField(validators=[django.core.validators.MaxValueValidator(999), django.core.validators.MinValueValidator(0)])),
                ('stock_shotgun', models.IntegerField(validators=[django.core.validators.MaxValueValidator(999), django.core.validators.MinValueValidator(0)])),
                ('owned_shotgun', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Sniper',
            fields=[
                ('id_sniper', models.AutoField(primary_key=True, serialize=False)),
                ('name_sniper', models.CharField(max_length=50, validators=[django.core.validators.MaxLengthValidator(150), django.core.validators.MinLengthValidator(4)])),
                ('blueprint_sniper', models.IntegerField(validators=[django.core.validators.MaxValueValidator(999), django.core.validators.MinValueValidator(0)])),
                ('barrel_sniper', models.IntegerField(validators=[django.core.validators.MaxValueValidator(999), django.core.validators.MinValueValidator(0)])),
                ('receiver_sniper', models.IntegerField(validators=[django.core.validators.MaxValueValidator(999), django.core.validators.MinValueValidator(0)])),
                ('stock_sniper', models.IntegerField(validators=[django.core.validators.MaxValueValidator(999), django.core.validators.MinValueValidator(0)])),
                ('owned_sniper', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Zhuge',
            fields=[
                ('id_zhuge', models.AutoField(primary_key=True, serialize=False)),
                ('name_zhuge', models.CharField(max_length=50, validators=[django.core.validators.MaxLengthValidator(150), django.core.validators.MinLengthValidator(4)])),
                ('blueprint_zhuge', models.IntegerField(validators=[django.core.validators.MaxValueValidator(999), django.core.validators.MinValueValidator(0)])),
                ('grip_zhuge', models.IntegerField(validators=[django.core.validators.MaxValueValidator(999), django.core.validators.MinValueValidator(0)])),
                ('string_zhuge', models.IntegerField(validators=[django.core.validators.MaxValueValidator(999), django.core.validators.MinValueValidator(0)])),
                ('barrel_zhuge', models.IntegerField(validators=[django.core.validators.MaxValueValidator(999), django.core.validators.MinValueValidator(0)])),
                ('receiver_zhuge', models.IntegerField(validators=[django.core.validators.MaxValueValidator(999), django.core.validators.MinValueValidator(0)])),
                ('owned_zhuge', models.BooleanField()),
            ],
        ),
    ]
