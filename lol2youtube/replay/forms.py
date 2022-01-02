from django import forms


class ReplayListSearchForm(forms.Form):
    days = forms.ChoiceField(
        widget=forms.Select(attrs={
            'class': 'form-control'
        }),
        choices=[
            (1, '최근 24시간'),
            (7, '최근 일주일'),
            (28, '최근 한달'),
            (-1, '모든 기간'),
        ],
        label='기간',
    )
    o = forms.ChoiceField(
        widget=forms.Select(attrs={
            'class': 'form-control'
        }),
        choices=[
            ('-game_creation', '최근 게임 순'),
            ('kill_duration', '빠른 펜타킬 순'),
        ],
        label='정렬',
    )
    name = forms.CharField(
        max_length=64,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control'
        }),
        label='챔피언 이름',
    )
