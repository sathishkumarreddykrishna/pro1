# Generated by Django 2.1.7 on 2019-07-11 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tempapp', '0002_auto_20190711_1941'),
    ]

    operations = [
        migrations.CreateModel(
            name='mointer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mname', models.CharField(max_length=20)),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tempapp.student')),
            ],
        ),
    ]