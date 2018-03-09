from django.conf.urls import url
from . import views

urlpatterns=[

    url(r'^$',views.photos_of_day,name='photosToday'),
    url(r'^archives/\d{4}-\d{2}-\d{2}/$',views.past_days_photos,name = 'pastPhotos'),
    url(r'^new/post$', views.new_post, name='new-post'),
    url(r'^profile/(?P<id>\d+)/$', views.profile, name ='myProfile'),
    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^search/', views.search_results, name='search_results')


]
