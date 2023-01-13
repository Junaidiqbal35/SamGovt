from django.urls import path
from . import views

urlpatterns = [
    # path('', views.search_data, name='search'),
    path('', views.sam_govt_search_form, name='search-form')
]
