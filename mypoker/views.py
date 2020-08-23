from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.pagination import LimitOffsetPagination
from django.core.cache import cache
from rest_framework.response import Response

from .models import *
from .serializers import *
# from .api_view import MeetingPaginaton


# Create your views here.
class SimpleMeetingView(viewsets.ModelViewSet):
    queryset = simpleMeeting.objects.all()
    serializer_class = SimpleMeetingSerializer


class VisualMeetingView(ListAPIView):
    queryset = simpleMeeting.objects.all()
    serializer_class = VisualMeetingSerializer


class SimpleGameView(viewsets.ModelViewSet):
    queryset = SimpleGame.objects.all()
    serializer_class = SimpleGameSerializer
    # pagination_class = MeetingPaginaton


class Player1View(viewsets.ModelViewSet):
    queryset = Player1.objects.all()
    serializer_class = Player1Serializer


class HandView(viewsets.ModelViewSet):
    queryset = Hand.objects.all()
    serializer_class = HandSerializer

    def destroy(self, request, *args, pk=None):
        hand_id = pk
        hand = self.queryset.filter(id = hand_id)
        hand.delete()
        cache.delete('hands{}'.format(hand_id))
        return Response("Hand removed" ,200)

