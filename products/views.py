from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from .models import Product, Review
from django.contrib.auth.decorators import login_required
from .forms import ProductReviewForm

# Create your views here.
def get_products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

    
def do_search(request):
    products = Product.objects.filter(name__icontains=request.GET['q'])
    return render(request, 'products.html', {'products':products})
    
def product_details(request, id):
    this_product = get_object_or_404(Product, pk=id)
    form = ProductReviewForm()
    return render(request, "product_detail.html", {"product" : this_product, 'form':form})
  


@login_required  
def add_review(request, product_id):
    product= get_object_or_404(Product, pk=product_id)
    
    form = ProductReviewForm(request.POST)
    if form.is_valid():
        review = form.save(commit=False)
        review.author = request.user
        review.product = product
        review.rating = form.cleaned_data.get('rating')
        
        review.save()
        
        return redirect('product_details', product_id)
        
        
