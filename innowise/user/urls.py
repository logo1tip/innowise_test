from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from user.views import UserList, UserDetail



urlpatterns = [
    path("users/", UserList.as_view(), name="users"),
    path('users/<int:id>/<str:name>', UserDetail.as_view(), name="user"), 
]

urlpatterns = format_suffix_patterns(urlpatterns)