# Generated by Django 2.2.24 on 2023-04-26 05:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0020_auto_20230426_0828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='flat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='complaints', to='property.Flat', verbose_name='квартира'),
        ),
    ]
