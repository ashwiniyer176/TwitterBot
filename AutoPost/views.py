import datetime
from email import message
from django.shortcuts import redirect, render
from . import TweetBot
from .forms import MessageForm
from . import models
# Create your views here.


def index(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        print(type(form))
        content = None
        if form.is_valid():
            new_message = form.save()

        # if content:
        #     print("Content:", content)
        #     bot = TweetBot.TwitterAPI()
        #     bot.authenticate()
        #     bot.tweet(content)
        return redirect('messages')
    else:
        form = MessageForm()
        return render(request, 'AutoPost/index.html', {"form": form})


def messages(request):
    messages = models.Message.objects.all()
    return render(request, "AutoPost/messages.html", {"messages": messages})
