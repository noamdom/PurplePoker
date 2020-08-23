from pprint import pprint

from rest_framework import serializers
from rest_framework.response import Response

from .models import *


class Player1Serializer(serializers.ModelSerializer):
    gain = serializers.SerializerMethodField()
    count_host = serializers.SerializerMethodField()
    power_hands = serializers.SerializerMethodField()

    class Meta:
        model = Player1
        fields = ('id', 'name', 'address', 'gain', 'count_host' , 'hands' , 'power_hands')
        # fields = ('id', 'name', 'address',  'count_host' , 'hands' , 'power_hands')
        extra_kwargs = {
            'hands': {'write_only': True}
        }

    def get_gain(self, player):
        res = 0
        games = SimpleGame.objects.all().values(player.name.lower())
        for g in games:
            res += g[player.name.lower()]
        return res

    def get_count_host(self, player):
        host_meeting = simpleMeeting.objects.filter(house_id=player.id)
        return len(host_meeting)

    def get_power_hands(self, player):
        player_hands = Hand.objects.filter(player_id=player.id)
        return len(player_hands)


class SimpleGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = SimpleGame
        # fiels = "__all__"
        fields = ('id', 'noam', 'johnny', 'moshe', 'ahon', 'dror', 'meeting')
        extra_kwargs = {
            'meeting': {'write_only': True}
        }


class SimpleMeetingSerializer(serializers.ModelSerializer):
    winner = serializers.SerializerMethodField()

    results = serializers.SerializerMethodField()
    all_game = serializers.SerializerMethodField()

    class Meta:
        model = simpleMeeting
        fields = ('id', 'date', 'house', 'games', 'all_game', 'winner', 'results', 'hands')
        extra_kwargs = {
            # 'house': {'write_only': True},
            'games': {'write_only': True},
        }

    def get_results(self, instance):
        games = SimpleGame.objects.filter(meeting=instance)
        total_results = {'noam': 0, 'johnny': 0, 'moshe': 0, 'ahon': 0, 'dror': 0}
        for g in games:
            total_results['noam'] += g.noam
            total_results['johnny'] += g.johnny
            total_results['moshe'] += g.moshe
            total_results['ahon'] += g.ahon
            total_results['dror'] += g.dror
        return total_results
        # return SimpleGameSerializer(g, many=True).data

    def get_all_game(self, meeting):
        games = SimpleGame.objects.filter(meeting=meeting)
        return SimpleGameSerializer(games, many=True).data

    def get_winner(self, meeting):
        all_results = self.get_results(meeting)
        winner_name = ''
        winner_gain = 0

        for player, gains in all_results.items():
            if gains > winner_gain:
                winner_name = player
        return winner_name


class VisualMeetingSerializer(serializers.ModelSerializer):
    # house = Player1Serializer(read_only=True, )
    # games = SimpleGameSerializer(many=True,)

    class Meta:
        model = simpleMeeting
        fields = ('id', 'date', 'house', 'games')
        depth = 1


class HandSerializer(serializers.ModelSerializer):
    # hand_owner = serializers.SerializerMethodField()
    # player = Player1Serializer( )


    class Meta:
        model = Hand
        fields = ('id', 'type', 'description', 'player' , 'meeting' )
        # depth=1





    def get_hand_owner(self, hand):
        # player_hands = Player1.objects.filter(id=hand.player)
        player_hands = "--"

        return player_hands
