# Generated by Django 2.2.2 on 2019-07-01 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Livraison',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idop', models.IntegerField()),
                ('dataclient', models.TextField(max_length=1000)),
                ('time', models.TextField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='OtherPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idop', models.IntegerField()),
                ('address', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('idc', models.IntegerField()),
                ('idsc', models.IntegerField()),
                ('address', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=500)),
                ('prix', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SousCategories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('idc', models.IntegerField()),
            ],
        ),
        migrations.RenameModel(
            old_name='Movie',
            new_name='Categories',
        ),
    ]
