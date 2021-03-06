from django.contrib import admin

from .models import Listing


class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published',
                    'price', 'list_date', 'realtor','bedrooms')
    list_display_links = ('id', 'title')
    ordering = ('id',)
    list_filter = ('realtor', 'is_published')
    list_editable = ('is_published', 'price','bedrooms')
    search_fields = ('title', 'description', 'address', 'city')
    list_per_page = 25


admin.site.register(Listing, ListingAdmin)
