"""foodgram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""





from django.contrib import admin
from django.urls import path
from users.views import index, user_login, change_password, cart, follows, favourites, logout, user_create
from cart.views import cart_detail, PurchasesView
from recipes import views
from ingredients.views import Ingredients
from django.conf.urls.static import static
from django.conf import settings
from django.urls import include
from ingredients.views import data_upl


urlpatterns = [
    path('cart/', include('cart.urls', namespace='cart')),
    # path('purchases', purchases, name='purchases'),
    # path('purchases/<int:id>', purchases, name='purchases_del'),
    path('ingredients/', Ingredients.as_view(), name='ingredients'),
    path('purchases/', PurchasesView.as_view(), name='purchases'),
    path('purchases/<int:id>/', PurchasesView.as_view(), name='purchases_add'),
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('recipes/<int:id>', views.recipe_detail, name='recipe_detail'),
    path('login/', user_login, name='login'),
    path('user_create/', user_create, name='user_create'),
    path('change_password/', change_password, name='change_password'),
    path('new/', views.new, name='new'),
    path('favourites/', favourites, name='favourites'),
    path('cart/', cart, name='cart'),
    path('follows/', follows, name='follows'),
    path('logout/', logout, name='logout'),
    # path('purchases', views.purchases, name='purchases'),
    path('shoplist', cart_detail, name='shoplist'),
    path('upload/', data_upl, name='data_upl'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns = [
#         path('__debug__/', include(debug_toolbar.urls)),
#     ] + urlpatterns