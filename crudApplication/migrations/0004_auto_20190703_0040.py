# Generated by Django 2.2.2 on 2019-07-02 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudApplication', '0003_recipient'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='id',
        ),
        migrations.AlterField(
            model_name='employee',
            name='eid',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]
