import datetime
from django.shortcuts import redirect, render
from . import TweetBot
from .forms import MessageForm
# Create your views here.


def hasDatePassed(date):
    '''
    date(str): String of the format YYYY-MM-DD
    '''
    year, month, day = date.split('-')
    if(datetime.datetime.now().date() > datetime.date(int(year), int(month), int(day))):
        return True
    return False


def hasTimePassed(time):
    '''
    time(str): String of the format HH:MM (24 hr format)
    '''
    hour, minute = time.split(":")
    print(datetime.datetime.now().time().hour, hour)
    if(datetime.datetime.now().time().hour > int(hour)):
        return True
    return False


def index(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        content = None
        if form.is_valid():
            # print(request.POST)
            date_published = request.POST['date_published']
            time_published = request.POST['time_published']
            message = request.POST['message']
            print(date_published, "-", time_published, "-", message)
        # if content:
        #     print("Content:", content)
        #     bot = TweetBot.TwitterAPI()
        #     bot.authenticate()
        #     bot.tweet(content)
        return redirect('index')
    else:
        form = MessageForm()
        return render(request, 'AutoPost/index.html', {"form": form})
