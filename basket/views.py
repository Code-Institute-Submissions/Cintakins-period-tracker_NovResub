from django.shortcuts import render, redirect

# Create your views here.

def view_basket(request):
    """ returns bag content view """

    return render(request, 'basket/basket.html')

def add_to_basket(request, item_id):
    """ adds items to basket """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    basket = request.session.get('basket', {})
    if 'product_size' in request.POST:
        size = request.session.POST['product_size']
# help from boutique-ado project
    if size:
        if item_id in list(basket.keys()):
            if size in basket[item_id]['item_size'].keys():
                basket[item_id]['item_size'][size] += quantity
            else:
                basket[item_id]['item_size'][size] = quantity
        else:
            basket[item_id] = {'item_size': {size: quantity}}
    else:
        if item_id in list(basket.keys()):
            basket[item_id] += quantity
        else:
            basket[item_id] = quantity
        
    request.session['basket'] = basket
    return redirect(redirect_url)