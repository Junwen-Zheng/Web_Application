# Generated by Django 4.1 on 2022-09-05 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server_functions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='athlete',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]