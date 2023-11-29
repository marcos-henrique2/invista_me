from django.forms import ModelForm
from .models import Investimeto

class InvestimentoForm(ModelForm):
    class Meta: 
        model = Investimeto
        fields = '__all__' 