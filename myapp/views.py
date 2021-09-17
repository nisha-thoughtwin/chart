from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Car,Vehicle
import pandas as pd

# Create your views here.
def mainview(request):
    qs = Car.objects.all().values()
    data = pd.DataFrame(qs)
    print(data)
    context ={
        'df': data.to_html(),
        'describe' : data.describe().to_html(),
    }
   
    return render(request,'car/main.html',context)

class chart(TemplateView):
    template_name = 'chart.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] =  Vehicle.objects.all()
        return context