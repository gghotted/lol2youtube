from django.db import models


class Champion(models.Model):
    eng_name = models.CharField(max_length=64)
    kor_name = models.CharField(max_length=64)

    def __str__(self):
        return self.eng_name


class Replay(models.Model):
    class Meta:
        abstract = True
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    url = models.URLField()

    @property
    def video_id(self):
        return self.url.split('/')[-1]


class PentakillReplay(Replay):
    match_id = models.CharField(max_length=32)
    game_creation = models.DateTimeField()
    game_version = models.CharField(max_length=32)

    upload_channel = models.CharField(max_length=64)

    champion = models.ForeignKey(Champion, models.DO_NOTHING, related_name='replays')
    kill_duration = models.PositiveIntegerField()
    damage_contribution = models.FloatField(default=0)
    ultimate_hit_count = models.PositiveIntegerField()

    @property
    def readable_duration(self):
        return str(round(self.kill_duration / 1000, 1)) + '초'
