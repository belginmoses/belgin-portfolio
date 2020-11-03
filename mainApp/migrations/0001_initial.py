# Generated by Django 3.1.2 on 2020-11-02 08:46

from django.db import migrations, models
import django.db.models.deletion
import mainApp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
                ('rate', mainApp.models.IntegerRangeField()),
                ('about', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.about')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('organization', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('about', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.about')),
            ],
        ),
    ]