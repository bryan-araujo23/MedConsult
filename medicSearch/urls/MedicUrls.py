from django.urls import path
from medicSearch.views.MedicView  import list_medics_views

urlpatterns = [
    path("", list_medics_views, name='medics'),
]