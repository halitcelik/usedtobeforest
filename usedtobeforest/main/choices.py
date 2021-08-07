from djchoices import DjangoChoices, ChoiceItem

class EstablishmentChoices(DjangoChoices):
    hotel = ChoiceItem(10, "Hotel")
    mine = ChoiceItem(20, "Mine")
    other = ChoiceItem(30, "Other")