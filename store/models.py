from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Game(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, related_name='games', on_delete=models.CASCADE)
    cover_image = models.ImageField(upload_to='covers/')

    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS_CHOICES = [
        ('received', 'Received'),
        ('in_delivery', 'In-delivery'),
        ('delivered', 'Delivered'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='store_orders')
    game = models.ForeignKey('Game', on_delete=models.CASCADE, related_name='store_orders')
    phone = models.CharField(max_length=15)
    address = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='received')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"
