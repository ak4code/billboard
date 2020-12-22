from django.urls import path
from .views import HomeView, CabinetView, SignUpView, ActivateView

app_name = 'core'

urlpatterns = [
    path('cabinet/', CabinetView.as_view(), name='cabinet'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('activate/<uidb64>/<token>/', ActivateView.as_view(), name='activate'),
    path('', HomeView.as_view(), name='home'),
]
