from rest_framework import serializers

from replay.models import PentakillReplay


class PentakillReplayCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PentakillReplay
        fields = (
            'url',
            'match_id',
            'game_creation',
            'game_version',
            'upload_channel',
            'champion_name',
            'champion_kor_name',
            'kill_duration',
            'ultimate_hit_count',
        )
