from django.urls import path
from . import views

urlpatterns = [
    # path('', views.api, name='home'),
    path('all-shoes/', views.shoeList, name='shoeList'),
    path('shoe-detail/<str:id>', views.shoeDetail, name='shoeDetail'),
]