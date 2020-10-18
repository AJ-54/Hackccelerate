from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from courses.views import CourseListView, home_view

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('course/', include('courses.urls')),
    path('', home_view, name='home'),
    path('students/', include('students.urls')),
    path('accounts/', include('accounts.urls')),
    path('api/', include('courses.api.urls', namespace='api')),
    path('chat/', include('chat.urls', namespace='chat')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
