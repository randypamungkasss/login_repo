from django.urls import path
from .views import index_view, detail_view, IndexView, DetailView, DeleteView

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('todos/<str:id>/', DetailView.as_view(), name="detail-view"),
    path('todos/<str:id>/delete/', DeleteView.as_view(), name="delete"),
]