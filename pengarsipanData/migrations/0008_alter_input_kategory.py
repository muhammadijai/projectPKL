# Generated by Django 3.2.8 on 2022-09-22 02:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pengarsipanData', '0007_delete_profil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='input',
            name='kategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='pengarsipanData.kategori'),
        ),
    ]
