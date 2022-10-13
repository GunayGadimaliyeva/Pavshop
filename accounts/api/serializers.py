from dataclasses import field
from rest_framework import serializers
from accounts.models import SubscriberEmail
class SubscriberEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriberEmail
        fields = "__all__"
