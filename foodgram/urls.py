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


from cart.views import PurcasesView


from rest_framework.routers import DefaultRouter


titles_router = DefaultRouter()
titles_router.register(r'purchases', DefaultRouter, basename='purchases')


from django.contrib import admin
from django.urls import path
from users.views import index, user_login, change_password, cart, follows, favourites, logout, user_create
from cart.views import cart_detail
from recipes import views
from django.conf.urls.static import static
from django.conf import settings
from django.urls import include
from ingredients.views import data_upl


urlpatterns = [
    path('', include(titles_router.urls)),
    # path('purchases/<int:pk>/', views.PurcasesView.as_view()),
    path('admin/', admin.site.urls),
    path('', index, name='index'),
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