#handle url Routing

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/notes/', include('notes.urls')),
    path('api/task/', include('task.urls')),
]
