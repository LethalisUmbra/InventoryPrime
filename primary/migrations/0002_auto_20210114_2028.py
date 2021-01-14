# Generated by Django 3.1.4 on 2021-01-14 23:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primary', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bow',
            old_name='owned_sniper',
            new_name='owned_bow',
        ),
        migrations.AddField(
            model_name='bow',
            name='user_bow',
            field=models.CharField(default=False, max_length=150, validators=[django.core.validators.MaxLengthValidator(150), django.core.validators.MinLengthValidator(4)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rifle',
            name='user_rifle',
            field=models.CharField(default=False, max_length=150, validators=[django.core.validators.MaxLengthValidator(150), django.core.validators.MinLengthValidator(4)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shotgun',
            name='user_shotgun',
            field=models.CharField(default=False, max_length=150, validators=[django.core.validators.MaxLengthValidator(150), django.core.validators.MinLengthValidator(4)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sniper',
            name='user_sniper',
            field=models.CharField(default=False, max_length=150, validators=[django.core.validators.MaxLengthValidator(150), django.core.validators.MinLengthValidator(4)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='zhuge',
            name='user_zhuge',
            field=models.CharField(default=False, max_length=150, validators=[django.core.validators.MaxLengthValidator(150), django.core.validators.MinLengthValidator(4)]),
            preserve_default=False,
        ),
    ]
