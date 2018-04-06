from django import forms
from .models import Scorecard
from django.core.exceptions import ValidationError

class ReasonValForm(forms.ModelForm):
    time = forms.TimeField(input_formats=('%I:%M %p', '%H:%M:%S'), error_messages={'invalid': 'Invalid time format. Ex. 10:30 AM, 1:30 PM, 11:00:00, 14:30:00'})
    
    def clean(self):
        sale_made = self.cleaned_data['sale_made']
        reason = self.cleaned_data['reason']
        
        if sale_made == 'No' and reason == None:
            raise ValidationError('A no sale needs a reason!')
            
        if sale_made == 'Yes' and reason != None:
            raise ValidationError('A sale should not have a reason for a no sale!')
            
    class Meta:
        model = Scorecard
        fields = '__all__'