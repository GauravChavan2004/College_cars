from django.urls import path
from core import views
from django.conf import settings
from django.conf.urls.static import static

app_name= 'core_url'
urlpatterns = [
    path('',views.index ),
    
] 
if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)