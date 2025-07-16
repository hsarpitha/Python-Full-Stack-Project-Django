from django.urls import path, include
from . import views

app_name = 'delivery'
urlpatterns = [
    path('',views.index, name = 'index'),
    path('signin/',views.sign_in, name = 'sign_in'),
    path('signup/',views.sign_up, name = 'sign_up'),
    path('handle_signin/',views.handle_signin, name = 'handle_signin'),
    path('add_res/', views.add_res, name = 'add_res'),
    path('handle_signup/',views.handle_signup, name = 'handle_signup'),
    path('display_res/',views.display_res, name = 'display_res'),
    path('view_menu/<int:id>/', views.view_menu, name = 'view_menu'),
    path('add_menu/<int:id>/', views.add_menu, name = 'add_menu'),
    path('delete_menu/<int:id>/', views.delete_menu, name = 'delete_menu'),
    path('cusdisplay_res/<str:username>/', views.cusdisplay_res, name = 'cusdisplay_res'),
    path('cusmenu/<int:id>/<str:username>/', views.cusmenu, name = 'cusmenu'),
    path('update_res/<int:id>/', views.update_res, name = 'update_res'),
    path('delete_res/<int:id>/', views.delete_res, name = 'delete_res'),
    path('show_cart/<str:username>/', views.show_cart, name = 'show_cart'),
    path('add_to_cart/<int:menuid>/<str:username>/',views.add_to_cart, name = 'add_to_cart'),
    path('checkout/<str:username>/', views.checkout, name = 'checkout'),
    path('orders/<str:username>/',views.orders, name = 'orders'),
]