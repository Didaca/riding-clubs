from django.urls import path

from riding_sport_clubs.web_accounts.views import UserRegistrationView, UserLoginView, UserLogoutView, \
    ChangeUserPasswordView, ProfileDetailsView, ProfileEditView, ProfileDeleteView

urlpatterns = (
    path('registration/', UserRegistrationView.as_view(), name='registration'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('edit-password/', ChangeUserPasswordView.as_view(), name='edit password'),

    path('profile/details/<int:pk>', ProfileDetailsView.as_view(), name='details profile'),
    path('profile/edit/<int:pk>', ProfileEditView.as_view(), name='edit profile'),
    path('profile/delete/<int:pk>', ProfileDeleteView.as_view(), name='delete profile'),
)
