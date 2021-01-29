#здесь хранятся наши таблица в базе данных
from django.db import models

# Create your models here.
class Product(models.Model):
    choice = (
        ('Computer', 'Computer'),
        ('Laptop', 'Laptop'),
        ('Phone', 'Phone'),
        ('Monitor', 'Monitor'),
        ('SSD', 'SSD'),
        ('Mouse', 'Mouse'),
        ('Keyboard', 'Keyboard'),
        ('Graphic card', 'Graphic card'),
        ('Cooler', 'Cooler'),
        ('System block', 'System block')
    )
    image = models.ImageField(blank=True, null=True, default='default_product.png')
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    type = models.CharField(choices=choice, max_length=50)
    price = models.IntegerField()

    def __str__(self):
        return f"{self.name} {self.type} {self.price}"

class Order(models.Model):
    statuses = (
        ('In process', 'In process'),
        ('Delivered', 'Delivered'),
        ('Not delivered', 'Not delivered')
    )
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=1)
    status = models.CharField(max_length=20, choices=statuses, default='In process')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product}"

class AboutUs(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()

class Contact(models.Model):
    choice = (
        ('Phone number', 'Phone number'),
        ('E-mail', 'E-mail'),
        ('Address', 'Address')
    )
    type = models.CharField(choices=choice, max_length=50)
    manager = models.CharField(max_length=100, help_text='Full Name')
    latitude = models.IntegerField(blank=True)
    longtitude = models.IntegerField(blank=True)

    def __str__(self):
        return f"{self.manager}"








