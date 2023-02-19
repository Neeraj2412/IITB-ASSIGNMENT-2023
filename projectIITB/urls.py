
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from allApps.userAccounts import views
from allApps.blogs import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('allApps.userAccounts.urls')),
    path('blogs/', include('allApps.blogs.urls')),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)