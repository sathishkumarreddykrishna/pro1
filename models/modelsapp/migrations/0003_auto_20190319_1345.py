# Generated by Django 2.1.7 on 2019-03-19 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelsapp', '0002_auto_20190227_1609'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('marks', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='student',
        ),
    ]
