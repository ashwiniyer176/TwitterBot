import datetime
from email import message
from django.http import HttpResponse
from django.shortcuts import redirect, render
from . import TweetBot
from .forms import MessageForm
from . import models
# Create your views here.


def index(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        print(type(form))
        if form.is_valid():
            new_message = form.save()
        return redirect('messages')
    else:
        form = MessageForm()
        return render(request, 'AutoPost/index.html', {"form": form})


def messages(request):
    messages = models.Message.objects.all()
    return render(request, "AutoPost/messages.html", {"messages": messages})


def viewMessage(request, msg_id):
    print("Message ID:", msg_id)
    msg = models.Message.objects.filter(id=msg_id)
    bot = TweetBot.TwitterAPI()
    bot.authenticate()
    bot.tweet(msg[0].message)
    return redirect('messages')
