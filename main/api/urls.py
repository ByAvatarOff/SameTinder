from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from main.api.views import ProfileListView, ProfileUpdateView, AddContentListView,\
    AddContentCreateView, UpdateLocation, CreateLikeView, CreateMessageView, ListMessageView


urlpatterns = [
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('profiles/', ProfileListView.as_view()),
    path('profiles/update/', ProfileUpdateView.as_view()),
    path('profiles/listcontent/', AddContentListView.as_view()),
    path('profiles/addcontent/', AddContentCreateView.as_view()),
    path('profiles/updategeo/', UpdateLocation.as_view()),
    path('profiles/addlike/', CreateLikeView.as_view()),
    path('profiles/writemessage/', CreateMessageView.as_view(), name='message'),
    path('profiles/chat/', ListMessageView.as_view()),
]