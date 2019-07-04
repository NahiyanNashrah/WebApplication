# Generated by Django 2.2.2 on 2019-07-04 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crudApplication', '0012_physicaltest'),
    ]

    operations = [
        migrations.CreateModel(
            name='BloodDonationHistory',
            fields=[
                ('reg_no', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='crudApplication.Donor')),
                ('blood_donate_before_boolean', models.BooleanField()),
                ('gap_of_blood_donation', models.CharField(max_length=20)),
                ('is_recipient_relative', models.BooleanField()),
                ('patient_name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'blood_Donation_History',
            },
        ),
        migrations.AlterField(
            model_name='physicaltest',
            name='bp',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='physicaltest',
            name='pulse',
            field=models.CharField(max_length=10),
        ),
    ]