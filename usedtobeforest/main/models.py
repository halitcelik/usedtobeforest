from django.db import models

# Create your models here.
class Hotel(models.Model):
    pass
    # name
    # website ?



class Address(models.Model):
    pass
    # hotel FK


class Image(models.Model):
    pass
    # file = filer file field
    # date (the date image is taken)
    # type choices: (old, new)