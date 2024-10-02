from django.urls import path

from users.views import UserList, UserDetails

urlpatterns = [
    path('', UserList.as_view()),
    path('<int:pk>', UserDetails.as_view())
]