from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='landing_page'),
    url(r'^(?P<room_name>[^/]+)/$', views.room, name='chat_room')
]

