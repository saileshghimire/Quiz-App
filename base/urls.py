from django.urls import path
from base import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index, name='index'),
    path('addQuestion/', views.addQuestion,name='addQuestion'),
    path('login/', views.loginPage,name='login'),
    path('logout/', views.logoutPage,name='logout'),
    path('register/', views.registerPage,name='register'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)