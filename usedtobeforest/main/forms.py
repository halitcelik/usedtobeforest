from django.forms import ModelForm
from .models import Hotel, Forest, Image, Address


class HotelForm(ModelForm):
    class Meta:
        model = Hotel
        fields = ['chain' ,'name' ,'booking_id' ,'tripadvisor_id' ,'built_year']



class ForestForm(ModelForm):
    class Meta:
        model = Forest
        fields = ['name', 'type_of_tree', 'number_of_trees', 'number_of_species', 'total_area', 'burned_area', 'occupied_area', 'fire_year']
        