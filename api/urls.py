from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('onsale-items/', views.onSellItemsList, name="onsale-items"),
    path("searchItem/<str:itemname>", views.filterOnSellItems, name="searchItem"),
    path('onsale-create/', views.onSellItemsCreate, name="onsale-items-detail")
]
