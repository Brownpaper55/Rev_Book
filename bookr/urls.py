"""
URL configuration for bookr project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from reviews import admin
from django.contrib import admin
from django.urls import path, include
import reviews.views
from django.conf import settings
from django.conf.urls.static import static
from bookr.views import profile
import reviews.api_views
from rest_framework.routers import DefaultRouter
import debug_toolbar

router = DefaultRouter()
router.register(r'books',reviews.api_views.BookViewSet)
router.register(r'reviews', reviews.api_views.ReviewViewSet)



urlpatterns = [
    path('api/', include((router.urls, 'api'))),
    path('api/login', reviews.api_views.Login.as_view(), name='login'),
    path('accounts/', include('django.contrib.auth.urls'),name='accounts'),
    path('accounts/profile/', profile, name='profile'),
    path('', reviews.views.index, name='index'),
    path('admin/', admin.site.urls),
    path('books/', reviews.views.book_list, name='book_list'),
    path('books/<int:pk>/', reviews.views.book_detail, name='book_detail'),
    path('book_search/', reviews.views.book_search, name='book_search'),
    path('publishers/<int:pk>/', reviews.views.publisher_edit, name='publisher_edit'),
    path('publishers/new/', reviews.views.publisher_edit, name='publisher_create'),
    path('books/<int:pk>/media/',reviews.views.book_media, name='book_media'),
    path('filter_demo/', include('filter_demo.urls')),
    path('book_management/',include('book_management.urls'))
    
    ]

if settings.DEBUG:
     urlpatterns = [path('__debug__/',include(debug_toolbar.urls)),] + urlpatterns
     urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
