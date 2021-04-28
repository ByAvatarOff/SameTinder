from django.urls import path, include
from chat.api.views import ChatListView

urlpatterns = [
    path('', ChatListView.as_view())
]