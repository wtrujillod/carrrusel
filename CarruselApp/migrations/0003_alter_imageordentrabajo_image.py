# Generated by Django 3.2.5 on 2021-08-03 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CarruselApp', '0002_imageordentrabajo_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageordentrabajo',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image/%Y/%m'),
        ),
    ]