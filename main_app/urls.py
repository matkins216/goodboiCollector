from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('goodboiz/', views.gb_index, name='index'),
    path('goodboiz/<int:gb_id>/', views.gb_detail, name='detail'),
    path('goodboiz/create/', views.GoodboiCreate.as_view(), name='gb_create'),
    path('goodboiz/<int:pk>/update/',
         views.GoodboiUpdate.as_view(), name='gb_update'),
    path('goodboiz/<int:pk>/delete/',
         views.GoodboiDelete.as_view(), name='gb_delete'),
    path('goodboiz/<int:goodboiz_id>/add_feeding/',
         views.add_feeding, name='add_feeding'),
    path('goodboiz/<int:gb_id>/assoc_toy/<int:toy_id>/',
         views.assoc_toy, name='assoc_toy'),
    path('toys/', views.ToyList.as_view(), name='toys_index'),
    path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
    path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
    path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
    path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),
]
