# Generated by Django 2.0.6 on 2018-08-23 08:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0012_auto_20180823_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_form1',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
