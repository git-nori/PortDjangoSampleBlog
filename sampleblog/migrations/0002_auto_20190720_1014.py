# Generated by Django 2.2.3 on 2019-07-20 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sampleblog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='gender',
            field=models.BooleanField(blank=True, choices=[(True, 'man'), (False, 'woman')], null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='sampleblog/images'),
        ),
    ]
