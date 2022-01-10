from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls', namespace='blog')),
    # post views
    # path('', views.post_list, name='post_list'),
    path('', views.PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',views.post_detail,name='post_detail'),

]




# from django.urls import path
# from . import views
# app_name = 'blog'
# urlpatterns = [
#     # post views
#     path('', views.post_list, name='post_list'),
#     path('<int:year>/<int:month>/<int:day>/<slug:post>/',views.post_detail,name='post_detail'),
# ]