from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cms.urls')),
    path('ckeditor', include('ckeditor_uploader.urls')),

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # TODO What was this for?


admin.site.site_header = "Pop Culture"
admin.site.site_title = "Pop Culture Shenzhen"
admin.site.index_title = "Welcome to Pop Culture Tutor System"