from celery import shared_task
from .models import Product, Review  # or move the function to a utils module
from .utils import generate_review_summary

@shared_task
def update_product_summary(product_id):
    product = Product.objects.get(id=product_id)
    reviews = Review.objects.filter(product=product).values_list('content', flat=True)
    summary = generate_review_summary(list(reviews))
    product.aiOverview = summary
    product.save()