from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import *


urlpatterns = [
    # path('auth/', include('djoser.urls')),
    path('register/', RegisterUserView.as_view()),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('profiles/', ProfileListView.as_view()),
    path('profiles/update/', ProfileUpdateView.as_view()),
    path('profiles/listcontent/', AddContentListView.as_view()),
    path('profiles/addcontent/', AddContentCreateView.as_view()),
    path('profiles/updategeo/', UpdateLocation.as_view()),
    path('profiles/addlike/', CreateLikeView.as_view()),
]