"""
Portfolio URL configuration.

Two includes share the '' prefix: core.urls provides /about/ and /contact/
(exact matches), projects.urls provides / and /project/<slug>/.
"""

from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('', include('projects.urls')),
]

# In development the runserver also serves uploaded screenshots.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
