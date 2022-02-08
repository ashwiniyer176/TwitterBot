from unicodedata import name
from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("messages/", views.messages, name="messages"),
    path("<int:msg_id>/", views.sendMessage, name="viewmessage"),
    path("delete/<int:msg_id>", views.deleteMessage, name="deletemessage")
]
