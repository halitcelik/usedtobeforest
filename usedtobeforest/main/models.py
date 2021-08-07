from django.db import models
from parler.models import TranslatableModel, TranslatedFields
from django.utils.translation import gettext_lazy as _
from .choices import EstablishmentChoices
class Chain(models.Model):
    name = models.CharField("Establishments chain name", max_length=127)

class Establishment(TranslatableModel):
    chain = models.ForeignKey(Chain, on_delete=models.PROTECT, blank=True, null=True)
    booking_id = models.CharField("booking.com ID", max_length=127, blank=True, null=True)
    tripadvisor_id = models.CharField("tripadvisor.com ID", max_length=127, blank=True, null=True)
    built_year = models.IntegerField(blank=True, null=True)
    type = models.IntegerField(choices=EstablishmentChoices.choices)
    translations = TranslatedFields(
        name = models.CharField("Establishment name", max_length=127)
    )

class Address(models.Model):
    Establishment = models.ForeignKey(Establishment, on_delete=models.CASCADE, related_name="addresses", blank=True, null=True)
    street = models.CharField(_("Street name"), max_length=255, blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    city = models.CharField(_("City"), max_length=127)
    country = models.CharField(_("Country"), max_length=127)

class Forest(TranslatableModel):
    number_of_trees = models.IntegerField(blank=True, null=True)
    number_of_species = models.IntegerField(blank=True, null=True)
    total_area = models.IntegerField(blank=True, null=True, help_text=_("The total area of the forest"))
    burned_area = models.IntegerField(blank=True, null=True, help_text=_("The total burned area of the forest"))
    occupied_area = models.IntegerField(blank=True, null=True, help_text=_("The total area occupied by the Establishment"))
    fire_year = models.IntegerField(blank=True, null=True)
    translations = TranslatedFields(
        name = models.CharField(_("Name"), max_length=127, blank=True, null=True),
        type_of_tree = models.CharField(_("Type of trees"), max_length=127, blank=True, null=True)
    )


class Image(models.Model):
    pass
    # file = filer file field
    # date (the date image is taken)
    # type choices: (old, new)