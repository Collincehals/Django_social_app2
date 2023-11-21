# Generated by Django 4.2.6 on 2023-11-06 06:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0003_alter_post_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('middlename', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, default='blank-profile-picture.png', upload_to='profilepics')),
                ('location', models.CharField(max_length=255)),
                ('bio', models.CharField(max_length=255)),
                ('alternate_email', models.EmailField(max_length=255)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]