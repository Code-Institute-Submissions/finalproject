from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from .models import Product, Category, Review
from django.contrib.auth.decorators import login_required
from .forms import ProductReviewForm

# Create your views here.
def get_products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

    
# def show_category(request,hierarchy= None):
#     category_slug = hierarchy.split('/')
#     parent = None
#     root = Category.objects.all()

#     for slug in category_slug[:-1]:
#         parent = root.get(parent=parent, slug = slug)

#     try:
#         instance = Category.objects.get(parent=parent,slug=category_slug[-1])
#     except:
#         instance = get_object_or_404(Product, slug = category_slug[-1])
#         return render(request, "product_detail.html", {'instance':instance})
#     else:
#         return render(request, 'categories.html', {'instance':instance})
    
def show_category(request):
    return render(request,"categories.html", {'nodes':Category.objects.all()})

    
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