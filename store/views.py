from django.shortcuts import render
from .models import Product, Category

def home(request):
    categories = Category.objects.all()
    products = Product.objects.all()

    category_id = request.GET.get('category')
    query = request.GET.get('q')

    if category_id:
        products = products.filter(category_id=category_id)

    if query:
        products = products.filter(name__icontains=query)

    context = {
        'products': products,
        'categories': categories
    }

    return render(request, 'store/home.html', context)
