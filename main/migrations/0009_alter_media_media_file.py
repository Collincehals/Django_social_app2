# Generated by Django 4.2.6 on 2023-11-07 15:38

from django.db import migrations, models
import main.validators


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_media_delete_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='media_file',
            field=models.FileField(blank=True, null=True, upload_to='mediafiles', validators=[main.validators.file_size]),
        ),
    ]
