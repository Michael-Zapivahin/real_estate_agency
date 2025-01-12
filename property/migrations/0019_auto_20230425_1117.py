# Generated by Django 2.2.24 on 2023-04-25 08:17

from django.db import migrations


def load_flats(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    for flat in Flat.objects.all().iterator():
        owner, created = Owner.objects.get_or_create(name=flat.owner, pure_phone=flat.owner_pure_phone)
        owner.flats.set([flat])
        owner.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0018_auto_20230425_1033'),
    ]

    operations = [
        migrations.RunPython(load_flats)
    ]
