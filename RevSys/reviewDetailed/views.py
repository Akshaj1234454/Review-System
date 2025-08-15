from django.shortcuts import render, redirect
from .models import Product, Review
from .utils import generate_review_summary
from django.contrib.auth.decorators import login_required
from .forms import ReviewForm
from django.utils import timezone
from django.contrib import messages
import threading

def update_summary_async(product_id):
    product = Product.objects.get(id=product_id)
    reviews = Review.objects.filter(title=product.name).values_list('content', flat=True)
    review_list = list(reviews)
    summary = generate_review_summary(review_list)
    if not summary:
        summary = "No summary available."
    product.aiOverview = summary
    product.save()
    print(f"[AI SUMMARY] Saved summary to product {product_id}")

# Initialize the summarizer (will load once when the module is imported)


# Create your views here.
@login_required(login_url='/SignLogIN_OUT/')
def reviews(request, product_id):
    dat = Product.objects.get(id=product_id)
    prodName = dat.name
    reviews = Review.objects.filter(title=prodName)
    summary = dat.aiOverview
    
    return render(request, 'reviews.html', {
        'reviews': reviews,
        'view_only': True,
        'product': dat,
        'summary': summary,
    })



@login_required(login_url='/SignLogIN_OUT/')
def reviewWrite(request, product_id):
    product = Product.objects.get(id=product_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.title = product.name
            review.author = request.user
            review.created_at = timezone.now()
            review.updated_at = timezone.now()
            review.save()
            # Update product avgRating
            all_ratings = Review.objects.filter(title=product.name).values_list('rating', flat=True)
            if all_ratings:
                avg = sum(all_ratings) / len(all_ratings)
                product.avgRating = round(avg)
                product.save()
            
            threading.Thread(target=update_summary_async, args=(product.id,)).start()
            
            messages.success(request, 'Thanks! Your review was submitted successfully.')
            return redirect('reviews', product_id=product.id)
    else:
        form = ReviewForm()

    return render(request, 'reviewWrite.html', {'product': product, 'form': form})