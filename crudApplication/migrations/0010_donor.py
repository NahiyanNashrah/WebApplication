# Generated by Django 2.2.2 on 2019-07-04 05:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crudApplication', '0009_bloodtest_storage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('reg_no', models.IntegerField(max_length=8, primary_key=True, serialize=False)),
                ('blood_group', models.CharField(max_length=5)),
                ('bag_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='crudApplication.Storage')),
            ],
            options={
                'db_table': 'donor',
            },
        ),
    ]
