from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.photos_of_day,name='photosToday'),
    url(r'^archives/\d{4}-\d{2}-\d{2}/$',views.past_days_photos,name = 'pastPhotos'),
    url(r'^new/post$', views.new_post, name='new-post')

]
