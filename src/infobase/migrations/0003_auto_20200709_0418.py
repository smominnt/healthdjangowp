# Generated by Django 3.0.8 on 2020-07-09 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infobase', '0002_auto_20200709_0412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]