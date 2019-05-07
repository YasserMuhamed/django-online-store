from django.shortcuts import render,redirect,get_object_or_404
from django.views.decorators.http import require_POST
from .cart import Cart
from .forms import CartAddProductForm
from shop.models import Product
# Create your views here.


@require_POST
def cart_add(request,product_id):
    cart=Cart(request)
    product=get_object_or_404(Product,id=product_id)
    product_form=CartAddProductForm(request.POST)
    if product_form.is_valid():
        cd=product_form.cleaned_data
        cart.add(product=product,
        quantity=cd['quantity'],
        update_quantity=cd['update'])
        if not cd['update']:
            return redirect('shop:product_list')
        return redirect('cart:cart_detail')

def cart_remove(request,product_id):
    cart=Cart(request)
    product=get_object_or_404(Product,id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart=Cart(request)
    dicty={'name':"yasser"}
    for item in cart:
        item['update_quantity_form']=CartAddProductForm(
        initial={'quantity':item['quantity'],
        'update':True}
        )
    return render(request,
    'cart/cart_detail.html',
    {'cart':cart,'vi':dicty}
    )
