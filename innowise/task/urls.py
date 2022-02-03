from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from task.views import *



urlpatterns = [
    path("post_list/", PostList.as_view(), name="post_list"),
    path("post_update/<int:pk>/", PostUpdate.as_view(), name="post_update"),
    path("post_destroy/<int:pk>/", PostDestroy.as_view(), name="post_destroy"),
    path("comments/<int:pk>/", CommentDetail.as_view(), name="comments"),  
]

urlpatterns = format_suffix_patterns(urlpatterns)