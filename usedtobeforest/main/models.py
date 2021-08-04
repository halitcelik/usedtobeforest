from django.db import models

class Chain(models.Model):
    name = models.CharField("Hotels chain name", max_length=127)

class Hotel(models.Model):
    chain = models.ForeignKey(Chain, on_delete=models.PROTECT, blank=True, null=True)
    name = models.CharField("Hotel name", max_length=127)
    booking_id = models.CharField("booking.com ID", max_length=127, blank=True, null=True)
    tripadvisor_id = models.CharField("tripadvisor.com ID", max_length=127, blank=True, null=True)
    built_year = models.IntegerField(blank=True, null=True)


class Address(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name="addresses")
    street = models.CharField("Street name", max_length=255, blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    city = models.CharField("City", max_length=127)
    country = models.CharField("Country", max_length=127)

class Forest(models.Model):
    name = models.CharField("Name", max_length=127, blank=True, null=True)
    type_of_tree = models.CharField("Type of trees", max_length=127, blank=True, null=True)
    number_of_trees = models.IntegerField(blank=True, null=True)
    number_of_species = models.IntegerField(blank=True, null=True)
    total_area = models.IntegerField(blank=True, null=True, help_text="The total area of the forest")
    burned_area = models.IntegerField(blank=True, null=True, help_text="The total burned area of the forest")
    occupied_area = models.IntegerField(blank=True, null=True, help_text="The total area occupied by the hotel")
    fire_year = models.IntegerField(blank=True, null=True)


class Image(models.Model):
    pass
    # file = filer file field
    # date (the date image is taken)
    # type choices: (old, new)