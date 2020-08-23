from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination

from .models import *
from .serializers import *


class GamesPaginaton(LimitOffsetPagination):
    default_limit = 10
    max_limit = 20

#
# class MeetingPaginaton(LimitOffsetPagination):
#     default_limit = 1
#     max_limit = 1


class GameList(ListAPIView):
    queryset = SimpleGame.objects.all()
    serializer_class = SimpleGameSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('id',)
    search_fields = ('noam',)
    pagination_class = GamesPaginaton

    def get_queryset(self):
        '''
        usign url
        '''
        # id = self.request.query_params.get('id', None)
        noam_gain = self.request.query_params.get('noam', None)

        # if id is not None:
        if noam_gain is None:
            return super().get_queryset()
        queryset = SimpleGame.objects.all()
        return queryset.filter(
            noam__gte=noam_gain)


class GameCreate(CreateAPIView):
    serializer_class = SimpleGameSerializer

    def create(self, request, *args, **kwargs):
        try:
            meeting = request.data.get('meeting')
            if meeting is not None and int(meeting) <= 0:
                raise ValidationError({'meeting': "Must be an existing meeting"})
        except ValueError:
            pass
        return super().create(request, *args, **kwargs)


class GameRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = SimpleGame.objects.all()
    lookup_field = 'id'
    serializer_class = SimpleGameSerializer

    def delete(self, request, *args, **kwargs):
        game_id = request.data.get('id')
        response = super().delete(request, *args, **kwargs)
        if response.status_code == 204:
            from django.core.cache import cache
            cache.delete('game_data_{}'.format(game_id))  # ???

        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        if response.status_code == 204:
            from django.core.cache import cache
            game = response.data
            cache.set('game_data_{}'.format(game['id']), {
                'noam': game['noam'],
                'johnny': game['johnny'],
                'moshe': game['moshe'],
                'ahon': game['ahon'],
                'dror': game['dror'],
                'meeting': game['meeting'],
            })

        return response
