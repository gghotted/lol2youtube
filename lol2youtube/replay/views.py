from rest_framework.generics import CreateAPIView

from replay import serializers


class PentakillReplayCreateView(CreateAPIView):
    serializer_class = serializers.PentakillReplayCreateSerializer
    
