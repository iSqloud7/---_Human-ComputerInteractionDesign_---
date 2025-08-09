from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm
# Create your views here.
def index(request):
    return render(request, 'index.html')

def outofstock(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product=form.save(commit=False)
            product.user = request.user
            product.image=form.cleaned_data['image']
            product.save()
            return redirect('outofstock')
    else:
        form = ProductForm()
    products=Product.objects.filter(quantity=0, category__active=True).all()
    return render(request, 'outofstock.html', {'products': products, 'form': form})
