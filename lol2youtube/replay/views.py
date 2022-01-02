import json
from datetime import datetime, timedelta
from urllib.parse import urlencode

from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView
from pure_pagination.mixins import PaginationMixin

from replay.forms import ReplayListSearchForm
from replay.models import Champion, PentakillReplay


class PentakillReplayListView(PaginationMixin, ListView):
    model = PentakillReplay
    paginate_by = 12

    def _get_default_url(self):
        default_params = {
            'days': -1,
            'o': '-game_creation',
            'name': '',
        }
        params_string = urlencode(default_params)
        return reverse('replay:home') + '?' + params_string

    def get(self, request, *args, **kwargs):
        self.form = ReplayListSearchForm(self.request.GET)
        if not self.form.is_valid():
            return redirect(self._get_default_url())
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form
        context['total_length'] = len(self.object_list)
        context['champion_kor_list'] = json.dumps(
            list(Champion.objects.values_list('kor_name', flat=True)),
            ensure_ascii=False,
        )
        return context

    def get_queryset(self):
        qs = super().get_queryset()
        for method_name in filter(lambda m: m.startswith('_filter'), dir(self)):
            method = getattr(self, method_name)
            qs = method(qs)
        return self._ordering(qs)

    def _filter_game_creation(self, qs):
        days = int(self.request.GET.get('days', -1))
        if days > 0:
            start_day = datetime.today() - timedelta(days=days)
        else:
            start_day = datetime.min
        return qs.filter(game_creation__gte=start_day)

    def _filter_champion_name(self, qs):
        name = self.request.GET.get('name', '')
        return qs.filter(champion__kor_name__icontains=name)

    def _ordering(self, qs):
        order = self.request.GET.get('o', '-game_creation')
        return qs.order_by(order)
