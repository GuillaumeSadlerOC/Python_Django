from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .forms import SearchForm
from .models import Product

from substitutes.scripts.relevant_products import RelevantProducts
from substitutes.scripts.comparative_products import ComparativeProducts

import re
import json


def index(request):

    form = SearchForm(request.POST or None)

    if form.is_valid():
        research = form.cleaned_data['research']

    return render(request, 'substitutes/index.html', locals())


def results(request, name=None):
    """
    Search in database all products whose name matches with keyword(s)
    entered by user.
    """

    if name is not None:
        user_keywords = name
    elif request.method == 'POST':
        user_keywords = request.POST.get("product-name")
    else:
        user_keywords = request.GET.get('name')

    # Remove all space to keyword end
    search = re.sub(r"( )+$", "", user_keywords)
    # Remove all space to keyword start
    search = re.sub(r"^( )+", "", search)

    product_list = Product.objects.filter(name__icontains=search)

    paginator = Paginator(product_list, 6)

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        products = paginator.page(page)
    except (EmptyPage, InvalidPage):
        products = paginator.page(paginator.num_pages)

    return render(request, 'substitutes/result.html', {
        'products': products,
        'title': search
        })


@login_required(login_url='/login/')
def favorites(request):

    favorites_list = request.user.profile.favorites.all()

    paginator = Paginator(favorites_list, 6)

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        products = paginator.page(page)
    except (EmptyPage, InvalidPage):
        products = paginator.page(paginator.num_pages)

    return render(request, 'substitutes/result.html', {
        'products': products,
        'title': 'Vos favoris'})


@login_required(login_url='/login/')
def add_favorite(request, id):

    profile = request.user.profile
    product = Product.objects.get(id=id)
    profile.favorites.add(product)

    return favorites(request)


@login_required(login_url='/login/')
def del_favorite(request, id):

    product = Product.objects.get(id=id)

    request.user.profile.favorites.remove(product)

    return favorites(request)


def substitutes(request, id):
    """
    Search in database the products substituable to the reference
    product.
    """

    # Get relevant products for comparison
    new_relevant_products = RelevantProducts(
        ref_product_id=id,
        relevant_level="5,4,3"
    )
    relevant_products = new_relevant_products.get_relevant_products()
    reference = new_relevant_products.ref_product

    # Start the comparise with relevant products and reference product
    comparate_products = ComparativeProducts()
    substitutes = comparate_products.get_substitutes(
        reference=reference,
        sample=relevant_products
    )

    paginator = Paginator(substitutes, 5)

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        products = paginator.page(page)
    except (EmptyPage, InvalidPage):
        products = paginator.page(paginator.num_pages)

    return render(
        request, 'substitutes/sub_result.html', {
            'ref_product': reference,
            'products': products,
            'title': reference.name
        }
    )


def legales_notices(request):
    return render(request, 'substitutes/legales_notices.html')


def product(request, id):

    # Get product
    product = Product.objects.get(id=id)
    nutriments = json.loads(product.nutriments)
    saturated_fat = nutriments["saturated-fat"]
    ingredients = json.loads(product.ingredients)

    # Get relevant products for comparison
    new_relevant_products = RelevantProducts(
        ref_product_id=product.id,
        relevant_level="5,4,3"
    )
    relevant_products = new_relevant_products.get_relevant_products()

    comparate_products = ComparativeProducts()
    averages = comparate_products.get_averages(sample=relevant_products)
    average_saturated_fat = averages["saturated-fat"]

    return render(request, 'substitutes/product.html', {
        'product': product,
        'nutriments': nutriments,
        'ingredients': ingredients,
        'ingredients_nbr': len(ingredients),
        'saturated_fat': saturated_fat,
        'averages': averages,
        'average_saturated_fat':average_saturated_fat
        })
