
from django.contrib import admin
from django.urls import path
from obituaries.views import submit_obituary, view_obituaries

urlpatterns = [
    path('admin/', admin.site.urls),
    path('submit/', submit_obituary, name='submit_obituary'),
    path('', view_obituaries, name='view_obituaries'),
    # Add other URL patterns as needed
]
