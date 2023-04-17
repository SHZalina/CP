from django.shortcuts import render

from .models import Listing
from django.core.paginator import Paginator, EmptyPage

def listings(request):
    
    # listing = Listing.objects.order_by('-list_date').filter(is_published=True)
    # paginator = Paginator(listings, 9)
    # page = request.GET.get('page')
    # page_listings = paginator.get_page(page)
    
    return render(request, 'listings/listings.html')

def listing(request, pk):
    return render(request, 'listings/listing.html')

def search(request):
    return render(request, 'listings/search.html')
    