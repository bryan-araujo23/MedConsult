from django.urls import path

# de     app     pasta  arquivo import  função
from medicSearch.views.HomeView import home_view


urlpatterns = [
    path("", home_view),
]
