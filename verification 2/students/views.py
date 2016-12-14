from rest_framework import permissions, viewsets
from rest_framework.response import Response

from django.contrib.auth import get_user_model
from django.shortcuts import redirect, render

from everify.models import StudentAlumniInfo
from .permissions import IsAccountOwner
from .serializers import StudentAlumniInfoSerializer, UserDocumentSerializer
from everify.models import StudentAlumniInfo, UserDocuments

User = get_user_model()

class StudentAlumniViewSet(viewsets.ModelViewSet):
	queryset = StudentAlumniInfo.objects.all()
	serializer_class = StudentAlumniInfoSerializer

	def get_permissions(self):
		if self.request.method in permissions.SAFE_METHODS:
			return (permissions.AllowAny(),)
		return (permissions.IsAuthenticated(), IsAccountOwner(),)

	def perform_create(self, serializer):
		instance = serializer.save(user=self.request.user)

		return super(StudentAlumniViewSet, self).perform_create(serializer)


class StudentInfoViewSet(viewsets.ViewSet):
	queryset = StudentAlumniInfo.objects.select_related('user')
	serializer_class = StudentAlumniInfoSerializer

	def list(self, request):
		serializer = self.serializer_class(queryset)

		return Response(serializer.data)

class DocumentViewSet(viewsets.ModelViewSet):
	queryset = UserDocuments.objects.order_by('-date_created')
	serializer_class = UserDocumentSerializer

	def get_permissions(self):
		if self.request.method in permissions.SAFE_METHODS:
			return (permissions.AllowAny(),)
		return (permissions.IsAuthenticated(), IsAccountOwner(),)

	def perform_create(self, serializer):
		instance = serializer.save(user=self.request.user)

		return super(DocumentViewSet, self).perform_create(serializer)


class UserDocumentViewSet(viewsets.ViewSet):
	queryset = UserDocuments.objects.select_related('user').all()
	serializer_class = UserDocumentSerializer

	def list(self, request, account_username=None):
		queryset = self.queryset.filter(user__username=account_username)
		serializer = self.serializer_class(queryset, many=True)

		return Response(serializer.data)

def login(request):
    return render(request, 'students/student_alumni_login.html', {})



"""
class PostViewSet(viewsets.ModelViewSet):
	queryset = Post.objects.order_by('-created_at')
	serializer_class = PostSerializer

	def get_permissions(self):
		if self.request.method in permissions.SAFE_METHODS:
			return (permissions.AllowAny(),)
		return (permissions.IsAuthenticated(), IsAuthorOfPost(),)

def perform_create(self, serializer):
	instance = serializer.save(author=self.request.user)

	return super(PostViewSet, self).perform_create(serializer)



class AccountPostsViewSet(viewsets.ViewSet):
	queryset = Post.objects.select_related('author').all()
	serializer_class = PostSerializer

	def list(self, request, account_username=None):
		queryset = self.queryset.filter(author__username=account_username)
		serializer = self.serializer_class(queryset, many=True)

		return Response(serializer.data)
"""