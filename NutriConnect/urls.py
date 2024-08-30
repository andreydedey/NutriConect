from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='users/login', permanent=False)),  # Redireciona a URL raiz para 'users/'
    path('admin/', admin.site.urls),
    path('users/', include("Users.urls")),
    path('home/', include("home.urls")),
]
