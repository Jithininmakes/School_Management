from django.urls import path
from .views import HomeView,RegisterView,LoginView,IndexView
from django.contrib.auth.views import LogoutView

app_name = 'accounts'


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('home', HomeView.as_view(), name='home'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),



]
