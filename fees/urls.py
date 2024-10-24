from django.urls import path
from .views import FeeListView, FeeCreateView,FeeUpdateView,FeeDeleteView

app_name = 'fees'


urlpatterns = [
    path('list/', FeeListView.as_view(), name='fee-list'),
    path('create/', FeeCreateView.as_view(), name='fee-create'),
    path('update/<int:pk>/', FeeUpdateView.as_view(), name='fee-update'),
    path('delete/<int:pk>/', FeeDeleteView.as_view(), name='fee-delete'),
]
