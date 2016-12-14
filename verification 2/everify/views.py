import json
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.conf import settings
from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import resolve, reverse
from django.shortcuts import redirect, render
from django.views import generic

from rest_framework import permissions, viewsets, status, views
from rest_framework.response import Response
from .serializers import SiteUserSerializer
from .permissions import IsAccountOwner

from authtools.forms import UserCreationForm
from authtools.views import LoginView, LogoutView

User = get_user_model()

class AccountViewSet(viewsets.ModelViewSet):
    lookup_field = 'email'
    queryset = User.objects.all()
    serializer_class = SiteUserSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (permissions.AllowAny(),)

        return (permissions.IsAuthenticated(), IsAccountOwner(),)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            User.objects.create_user(**serializer.validated_data)

            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)

        return Response({
            'status': 'Bad request',
            'message': 'Account could not be created with received data.'
        }, status=status.HTTP_400_BAD_REQUEST)


class LoginView(views.APIView):
    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)
        return (permissions.IsAuthenticated(), IsAccountOwner(),)
        
    def post(self, request, format=None):
        data = json.loads(request.body)

        email = data.get('email', None)
        password = data.get('password', None)

        account = authenticate(email=email, password=password)

        if account is not None:
            if account.is_active:
                login(request, account)

                serialized = SiteUserSerializer(account)

                return Response(serialized.data)
            else:
                return Response({
                    'status': 'Unauthorized',
                    'message': 'This account has been disabled.'
                }, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({
                'status': 'Unauthorized',
                'message': 'Username/password combination invalid.'
            }, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, format=None):
        logout(request)

        return Response({}, status=status.HTTP_204_NO_CONTENT)


class HomeView(generic.TemplateView):
    model = None
    template_name = 'everify/index.html'

class RegistrationView(generic.TemplateView):
    model = None
    template_name = 'everify/register.html'


"""
class EmailUserLoginView(LoginView):
    def get_queryset(self):
        try:
            queryset = User.objects.get(user_id=self.request.user.id)
        except ObjectDoesNotExist:
            queryset = None
        return queryset
    def get_success_url(self, *args, **kwargs):
        queryset =self.get_queryset()
        if queryset != None:
            success_url = reverse('view_list', args=[queryset.id])
        else:
            success_url = reverse('new_list')
        return success_url


class EmailUserLogoutView(LoginView):
    template_name = 'logout.html'

def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
        else:
            return render(request, 'register.html', {'form: form'})
    else:
        return render(request, 'register.html', {'form: form'})

@login_required(login_url='/login')
def home_page(request):
    return render(request, 'home.html', {'form': ItemForm()})

@login_required(login_url='/login')
def view_list()
"""



   
"""
from django.views.generic import TemplateView
from rest_framework import generics
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader, RequestContext
from .models import SiteUser, SiteUserSerializer
from django.shortcuts import render_to_response, redirect, get_object_or_404, render
from django.contrib.auth import login as django_login, authenticate, logout as django_logout

from .forms import AuthenticationForm, EmailUserCreationForm

def login(request):
    #Log in view
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = authenticate(email=request.POST['email'], password=request.POST['password'])
            if user is not None:
                if user.is_active:
                    django_login(request, user)
                    return redirect('/')
    else:
        form = AuthenticationForm()
    return render_to_response('accounts/login.html', {
        'form': form,
    }, context_instance=RequestContext(request))

def register(request):
    #User registration view.
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('/')
    else:
        form = RegistrationForm()
    return render_to_response('accounts/register.html', {
        'form': form,
    }, context_instance=RequestContext(request))

def logout(request):
    #Log out view
    django_logout(request)
    return redirect('/')
"""


"""
class SiteUserViewSet(viewsets.ModelViewSet):
    serializers_class = SiteUserSerializer

    def get_queryset(self):
        return User.objects.filter(self.request.user)
"""