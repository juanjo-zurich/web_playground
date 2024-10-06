from django.urls import path
from core.urls import urlpatterns
from .views import SignUpView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name="signup"),
]