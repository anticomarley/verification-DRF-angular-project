"""verification URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import get_user_model
from rest_framework_nested import routers
from rest_framework import serializers, viewsets
from everify.views import AccountViewSet, LoginView, LogoutView
from students.views import StudentAlumniViewSet, StudentInfoViewSet

admin.autodiscover()

User = get_user_model()

"""
# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
"""

# Routers provide an easy way of automatically determining the URL conf.
#router = routers.DefaultRouter()

router = routers.SimpleRouter()
router.register(r'accounts', AccountViewSet)

router.register(r'students', StudentAlumniViewSet)
accounts_router = routers.NestedSimpleRouter(
    router, r'accounts', lookup='account'
)
accounts_router.register(r'students', StudentInfoViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('everify.urls', namespace='everify')),
    url(r'^students/', include('students.urls', namespace='students')),
    url(r'^api/auth/login/$', LoginView.as_view(), name='login'),
    url(r'^api/auth/logout/$', LogoutView.as_view(), name='logout'),
    #url(r'^accounts/', include('authtools.urls')),
    url(r'^api/', include(router.urls)),
    url(r'^api/', include(accounts_router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
