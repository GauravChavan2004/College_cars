from django.urls import path
from users import views
from django.conf import settings
from django.conf.urls.static import static

app_name= 'users_url'
urlpatterns = [
    path('user_register/', views.user_register, name='user_register'),
    path('user_login/', views.user_login, name='user_login'),
    path('user_logout/', views.user_logout, name='user_logout'), 
]

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)