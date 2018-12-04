'''
home
about
services
store
contact
blog
sample
'''
from django.contrib import admin
from django.urls import path, include
from django.conf import settings


urlpatterns = [
    #Path del admin
    path('admin/', admin.site.urls),
    #Path del core
    path('', include('core.urls')),
    #Path de los servicios
    path('services/', include('services.urls')),
    #Path del blog
    path('blog/', include('blog.urls')),
    #Path de las paginas de politicas
    path('page/', include('pages.urls')),

]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)