# Generated by Django 3.1.5 on 2021-01-22 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('In process', 'In process'), ('Delivered', 'Delivered'), ('Not delivered', 'Not delivered')], default='In process', max_length=20),
        ),
    ]
