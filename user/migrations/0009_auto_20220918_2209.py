# Generated by Django 3.2.8 on 2022-09-18 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_delete_adminuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='biodata',
            name='namabelakang',
            field=models.CharField(max_length=200, null=b'I00\n'),
            preserve_default=b'I00\n',
        ),
        migrations.AddField(
            model_name='biodata',
            name='namadepan',
            field=models.CharField(max_length=200, null=b'I00\n'),
            preserve_default=b'I00\n',
        ),
    ]