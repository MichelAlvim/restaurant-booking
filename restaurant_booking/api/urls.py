from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views.custom_user import CustomUserDetail
from .views.reservation import ReservationCreate, ReservationList, ReservationDetail

urlpatterns = [
    path('users/<int:pk>/', CustomUserDetail.as_view(), name='user-detail'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('reservations/', ReservationCreate.as_view(), name='reservation-create'),
    path('reservations/list/', ReservationList.as_view(), name='reservation-list'),
    path('reservations/<int:pk>/', ReservationDetail.as_view(), name='reservation-detail'),
]
