# Generated by Django 3.2.8 on 2022-09-14 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_biodata_jabatan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biodata',
            name='alamat',
            field=models.TextField(max_length=200, null=b'I01\n'),
        ),
    ]
