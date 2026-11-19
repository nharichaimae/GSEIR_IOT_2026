
from .models import Dht11
from .serializers import DHT11serialize

from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.response import Response

from django.core.mail import send_mail
from django.conf import settings

import telebot


# ==========================================
# GET : Récupérer toutes les mesures
# ==========================================

@api_view(['GET'])
def Dlist(request):
    all_data = Dht11.objects.all()
    data = DHT11serialize(all_data, many=True).data

    return Response({'data': data})


# ==========================================
# POST : Enregistrer les mesures du DHT11
# et envoyer les alertes
# ==========================================

class Dhtviews(generics.CreateAPIView):

    queryset = Dht11.objects.all()
    serializer_class = DHT11serialize

    def perform_create(self, serializer):

        # 1. Enregistrer les données dans MySQL
        data = serializer.save()

        # 2. Récupérer la température
        temperature = data.temperature

        # 3. Vérifier si la température dépasse 20°C
        if temperature is not None and temperature > 20:

            message = f"Alerte ! Température = {temperature} °C"

            # 4. Envoyer une alerte Gmail
            try:
                send_mail(
                    subject="Alerte Température",
                    message=message,
                    from_email=None,
                    recipient_list=["nhchaimae774@gmail.com"],
                    fail_silently=False
                )

                print("Alerte Gmail envoyée avec succès !")

            except Exception as e:
                print(f"Erreur Gmail : {e}")

            # 5. Envoyer une alerte Telegram
            try:
                bot = telebot.TeleBot(settings.TELEGRAM_TOKEN)

                bot.send_message(
                    settings.TELEGRAM_CHAT_ID,
                    message
                )

                print("Alerte Telegram envoyée avec succès !")

            except Exception as e:
                print(f"Erreur Telegram : {e}")
