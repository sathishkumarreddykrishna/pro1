# Generated by Django 2.1.7 on 2019-06-06 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='create_account',
            fields=[
                ('first_name', models.CharField(blank=True, max_length=30)),
                ('last_name', models.CharField(blank=True, max_length=30)),
                ('mobile_number', models.IntegerField(blank=True, primary_key=True, serialize=False)),
                ('adders', models.TextField(max_length=300)),
                ('password', models.CharField(max_length=10)),
                ('conform_password', models.CharField(max_length=10)),
            ],
        ),
    ]