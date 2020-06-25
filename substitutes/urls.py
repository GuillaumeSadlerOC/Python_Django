from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='searchindex'),
    path('results/', views.results, name='results'),
    path('product/', views.product, name='product'),
    path('substitutes/', views.substitutes, name='substitutes'),
]
