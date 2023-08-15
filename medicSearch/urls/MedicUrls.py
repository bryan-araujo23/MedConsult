from django.urls import path
from medicSearch.views.MedicView  import list_medics_views, add_favorite_view, remove_favorite_view

urlpatterns = [
    path("", list_medics_views, name='medics'),
    path("favorite", add_favorite_view, name='medic-favorite'),
    path("favorite/remove", remove_favorite_view, name='medic-favorite-remove')
]