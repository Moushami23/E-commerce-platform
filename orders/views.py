from django.shortcuts import render, redirect
from cart.models import CartItem
from .models import Order
from store.models import Product

def checkout(request):
    cart = request.session.get('cart', {})
    total = 0
    items = []

    for product_id, quantity in cart.items():
        product = Product.objects.get(id=product_id)
        total += product.price * quantity
        items.append({
            'product': product,
            'quantity': quantity
        })

    if request.method == 'POST':
        request.session['checkout_name'] = request.POST.get('name')
        request.session['checkout_email'] = request.POST.get('email')
        request.session['checkout_address'] = request.POST.get('address')
        request.session['checkout_total'] = float(total)


        return redirect('payment_method')

    return render(request, 'orders/checkout.html', {
        'items': items,
        'total': total
    })

def payment_method(request):
    total = request.session.get('checkout_total')

    if request.method == 'POST':
        method = request.POST.get('payment_method')

        if method == 'cod':
            return redirect('complete_order')

        if method == 'card':
            return redirect('card_payment')

    return render(request, 'orders/payment_method.html', {'total': total})

def card_payment(request):
    total = request.session.get('checkout_total')

    if request.method == 'POST':
        # We won't store real card data (just simulation)
        return redirect('complete_order')

    return render(request, 'orders/card_payment.html', {'total': total})
def complete_order(request):
    name = request.session.get('checkout_name')
    email = request.session.get('checkout_email')
    address = request.session.get('checkout_address')
    total = request.session.get('checkout_total')

    order = Order.objects.create(
        name=name,
        email=email,
        total=total,
        address=address
    )

    # clear cart
    request.session['cart'] = {}

    # remove checkout session values
    request.session.pop('checkout_name', None)
    request.session.pop('checkout_email', None)
    request.session.pop('checkout_address', None)
    request.session.pop('checkout_total', None)

    return redirect('order_success', order_id=order.id)




def order_success(request, order_id):
    order = Order.objects.get(id=order_id)
    return render(request, 'orders/success.html', {'order': order})
