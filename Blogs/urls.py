from django.urls import path
from .views import *


urlpatterns = [
    path('', BlogList.as_view(), name = "blog_list"),
    path('<int:pk>', BlogDetail.as_view(), name = "blog_detail"),
    path('new/', BlogCreate.as_view() , name = 'blog_new'), 
    path('<int:pk>/update', BlogUpdate.as_view(), name = 'blog_update'),
    path('<int:pk>/delete', BlogDelete.as_view(), name = 'blog_delete'),
    # path('profile/' , ProfileView.as_view(), name='profile')
]
