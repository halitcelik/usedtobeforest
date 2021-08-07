from django.forms import ModelForm
from .models import Establishment, Forest, Image, Address


class EstablishmentForm(ModelForm):
    class Meta:
        model = Establishment
        fields = ['chain' ,'name' ,'booking_id' ,'tripadvisor_id' ,'built_year']



class ForestForm(ModelForm):
    class Meta:
        model = Forest
        fields = ['name', 'type_of_tree', 'number_of_trees', 'number_of_species', 'total_area', 'burned_area', 'occupied_area', 'fire_year']

