# Generated by Django 3.0.4 on 2020-03-26 15:58

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_auto_20200326_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='summary',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
