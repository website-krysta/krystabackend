# Generated by Django 4.1.2 on 2023-04-18 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('krysta_app', '0024_invoice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addrawmaterial',
            name='Id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
