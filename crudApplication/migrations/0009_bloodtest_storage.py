# Generated by Django 2.2.2 on 2019-07-04 04:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crudApplication', '0008_charge'),
    ]

    operations = [
        migrations.CreateModel(
            name='BloodTest',
            fields=[
                ('blood_id', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('HCV', models.BooleanField()),
                ('HIV', models.BooleanField()),
                ('HBsAg', models.BooleanField()),
                ('Syphilis', models.BooleanField()),
                ('MP', models.BooleanField()),
            ],
            options={
                'db_table': 'blood_test',
            },
        ),
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('bag_id', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('blood_group', models.CharField(max_length=5)),
                ('rh_type', models.CharField(max_length=5)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('stored_date', models.DateField()),
                ('expired_date', models.DateField()),
                ('blood_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='crudApplication.BloodTest')),
            ],
            options={
                'db_table': 'storage',
            },
        ),
    ]
