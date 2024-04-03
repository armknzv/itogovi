from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),

    # add App urls patterns
    path('', include('App.urls')),

    path("", include("Account.urls")),              # our application
]