# Generated by Django 3.1.4 on 2021-01-15 00:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('primary', '0005_auto_20210114_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bow',
            name='owner',
            field=models.ForeignKey(default='LethalisUmbra', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='rifle',
            name='owner',
            field=models.ForeignKey(default='LethalisUmbra', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='shotgun',
            name='owner',
            field=models.ForeignKey(default='LethalisUmbra', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='sniper',
            name='owner',
            field=models.ForeignKey(default='LethalisUmbra', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='zhuge',
            name='owner',
            field=models.ForeignKey(default='LethalisUmbra', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
