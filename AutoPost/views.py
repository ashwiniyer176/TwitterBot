import json
from django.http import HttpResponse
from django.shortcuts import redirect, render
from . import TweetBot
from .forms import MessageForm
from . import models
import requests
# Create your views here.


def getNewQuotes():
    url = "https://favqs.com/api/qotd"
    response = requests.request(
        "GET", url)
    # new_mesage=models.Message()
    quote_object = json.loads(response.text)
    message = quote_object['quote']['body']
    author = quote_object['quote']['author']
    new_message = models.Message(message=message, author=author)
    new_message.save()


def index(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        print(type(form))
        if form.is_valid():
            new_message = form.save()
            return redirect('messages')
        else:
            return HttpResponse("error")
    else:
        form = MessageForm()
        return render(request, 'AutoPost/index.html', {"form": form})


def messages(request):
    messages = models.Message.objects.filter(sent=False)
    if len(messages) == 0:
        print("No new messages")
        # API Call to QuotesAPI
        getNewQuotes()
        return redirect('messages')
    return render(request, "AutoPost/messages.html", {"messages": messages})


def deleteMessage(request, msg_id):
    models.Message.objects.filter(id=msg_id).delete()
    return redirect('messages')


def sendMessage(request, msg_id):
    msg = models.Message.objects.filter(id=msg_id)
    bot = TweetBot.TwitterAPI()
    bot.authenticate()
    bot.tweet(msg[0].message, msg[0].author)
    msg[0].toggle_message_status()
    return redirect('messages')
