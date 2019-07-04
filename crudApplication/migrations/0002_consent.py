# Generated by Django 2.2.2 on 2019-07-02 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudApplication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consent',
            fields=[
                ('reg_no', models.IntegerField(max_length=8, primary_key=True, serialize=False)),
                ('permitted_to_donate', models.BooleanField()),
                ('donor_consent', models.CharField(max_length=20)),
                ('doctor_consent', models.CharField(max_length=20)),
                ('date', models.DateField()),
            ],
            options={
                'db_table': 'Consent',
            },
        ),
    ]
