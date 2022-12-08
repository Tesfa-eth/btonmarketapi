from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('onsale-items/', views.onSellItemsList, name="onsale-items"),
    path("searchItem/<str:itemname>", views.filterOnSellItems, name="searchItem"),
    path("category/<str:itemname>", views.onSellItemsCategory, name="categoryItem"),
    path("onsale-item-detail/<str:pk>", views.itemDetail, name="itemDetail"),
    path('onsale-create/', views.onSellItemsCreate, name="onsale-items-detail")
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
