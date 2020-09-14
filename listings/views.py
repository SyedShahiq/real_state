from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render

from listings.choices import bedroom_choices, price_choices, state_choices

from .models import Listing


def index(request):
    listings = Listing.objects.all().order_by(
        '-list_date').filter(is_published=True)
    paginator = Paginator(listings, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'listings': page_obj
    }
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {
        'listing': listing,
    }
    return render(request, 'listings/listing.html', context)


def search(request):
    context = {
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'state_choices': state_choices
    }
    return render(request, 'listings/search.html',context)
