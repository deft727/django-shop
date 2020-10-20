from django.urls import path
from .views import test_view,ProductDetailView,CategotyDetailView



urlpatterns = [

    path('',test_view,name='index'),
    path('products/<str:ct_model>/<str:slug>/',ProductDetailView.as_view(),name='product_detail'),
    path('category/<str:slug>/',CategotyDetailView.as_view(), name='category_detail')

]