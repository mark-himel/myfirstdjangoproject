from django.urls import  path, include
from . import views
from rest_framework import routers

app_name = 'merchants'
# router = routers.DefaultRouter()
# router.register('merchants', views.MerchantView)
urlpatterns = [
    # ex: /merchants/
    path('merchants/', views.IndexView.as_view(), name='index'),
    # ex: /merchants/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    # path('', include(router.urls))
]
