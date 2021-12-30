from rest_framework.generics import ListCreateAPIView

from replay import serializers
from replay.models import PentakillReplay


class PentakillReplayListCreateView(ListCreateAPIView):
    serializer_class = serializers.PentakillReplaySerializer
    queryset = PentakillReplay.objects.all()
