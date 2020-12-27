from django.contrib.auth import login
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .forms import SignUpForm
from .models import Account
from .tokens import account_activation_token
from .utils import mail_confirm_new_user


class HomeView(TemplateView):
    template_name = 'home.html'


class CabinetView(LoginRequiredMixin, TemplateView):
    template_name = 'cabinet/index.html'


class SignUpView(View):
    form_class = SignUpForm
    initial = {'key': 'value'}
    template_name = 'signup.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_confirm_new_user(current_site, user, form.cleaned_data.get('email'))
            return HttpResponse('Пожалуйста потвердите свой адрес электронной почты чтобы закончить регистрацию.')

        return render(request, self.template_name, {'form': form})


class ActivateView(View):
    def get(self, request, *args, **kwargs):
        uidb64 = kwargs.get('uidb64')
        token = kwargs.get('token')
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = Account.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
            user = None
        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            login(request, user)
            return HttpResponse(
                'Спасибо Ваш адрес электронной почты потвержден. Сейчас Вы можете войти в свой аккаунт.')
        else:
            return HttpResponse('Ссылка активации неправильная!')
