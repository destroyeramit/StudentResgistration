# Generated by Django 2.0.6 on 2018-08-21 15:48

from django.db import migrations, models
import student.models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0007_auto_20180821_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_form4',
            name='tenth_marksheet',
            field=models.FileField(blank=True, null=True, upload_to=student.models.user_directory_path),
        ),
    ]
