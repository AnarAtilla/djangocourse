from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from mypro.views import home  # Правильный импорт
from django.conf import settings  # Импортируйте settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Главная страница
    path('library/', include('library.urls')),
    path('lagerhouse/', include('lagerhouse.urls')),
    path('task_manager/', include('task_manager.urls')),  # Маршруты для task_manager
    path('project_tasks/', include('project_tasks.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api-auth/', include('rest_framework.urls')),  # Добавьте эту строку
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns