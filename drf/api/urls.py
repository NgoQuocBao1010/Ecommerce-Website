from django.urls import path
from . import views

urlpatterns = [
    # path('', views.api, name='home'),
    path('all-shoes/', views.shoeList, name='shoeList'),
    path('shoes/<str:brandName>', views.shoesByBrand, name='shoeBrand'),
    path('shoe-detail/<str:id>', views.shoeDetail, name='shoeDetail'),
    # path('task-update/<str:id>', views.taskUpdate, name='taskUpdate'),
    # path('task-delete/<str:id>', views.taskDelete, name='taskDelete'),
    # path('task-create', views.taskCreate, name='taskCreate'),
]