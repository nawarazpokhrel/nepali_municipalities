# Generated by Django 4.0 on 2022-01-02 15:01

from django.db import migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('municaplities', '0006_rename_uuid_district_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='district',
            name='id',
            field=django_extensions.db.fields.ShortUUIDField(blank=True, editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='municipalities',
            name='id',
            field=django_extensions.db.fields.ShortUUIDField(blank=True, editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='province',
            name='id',
            field=django_extensions.db.fields.ShortUUIDField(blank=True, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]