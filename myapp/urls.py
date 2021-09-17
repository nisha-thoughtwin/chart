from django.urls import path
from .views import mainview,chart
urlpatterns = [
    path('mainview/',mainview,name='mainview'),
    path('chart/',chart.as_view(),name="chart")
]