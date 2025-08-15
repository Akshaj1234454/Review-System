from django.contrib import admin
from .models import Review, Product # Replace with your model name

admin.site.register(Review)  # Register your model here
admin.site.register(Product)