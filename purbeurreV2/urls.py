"""purbeurreV2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url, include
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.conf import settings

from substitutes import views as sub_views
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # SUBSTITUTES APP
    path('', sub_views.index, name='index'),
    path('results/', sub_views.results, name='results'),
    path('results/<str:name>', sub_views.results, name='results'),
    path('product/<int:id>', sub_views.product, name='product'),
    path('substitutes/<int:id>', sub_views.substitutes, name='substitutes'),
    path('favorites', sub_views.favorites, name='favorites'),
    path('del_favorite/<int:id>', sub_views.del_favorite, name='del_favorite'),
    path('add_favorite/<int:id>', sub_views.add_favorite, name='add_favorite'),
    path(
        'legales_notices/',
        sub_views.legales_notices,
        name='legales_notices'
    ),
    # USERS APP
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path(
        'login/',
        auth_views.LoginView.as_view(template_name='users/login.html'),
        name='login'
    ),
    path(
        'logout/',
        auth_views.LogoutView.as_view(template_name='users/logout.html'),
        name='logout'
    ),
    # SOCIAL AUTH MODULE
    url(r'^auth/', include('social_django.urls', namespace='social')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
