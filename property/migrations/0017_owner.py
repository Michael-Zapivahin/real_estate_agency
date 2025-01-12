# Generated by Django 2.2.24 on 2023-04-25 07:30

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0016_auto_20230425_0935'),
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name='ФИО владельца')),
                ('phonenumber', models.CharField(db_index=True, max_length=20, verbose_name='Номер владельца')),
                ('pure_phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, db_index=True, max_length=128, verbose_name='Нормализованный номер владельца')),
                ('flats', models.ManyToManyField(blank=True, related_name='owners', to='property.Flat', verbose_name='Квартиры в собственности')),
            ],
        ),
    ]
