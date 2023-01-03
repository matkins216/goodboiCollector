from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('goodboiz/', views.gb_index, name='index'),
    path('goodboiz/<int:gb_id>/', views.gb_detail, name='detail'),
    path('goodboiz/create/', views.GoodboiCreate.as_view(), name='gb_create'),
    path('goodboiz/<int:pk>/update/', views.GoodboiUpdate.as_view(), name='gb_update'),
   	path('goodboiz/<int:pk>/delete/', views.GoodboiDelete.as_view(), name='gb_delete'),
    path('goodboiz/<int:goodboiz_id>/add_feeding/', views.add_feeding, name='add_feeding'),
]
