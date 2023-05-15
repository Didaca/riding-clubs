from django.urls import reverse_lazy, reverse
from django.views import generic as views
from django.shortcuts import render, redirect

from riding_sport_clubs.web_accounts.models import SiteUser
from riding_sport_clubs.web_clubs.forms import ClubForm
from riding_sport_clubs.web_clubs.models import Club, HorseBreed


def search_club(request):
    if request.method == 'GET':
        all_clubs_search = []
        input_text = request.GET.get('search')
        clubs = Club.objects.all()
        for club in clubs:
            compare_name = club.club_name.lower()
            if club.club_name == input_text:
                all_clubs_search.append(club)
                return render(request, 'web/clubs_list.html', {'object_list': all_clubs_search})
            elif compare_name.startswith(input_text.lower()):
                all_clubs_search.append(club)
        return render(request, 'web/clubs_list.html', {'object_list': all_clubs_search})


def racing_info(request):
    return render(request, 'bases/under_construction.html')


def like_club(request, pk):
    club = Club.objects.get(pk=pk)
    user_ho_like = SiteUser.objects.get(pk=request.user.pk)
    inside = False
    for k in user_ho_like.lk_clubs:
        if k == club.club_name:
            inside = True
    if not inside:
        user_ho_like.lk_clubs.append(club.club_name)
        user_ho_like.save()
        club.rating += 1
        club.save()
    return redirect('list clubs')


class BreedInfo(views.DetailView):
    model = HorseBreed
    template_name = 'web/breed_info.html'


class BreedsList(views.ListView):
    model = HorseBreed
    template_name = 'web/horse_breeds.html'


def payment(request):
    return render(request, 'web/pay_page.html')


class HomeView(views.TemplateView):
    context_key = 'user'
    context_value = 'No'

    template_name = 'account/entry_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            context[self.context_key] = self.request.user.username
        else:
            context[self.context_key] = self.context_value

        return context


class ClubsListView(views.ListView):
    context_object_name = 'object_list'
    model = Club
    template_name = 'web/clubs_list.html'
    ordering = ('-award_gold', '-award_silver', '-award_bronze',)

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset.prefetch_related('trainer_set')
        return queryset


class ClubCreateView(views.CreateView):
    form_class = ClubForm
    template_name = 'web/create_club.html'
    success_url = reverse_lazy('list clubs')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_staff is False:
            return redirect('authorization')
        return super().dispatch(request, *args, **kwargs)


class ClubDetailsView(views.DetailView):
    context_object_name = 'club'
    model = Club
    template_name = 'web/club_info.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset.prefetch_related('trainer_set')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        try:
            user_object = SiteUser.objects.get(pk=self.request.user.pk).full_name
            context['object'] = user_object
        except SiteUser.DoesNotExist:
            context['object'] = None
        return context


class ClubEditView(views.UpdateView):
    model = Club
    fields = ['club_name', 'owner', 'email_club', 'address', 'club_phone_number', 'description', 'club_logo']
    template_name = 'web/club_edit.html'

    def get_success_url(self):
        success_url = reverse('club info', kwargs={'pk': self.object.pk})

        if success_url:
            return success_url
        return super().get_success_url()
