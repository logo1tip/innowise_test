from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from task.views import *



urlpatterns = [
    path("post_list/", PostList.as_view(), name="post_list"),
    path("post_update/<int:pk>/<str:name>/", PostUpdate.as_view(), name="post"),
    path("post_destroy/<int:pk>/<str:name>/", PostDestroy.as_view(), name="post"),
    path("comments/<str:name>/<int:pk>/", CommentDetail.as_view(), name="comment"),  
]

urlpatterns = format_suffix_patterns(urlpatterns)