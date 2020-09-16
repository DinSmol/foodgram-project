from django.contrib import admin
from django.urls import path
from users.views import index, user_login, change_password, cart, follows, logout, user_create, user_profile
from cart.views import cart_detail, PurchasesView
from recipes import views
from ingredients.views import Ingredients
from django.conf.urls.static import static
from django.conf import settings
from django.urls import include
from ingredients.views import data_upl



urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('login/', user_login, name='login'),
    path('logout/', logout, name='logout'),
    path('user_create/', user_create, name='user_create'),
    path('users/<int:id>/', user_profile, name='user_profile'),
    path('change_password/', change_password, name='change_password'),

    path('cart/', include('cart.urls', namespace='cart')),

    path('ingredients/', Ingredients.as_view(), name='ingredients'),
    path('purchases/', PurchasesView.as_view(), name='purchases'),
    path('purchases/<int:id>/', PurchasesView.as_view(), name='purchases_add'),

    path('subscriptions', views.SubscriptionsView.as_view(), name='subscriptions_add'),
    path('subscriptions/<int:id>/', views.SubscriptionsView.as_view(), name='subscriptions_delete'),

    
    path('recipes/<int:id>', views.recipe_detail, name='recipe_detail'),
    path('recipes/<int:id>/edit', views.recipe_change, name='recipe_change'),
    path('recipes/<int:id>/terminate', views.recipe_delete, name='recipe_delete'),
    path('new/', views.new, name='new'),

    
    
    
    
    path('favourites/', views.favourites, name='favourites'),
    path('favorites/<int:id>', views.FavouritesView.as_view(), name='favorites'),
    
    
    
    # path('cart/', cart, name='cart'),
    path('follows/', follows, name='follows'),
    
    # path('purchases', views.purchases, name='purchases'),
    path('shoplist', cart_detail, name='shoplist'),
    path('upload/', data_upl, name='data_upl'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns = [
#         path('__debug__/', include(debug_toolbar.urls)),
#     ] + urlpatterns