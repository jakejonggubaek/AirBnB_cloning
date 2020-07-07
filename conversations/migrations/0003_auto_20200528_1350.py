# Generated by Django 2.2.5 on 2020-05-28 18:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conversations', '0002_auto_20200528_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversation',
            name='participants',
            field=models.ManyToManyField(related_name='conversations', to=settings.AUTH_USER_MODEL),
        ),
    ]
