# Generated by Django 4.1.2 on 2023-05-30 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('krysta_app', '0054_alter_productiondamage_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productiondamage',
            name='ID',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='production_damage', to='krysta_app.production'),
        ),
    ]
