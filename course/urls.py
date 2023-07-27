from django.urls import path
from . import views

urlpatterns = [
    path('', views.CourseListView.as_view(), name='course-list'),
    # path('cat/<cat>', views.ProductListView.as_view(), name='product-list-by-categories'),
    path('<slug:slug>', views.CourseDetailView.as_view(), name='course-detail'),
]
