import os

from django.http import Http404
from django.shortcuts import redirect
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.urls import reverse_lazy, reverse
from django.contrib.auth import login, authenticate

from riding_sport_clubs.web_accounts.forms import UserRegistrationForm, UserLoginForm
from riding_sport_clubs.web_accounts.models import SiteUser


class UserRegistrationView(CreateView):
    form_class = UserRegistrationForm
    template_name = 'account/create_profile.html'

    success_url = reverse_lazy('list clubs')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = UserRegistrationForm()
        return context

    def form_valid(self, form):
        form.save()
        new_user = authenticate(username=self.request.POST['username'],
                                password=self.request.POST['password1'])
        login(self.request, new_user)
        return redirect(self.get_success_url())


class UserLoginView(LoginView):
    template_name = 'account/login.html'
    next_page = 'list clubs'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = UserLoginForm()
        return context


class UserLogoutView(LogoutView):
    next_page = 'home page'


class ChangeUserPasswordView(PasswordChangeView):
    template_name = 'account/edit_password.html'
    success_url = reverse_lazy('details profile')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = SiteUser.objects.get(pk=self.request.user.pk)
        return context


class ProfileDetailsView(DetailView):
    model = SiteUser
    template_name = 'account/details_profile.html'


class ProfileEditView(UpdateView):
    model = SiteUser
    fields = ['email', 'phone_number', 'picture']
    template_name_suffix = '_update_form'
    template_name = 'account/edit_profile.html'

    def get_success_url(self):
        success_url = reverse('details profile', kwargs={'pk': self.object.pk})
        if success_url:
            return success_url
        return super().get_success_url()

    def get_context_data(self, **kwargs):
        try:
            context = super(ProfileEditView, self).get_context_data()
            context['object'] = SiteUser.objects.get(pk=self.request.user.pk)
        except SiteUser.DoesNotExist:
            raise Http404()
        return context


class ProfileDeleteView(DeleteView):
    model = SiteUser
    template_name = 'account/delete_profile.html'

    success_url = reverse_lazy('home page')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()

    def form_valid(self, form):
        success_url = self.get_success_url()
        img = SiteUser.objects.get(pk=self.request.user.pk).picture.path
        self.object.delete()
        os.remove(img)
        return redirect(success_url)
