from django.contrib.auth import update_session_auth_hash
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class SiteUserSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True, required=False)

	class Meta:
		model = User
		fields = ('id', 'email', 'name','is_active', 'is_superuser', 
				  'is_staff', 'password',)

		def create(self, validated_data):
			return User.objects.create(**validated_data)

		def update(self, instance, validated_data):
			instance.email = validated_data.get('email', instance.email)
			instance.full_name = validated_data.get('full_name', instance.full_name)

			instance.save()

			password = validated_data.get('password', None)
			instance.set_password(password)
			instance.save()

			update_session_auth_hash(self.context.get('request'), instance)

			return instance

"""
class SiteUserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		#fields = ('id', 'email', 'full_name', 'is_active', 'is_superuser', 'is_staff')
		fields = '__all__'
"""