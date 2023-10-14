from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.authtoken.models import Token
from django.db import transaction
# from datetime import date

from .serializers import gameSerializer,yourgameSeralizer,transSerializer,WalletSerializer
from .models import Games,User,GameSelect,trans,wallet
from django_filters.rest_framework import DjangoFilterBackend
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json 


# Create your views here.

class gameViewset(ModelViewSet):
    queryset=Games.objects.select_related('pitch','sport','Agerange').prefetch_related("gameselect_set__user").all()
    serializer_class=gameSerializer
    filter_backends=[DjangoFilterBackend]
    filterset_fields=['Date','Status','id']
 
    
# print(date.today())
class selectgameViewset(ModelViewSet):

    def get_queryset(self):
        bam=self.request.query_params.get('username')
        bam1=str(bam).replace("%40","@")
        boom = str(bam1).lower()        # print(boom)
        rpm=User.objects.get(email=boom)
        queryset=GameSelect.objects.filter(user=rpm).order_by("-createdat","-id")
        
        return queryset

    # queryset=GameSelect.objects.all().order_by("-createdat","-id")
    serializer_class=yourgameSeralizer


class gameViewset(ModelViewSet):
    queryset=Games.objects.select_related('pitch','sport','Agerange').prefetch_related("gameselect_set__user").all()
    serializer_class=gameSerializer
    filter_backends=[DjangoFilterBackend]
    filterset_fields=['Date','Status','id']

class transviewset(ModelViewSet):
    queryset=trans.objects.all()
    serializer_class=transSerializer

class walletviewset(ModelViewSet):
    queryset=wallet.objects.all()
    serializer_class=WalletSerializer



@csrf_exempt
def webhook (request):
    if request.method== "POST": 
        with transaction.atomic():       
            cado=request.body.decode('utf-8')
            # jsr=cado.to_json(orient='records')
            dab=[]
            dab=json.loads(cado)
            amt=dab['Body']['amount']
            eml=dab['Body']['email']
            eml2=str(eml).lower()
            game=dab['Body']['meta']['gameid']
            # name=dab['Body']['meta']['name']
            polz=(int(amt))/100

            user1=User.objects.get(email=eml2)
            game1=Games.objects.get(id=game)
            GameSelect.objects.create(user=user1,games=game1,Amount=polz)
            # game2=Games.objects.get(id=game)
            game1.spot = game1.spot + 1
            game1.save()

            ## check if the space is filled then change the game status to complete 
            pum=game1.pitch.players
            pam=game1.spot
            if pum==pam:
                game1.Status='COMPLETE'
                game1.save()
            else:
                pass
            



        print("data received from webhook is :",game,amt,)
        return HttpResponse("webhook received")
    else:
        return HttpResponse("This is not a post methood")





