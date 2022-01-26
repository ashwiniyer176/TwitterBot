from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("messages/", views.messages, name="messages"),
    path("<int:msg_id>/", views.viewMessage, name="viewmessage")
]
