from django.urls import path

from . import views

urlpatterns = [
    path('dashboard', views.UserPanelDashboardPage.as_view(), name='user_panel_dashboard'),
    #path('change-pass', views.ChangePasswordPage.as_view(), name='change_password_page'),
    path('edit-profile', views.EditUserProfilePage.as_view(), name='edit-profile-page'),
    # path('cart', views.user_cart, name='user_cart'),
    # path('remove-order-detail', views.remove_order_detail, name='remove_order_detail_ajax'),
    # path('change-order-detail', views.change_order_detail_count, name='change_order_detail_coutn_ajax'),


]
