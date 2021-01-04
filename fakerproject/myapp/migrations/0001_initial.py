# Generated by Django 2.2 on 2020-12-02 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('roll', models.IntegerField()),
                ('marks', models.IntegerField()),
                ('dob', models.DateField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
