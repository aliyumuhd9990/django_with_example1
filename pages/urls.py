from django.urls import path
from .views import *
app_name = 'pages'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('new_post/', CreatePostView.as_view(), name= 'new_post'),
    path('edit_post/<int:pk>', UpdatePostView.as_view(), name= 'update_post'),
    path('delete_post/<int:pk>', DeletePostView.as_view(), name= 'delete_post'),
]
