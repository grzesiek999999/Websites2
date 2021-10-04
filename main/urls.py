from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('<int:id>/', views.detail, name ='detail'),
    path("sorted_by_rank" , views.sorted_by_rank , name='sorted_by_rank')
]