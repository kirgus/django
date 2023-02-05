from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path, include

from games.views import landing_page
from users import views

urlpatterns = [

    # ГЛАВНАЯ СТРАНИЦА
    path('', landing_page, name='landing-page'),

    # КАТАЛОГ ИГР
    path('games/', include('games.urls', namespace='games')),

    path('users/', include('users.urls', namespace='users')),

    # АДМИНКА
    path('admin/', admin.site.urls),

    # АУТЕНТИФИКАЦИЯ
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),

    path('logout/', views.logout_view, name='logout'),

    path('register/', views.register, name='register'),

]

# Добавление путей файлов для работы на local
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
