from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from meetups.models import Meetup, Account

class MeetupSerializer(ModelSerializer):
    class Meta:
        model = Meetup
        fields = '__all__'

# class UserSerializer(ModelSerializer):
#     def create(self, validated_data):
#         user = User.objects.create_user(**validated_data)
#         return user

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password']

class RegistrationSerializer(ModelSerializer):

    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = Account
        fields = ['email', 'username', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        account = Account(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})

        account.set_password(password)
        account.save()

        return account

