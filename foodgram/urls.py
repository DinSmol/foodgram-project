from cart.views import PurchasesView, cart_detail
from django.conf import settings
from django.conf.urls import handler404
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.flatpages import views as flatpages_views
from django.urls import include, path
from ingredients.views import Ingredients
from recipes import views
from users.views import follows, index, user_profile

handler404 = 'recipes.views.handler404'


urlpatterns = [
	
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path("auth/", include("users.urls")),
    path("auth/", include("django.contrib.auth.urls")),
    path('users/<int:id>/', user_profile, name='user_profile'),

    path('cart/', include('cart.urls', namespace='cart')),

    path('recipes/', include('recipes.urls', namespace='recipes')),

    path('ingredients/', Ingredients.as_view(), name='ingredients'),

    path('purchases/', PurchasesView.as_view(), name='purchases'),
    path('purchases/<int:id>/', PurchasesView.as_view(), name='purchases_add'),

    path(
        'subscriptions',
        views.SubscriptionsView.as_view(),
        name='subscriptions_add'
    ),
    path(
        'subscriptions/<int:id>/',
        views.SubscriptionsView.as_view(),
        name='subscriptions_delete'
    ),

    path('favourites/', views.FavouritesView.as_view(), name='favourites'),
    path(
        'favorites/<int:id>',
        views.FavouritesView.as_view(),
        name='favorites'
    ),

    path('new/', views.new, name='new'),

    path('follows/', follows, name='follows'),

    path('shoplist', cart_detail, name='shoplist'),
    ]

urlpatterns += [
    path(
        'about-us/',
        flatpages_views.flatpage,
        {'url': 'about-us/'}, name='about'
    ),
    path(
        'about-author/',
        flatpages_views.flatpage,
        {'url': 'about-author/'},
        name='author'
    ),
    path(
        'about-spec/',
        flatpages_views.flatpage,
        {'url': 'about-spec/'}, name='spec'
    ),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
    )
