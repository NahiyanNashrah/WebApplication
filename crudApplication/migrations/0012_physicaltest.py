# Generated by Django 2.2.2 on 2019-07-04 09:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crudApplication', '0011_donorinformation'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhysicalTest',
            fields=[
                ('reg_no', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='crudApplication.Donor')),
                ('weight', models.CharField(max_length=5)),
                ('haemoglobin_level', models.CharField(max_length=8)),
                ('bp', models.DecimalField(decimal_places=2, max_digits=8)),
                ('pulse', models.DecimalField(decimal_places=2, max_digits=8)),
                ('temp', models.CharField(max_length=5)),
                ('heart', models.CharField(max_length=8)),
                ('lungs', models.CharField(max_length=8)),
                ('others', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'physical_test',
            },
        ),
    ]
