from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from account.views import loginApi, register, getProfile, updateProfile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),
    path('', include('api.urls')),

    path('api/login', loginApi, name='login'),
    path('api/register', register, name='register'),
    path('api/profile', getProfile, name='profile'),
    path('api/update-profile', updateProfile, name='updateProfile'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
