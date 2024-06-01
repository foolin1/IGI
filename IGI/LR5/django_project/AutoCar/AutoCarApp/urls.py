from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('add-review/', views.add_review, name='add_review'),
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('register', views.register, name='register'),
    path('user_cars', views.user_cars, name='user_cars'),
    path('add_car', views.add_car, name='add_car'),
    path('parking_spots', views.parking_spots, name='parking_spots'),
    path('park_auto/<int:spot_number>', views.park_auto, name='park_auto'),
    path('delete_car/<int:car_id>/', views.delete_car, name='delete_car'),
    path('edit_car/<int:car_id>/', views.edit_auto, name='edit_car'),
    path('remove_from_spot/<int:car_id>/', views.remove_from_spot, name='remove_from_spot'),
    path('replenish_balance/<int:car_id>/', views.replenish_balance, name='replenish_balance'),
    path('replenish_user_balance', views.replenish_user_balance, name='replenish_user_balance'),
    path('edit_account/', views.edit_account, name='edit_account'),
    path('sales_statistics/', views.sales_statistics, name='sales_statistics'),
    path('politics', views.politics, name='politics'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

