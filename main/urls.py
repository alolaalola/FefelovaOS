from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static
import os

urlpatterns = [
    path('', views.index, name='index'),
    path('services/', views.services, name='services'),
    path('contacts/', views.contacts, name='contacts'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('news/', views.news, name='news'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('profile/', views.profile_view, name='profile'),
    path('sitemap/', views.sitemap, name='sitemap'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=os.path.join(settings.BASE_DIR, 'main', 'static'))
