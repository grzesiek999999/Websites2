from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Website, WebPage, WebsiteCategory
from .filters import WebsiteCategoryFilter
from django.core.paginator import Paginator, EmptyPage


def index(request):
    queryset = Website.objects.all()
    filter = WebsiteCategoryFilter(request.GET, queryset = queryset)
    p = Paginator(queryset, 25)
    page_num = request.GET.get('page', 1)

    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)


    context = {
        "object_list": queryset,
        "filter": filter,
        "items" : page,

    }


    return render(request, "main/list.html", context)

def detail(request, id):

    obj = get_object_or_404(Website, pk = id)

    return render(request, 'main/detail.html' , {'obj':obj})


def sorted_by_rank(request):
    sorted_by_rank = Website.objects.order_by('-alexa_rank')
    filter = WebsiteCategoryFilter(request.GET, queryset=sorted_by_rank)
    p = Paginator(sorted_by_rank, 25)
    page_num = request.GET.get('page', 1)

    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    context = {
        "object_list": sorted_by_rank,
        "filter": filter,
        "items": page,

    }

    return render(request, "main/list.html", context)