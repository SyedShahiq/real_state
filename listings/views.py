from django.shortcuts import render
from .models import Listing
from django.core.paginator import Paginator


def index(request):
    listings = Listing.objects.all()
    paginator = Paginator(listings, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'listings': page_obj
    }
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    return render(request, 'listings/listing.html')


def search(request):
    return render(request, 'listings/search.html')
