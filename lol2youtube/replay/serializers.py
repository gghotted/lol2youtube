from rest_framework import serializers

from replay.models import Champion, PentakillReplay


class ChampionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Champion
        fields = '__all__'

    def create(self, validated_data):
        return self.Meta.model.objects.get_or_create(**validated_data)


class PentakillReplaySerializer(serializers.ModelSerializer):
    champion = ChampionSerializer()

    class Meta:
        model = PentakillReplay
        fields = (
            'url',
            'match_id',
            'game_creation',
            'game_version',
            'upload_channel',
            'kill_duration',
            'damage_contribution',
            'ultimate_hit_count',
            'champion',
        )

    def create(self, validated_data):
        champion = Champion.objects.get_or_create(**validated_data.pop('champion'))[0]
        return PentakillReplay.objects.create(
            champion=champion,
            **validated_data,
        )
