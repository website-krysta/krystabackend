# Generated by Django 4.1.2 on 2023-04-27 06:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('krysta_app', '0029_alter_formula_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='invoice',
            old_name='ID',
            new_name='InvoiceID',
        ),
    ]