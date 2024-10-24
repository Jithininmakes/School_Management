from django.urls import path
from .views import FeeListView, FeeCreateView

app_name = 'fees'


urlpatterns = [
    path('list/', FeeListView.as_view(), name='fee-list'),
    path('create/', FeeCreateView.as_view(), name='fee-create'),
]
