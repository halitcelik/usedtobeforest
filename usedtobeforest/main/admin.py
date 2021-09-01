from usedtobeforest.main.models import Establishment
from django.contrib import admin
from .models import Establishment
# Register your models here.


class EstablishmentAdmin(admin.ModelAdmin):
    model = Establishment