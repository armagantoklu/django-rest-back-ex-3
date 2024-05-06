from django.urls import path, include
from profiller.api.views import ProfileViewSet, ProfilDurumViewSet, ProfilFotoUpdateView
from rest_framework.routers import DefaultRouter

# profile_list = ProfileViewSet.as_view({'get': 'list'})
# profile_detay = ProfileViewSet.as_view({'get': 'retrieve'})
router = DefaultRouter()
router.register(r'kullanici-profilleri', ProfileViewSet, basename='profile')
router.register(r'kullanici-profil-detay', ProfilDurumViewSet, basename='kullanici-profil-detay')
urlpatterns = [
    # path('kullanici-profilleri/', profile_list, name='profuller'),
    # path('kullanici-profilleri/<int:pk>', profile_detay, name='profil-detay'),
    path('', include(router.urls)),
    path('profil_foto/', ProfilFotoUpdateView.as_view(), name='profil-foto'),
]
