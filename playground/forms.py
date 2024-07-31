from django import forms
from .models import Booking
from .models import contact
class DateInput(forms.DateInput):
    input_type = 'date'
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
        widgets = {
            'period_from' : DateInput(),
            'period_to' : DateInput(),
        }
class contactForm(forms.ModelForm):
    class Meta:
        model = contact
        fields = '__all__'
      
    