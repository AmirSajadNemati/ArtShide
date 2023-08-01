from django.urls import path

from order import views

urlpatterns = [
    path('add-to-order', views.add_course_to_order, name='add-product-to-order')
]