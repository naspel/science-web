from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('field/', views.field, name='field'),
    path('field/mathematics', views.mathematics, name='mathematics'),
    path('field/fisics', views.fisics, name='fisics'),
    path('field/chemistry', views.chemistry),
    path('field/informatics', views.informatics, name='informatics'),
    path('field/history', views.history, name='history'),
    path('shop', views.shop, name='shop'),
]