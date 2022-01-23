import tweepy

from django.shortcuts import redirect, render
from . import TweetBot
from .forms import MessageForm
# Create your views here.


def index(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        content = None
        if form.is_valid():
            print(request.POST)
        # if content:
        #     print("Content:", content)
        #     bot = TweetBot.TwitterAPI()
        #     bot.authenticate()
        #     bot.tweet(content)
        return redirect('index')
    else:
        form = MessageForm()
        return render(request, 'AutoPost/index.html', {"form": form})
