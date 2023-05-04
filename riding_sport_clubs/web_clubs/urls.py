from django.urls import path
from django.views.generic import TemplateView

from riding_sport_clubs.web_clubs.views import HomeView, payment, ClubsListView, ClubDetailsView, ClubEditView, \
    ClubCreateView, racing_info, like_club, search_club, BreedsList, BreedInfo

urlpatterns = (
    path('', HomeView.as_view(), name='home page'),
    path('payment/', payment, name='pay page'),
    path('access_denied/', TemplateView.as_view(template_name='web/../../templates/bases/authorization.html'), name='authorization'),

    path('list_clubs/', ClubsListView.as_view(), name='list clubs'),
    path('list_clubs/search/', search_club, name='search club'),
    path('like/<int:pk>', like_club, name='like club'),
    path('club_info/<int:pk>/', ClubDetailsView.as_view(), name='club info'),
    path('club_edit/<int:pk>/', ClubEditView.as_view(), name='edit club'),
    path('club/create/', ClubCreateView.as_view(), name='create club'),

    path('breeds/', BreedsList.as_view(), name='breeds page'),
    path('breed_info/<int:pk>/', BreedInfo.as_view(), name='breed info'),

    path('racing_info/', racing_info, name='racing info'),
)

