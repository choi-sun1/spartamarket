from django.db import models
from django.conf import settings

class Product(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="products")
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="like_product"
    )


    def __str__(self):
        return self.title