# Generated by Django 3.1.2 on 2020-11-11 08:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('phone', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('image', stdimage.models.StdImageField(blank=True, null=True, upload_to='media/images/customer_images/')),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zip_code', models.CharField(max_length=50)),
                ('area', models.CharField(max_length=50, null=True)),
                ('street', models.CharField(max_length=50, null=True)),
                ('house_number', models.CharField(max_length=50, null=True)),
                ('flat_number', models.CharField(max_length=50, null=True)),
                ('floor_number', models.CharField(max_length=50, null=True)),
                ('city', models.CharField(max_length=50)),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_address', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
