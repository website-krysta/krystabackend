# Generated by Django 4.1.7 on 2023-03-18 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('krysta_app', '0002_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Password',
            field=models.CharField(max_length=25),
        ),
    ]
