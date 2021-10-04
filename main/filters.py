import django_filters

from. models import *

class WebsiteCategoryFilter(django_filters.FilterSet):
    class Meta:
        model = Website
        fields = ['category']
