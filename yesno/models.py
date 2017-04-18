from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
from radiogrid import RadioGridField
import random

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'yesno'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    ...


class Group(BaseGroup):
    ...


class Player(BasePlayer):
    response_1 = models.PositiveIntegerField()
    punish_1 = models.BooleanField(widget = widgets.RadioSelectHorizontal())
