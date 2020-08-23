from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views
from . import api_view

router = routers.DefaultRouter()
router.register('meetings', views.SimpleMeetingView)
# router.register('visualmeetings', views.VisualMeetingView)
router.register('players', views.Player1View)
router.register('games', views.SimpleGameView)
router.register('hands', views.HandView)

urlpatterns = [
    path('', include(router.urls)),
    path('api/meetings/', views.VisualMeetingView.as_view()),
    path('api/games/', api_view.GameList.as_view()),
    path('api/games/new/', api_view.GameCreate.as_view()),
    path('api/games/<int:id>/', api_view.GameRetrieveUpdateDestroy.as_view()),
]
