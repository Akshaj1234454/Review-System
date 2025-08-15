
from django.shortcuts import render, redirect
from reviewDetailed.models import Product, Review
import math
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def avg(product_id):
    temp = 0
    try:
        for i in product_id:
            temp += i
        return temp / len(product_id)
    except ZeroDivisionError:
        return "Error: No ratings available"

def LogOut(request):
    logout(request)
    return redirect("SignUp")

@login_required(login_url='/SignLogIN_OUT/')
def index(request):
    products = Product.objects.all()
    ratings = Review.objects.values("rating")
    ratList = []
    for i in ratings:
        ratList.append(i["rating"])
    avgRating = math.floor(avg(ratList))
    
    context = {
        'products': products,
        'viewOnly': True,
    }
    return render(request, 'index.html', context)
