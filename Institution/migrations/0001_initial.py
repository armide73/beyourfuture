# Generated by Django 4.1 on 2022-09-13 17:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('InstitutionName', models.CharField(max_length=100)),
                ('title', models.TextField(blank=True, max_length=100, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('video', models.FileField(blank=True, null=True, upload_to='post_video')),
                ('Discription', models.TextField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='FCreate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nation_Id', models.PositiveIntegerField(max_length=16)),
                ('your_Names', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=50)),
                ('Description', models.TextField(max_length=254)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('NamesHelp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='UsernameForm', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='partnershipsInsitutions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserName', models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.CASCADE, related_name='User_Name', to='Institution.fcreate')),
            ],
        ),
    ]
