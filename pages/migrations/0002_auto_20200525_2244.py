# Generated by Django 3.0.6 on 2020-05-25 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='designation',
            field=models.CharField(max_length=50),
        ),
    ]