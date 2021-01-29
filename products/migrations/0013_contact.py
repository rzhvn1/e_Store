# Generated by Django 3.1.5 on 2021-01-29 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_aboutus'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Phone number', 'Phone number'), ('E-mail', 'E-mail'), ('Address', 'Address')], max_length=50)),
                ('client', models.CharField(help_text='Full Name', max_length=100)),
                ('latitude', models.IntegerField(blank=True)),
                ('longtitude', models.IntegerField(blank=True)),
            ],
        ),
    ]
