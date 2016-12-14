from rest_framework import serializers

from django.contrib.auth import get_user_model
from everify.models import StudentAlumniInfo, UserDocuments
from everify.serializers import SiteUserSerializer

User = get_user_model()

class StudentAlumniInfoSerializer(serializers.ModelSerializer):
    user = SiteUserSerializer(read_only=True, required=False)

    class Meta:
        model = StudentAlumniInfo

        fields = ('id', 'user', 'first_name', 'last_name', 'dateofbirth', 'contact', 'city', 'country', 'photo')
        read_only_fields = ('id',)

    def get_validation_exclusions(self, *args, **kwargs):
        exclusions = super(StudentAlumniInfoSerializer, self).get_validation_exclusions()

        return exclusions + ['user']

class UserDocumentSerializer(serializers.ModelSerializer):
    user = SiteUserSerializer(read_only=True, required=False)

    class Meta:
        model = UserDocuments

        fields = ('id', 'user', 'category', 'subcategory', 'document_id', 'document name', 'date_created', 'document')
        read_only_fields = ('id', 'date_created')

    def get_validation_exclusions(self, *args, **kwargs):
        exclusions = super(UserDocumentSerializer, self).get_validation_exclusions()

        return exclusions + ['user']
