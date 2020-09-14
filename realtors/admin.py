import datetime

from django.contrib import admin

from .models import Realtor


class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'email', 'get_hire_date')
    list_display_links = ('id', 'name')
    ordering = ('id',)

    def get_hire_date(self, obj):
        date = obj.hire_date.strftime("%d %b %Y ")
        return date
    get_hire_date.short_description = 'Hire Date'

admin.site.register(Realtor, RealtorAdmin)
