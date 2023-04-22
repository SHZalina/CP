from django.shortcuts import render, get_object_or_404, redirect
from .models import Listing
from django.core.paginator import Paginator, EmptyPage
from .choices import price_choices, category_choices, city_choices

def listings(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 9)
    page = request.GET.get('page')
    page_listings = paginator.get_page(page)
    context = {
        'listings': page_listings
    }  
    return render(request, 'listings/listings.html', context)

def listing(request, pk):
    listing = get_object_or_404(Listing, pk=pk)
    context = {
        'listing': listing
    } 
    return render(request, 'listings/listing.html', context)

def search(request):
    query_set = Listing.objects.order_by('-list_date')
    
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            query_set = query_set.filter(description__icontains=keywords)
    if 'breed' in request.GET:
        breed = request.GET['breed']
        if breed:
            query_set = query_set.filter(breed__iexact=breed)
    if 'category' in request.GET:
        category = request.GET['category']
        if category:
            query_set = query_set.filter(category__iexact=category)
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            query_set = query_set.filter(city__iexact=city)
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            query_set = query_set.filter(price__lte=price)
    context = {
        'query_set': query_set,
        'price_choices': price_choices,
        'city_choices': city_choices,
        'category_choices': category_choices,
        'values': request.GET
    }
    return render(request, 'listings/search.html', context)
    