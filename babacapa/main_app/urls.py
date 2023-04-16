from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'main_app'
urlpatterns = [
   path('', views.index, name='index'),
   path('posts', views.posts, name='posts'),
   path('posts/<int:post_id>/', views.post, name='post'),
   path('new_post', views.new_post, name='new_post'),
   path('edit_post/<int:post_id>', views.edit_post, name='edit_post'),
   path('userlist', views.userlist, name='userlist'),
   path('owned_posts/<int:owner_id>/', views.owned_posts, name='owned_posts'),
   path('delete_post/<int:post_id>/', views.delete_post, name='delete_post'),
   path('like_post/<int:post_id>/', views.like_post, name='like_post'),
]

if settings.DEBUG:
   urlpatterns += static(
      settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
   )

