from django.urls import path
from .views import (
    MessageCreateView,
    MessageListView,
    UserLoginAPIView,
    UserCreateAPIView,
    ChannelCreateAPIView,
    ChannelListAPIView
)
urlpatterns = [
    path('channellist', ChannelListAPIView.as_view(), name='channel-list'),
    path('create/', ChannelCreateAPIView.as_view(), name='channel-create'),
    path('messagelist/<int:channel_id>/', MessageListView.as_view(), name='message-list'),
    path('messagecreate/<int:channel_id>/send/',MessageCreateView.as_view(), name='message-create'),
]