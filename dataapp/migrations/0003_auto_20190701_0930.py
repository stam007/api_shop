# Generated by Django 2.2.2 on 2019-07-01 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dataapp', '0002_auto_20190701_0901'),
    ]

    operations = [
        migrations.RenameField(
            model_name='otherphoto',
            old_name='idop',
            new_name='idp',
        ),
        migrations.RemoveField(
            model_name='produit',
            name='idc',
        ),
    ]
