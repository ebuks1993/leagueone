from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views



router=DefaultRouter()
router.register('games', views.gameViewset)
router.register("selectgames",views.selectgameViewset,basename='gameselect')



urlpatterns = [
    path("",include(router.urls)),
    path('webhook',views.webhook)]
