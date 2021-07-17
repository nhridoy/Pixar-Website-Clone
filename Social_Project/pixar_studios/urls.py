from django.urls import path
from pixar_studios import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'pixar_studios'

urlpatterns = [
    path('', views.home, name='home'),
    path('disneyplus/', views.disneyplus, name='disneyplus'),
    path('theatrical-shorts/', views.theatricalshorts, name='theatrical-shorts'),
    path('feature-films/', views.featurefilms, name='feature-films'),
    path('theatrical-short/<str:theatrical_id>/', views.theatricalshort, name='theatrical-short'),
    path('registration/', views.registration, name='registration'),
    path('login_page/', views.login_page, name='login_page'),
    path('profile/<str:user_name>/', views.profile_url, name='profile'),
    path('logout_url/', views.logout_url, name='logout_url'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
