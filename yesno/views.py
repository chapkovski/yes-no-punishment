from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants

class Punishment(Page):
    form_model = models.Player
    form_fields = ['response_1',
                   'punish_1']



page_sequence = [
    Punishment,
]
