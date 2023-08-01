from django.urls import path

from . import views

urlpatterns = [
    path('dashboard', views.UserPanelDashboardPage.as_view(), name='user_panel_dashboard'),
    path('change-pass', views.ChangePasswordPage.as_view(), name='change-password-page'),
    path('edit-profile', views.EditUserProfilePage.as_view(), name='edit-profile-page'),
    path('my-courses', views.UserCoursesPage.as_view(), name='user-courses-page'),
    path('my-exams', views.UserExamsPage.as_view(), name='user-exams-page'),
    path('cart', views.user_cart, name='user_cart'),
    path('remove-order-detail', views.remove_order_detail, name='remove_order_detail_ajax'),
]

