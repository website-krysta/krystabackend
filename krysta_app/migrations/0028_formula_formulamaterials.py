# Generated by Django 4.1.2 on 2023-04-19 05:53

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('krysta_app', '0027_addrawmaterial_invoiceid_packingdetails_invoiceid_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Formula',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('FormulaName', models.CharField(max_length=20)),
                ('TotalMaterialsUsed', models.IntegerField()),
                ('AddedTimeStamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('UpdatedTimeStamp', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='FormulaMaterials',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('Quantity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('AddedTimeStamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('UpdatedTimeStamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('FormulaID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='krysta_app.formula')),
                ('RawMaterialID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='krysta_app.rawmaterial')),
            ],
        ),
    ]