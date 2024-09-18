from django.urls import path
from .views import LoginView, SignupView

urlpatterns = [
    path("signup/", SignupView.as_view(), name="signup"),
    path('', LoginView.as_view(), name='login'),
    path('login/', LoginView.as_view(), name='login')
]