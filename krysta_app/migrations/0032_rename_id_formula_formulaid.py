# Generated by Django 4.1.2 on 2023-04-29 06:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('krysta_app', '0031_rename_rawmaterialid_formulamaterials_materialid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='formula',
            old_name='ID',
            new_name='FormulaID',
        ),
    ]
