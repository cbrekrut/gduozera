from django.shortcuts import render
import telebot
from .models import House, Service
TELEGRAM_BOT_TOKEN ='6919768284:AAEAiJtCTWaUWVdkY5vxDNRmb3pqES4Fx_o'
TELEGRAM_CHAT_ID = '-4137887911'
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

def index(request):
    houses = House.objects.all()
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        telephone = request.POST.get('telephone')
        date = request.POST.get('date')
        home = request.POST.get('home')
        message = f"Новый заказ!\nИмя: {name}\nEmail: {email}\nТелефон: {telephone}\nДаты: {date}\nДомик: {home}"
        
        bot.send_message(TELEGRAM_CHAT_ID, message)
    return render(request, 'index.html', {'houses':houses})

def about(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        telephone = request.POST.get('telephone')
        message = f"Новый заказ!\nИмя: {name}\nEmail: {email}\nТелефон: {telephone}"
        
        bot.send_message(TELEGRAM_CHAT_ID, message)
    return render(request, 'about.html')


def places(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        telephone = request.POST.get('telephone')
        message = f"Новый заказ!\nИмя: {name}\nEmail: {email}\nТелефон: {telephone}"
        
        bot.send_message(TELEGRAM_CHAT_ID, message)
    return render(request, 'places.html')

def contacts(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        telephone = request.POST.get('telephone')
        message = f"Новый заказ!\nИмя: {name}\nEmail: {email}\nТелефон: {telephone}"
        
        bot.send_message(TELEGRAM_CHAT_ID, message)
    return render(request, 'contact-us.html')

def services(request):
    services = Service.objects.all()
    return render(request, 'services.html', {'services': services})