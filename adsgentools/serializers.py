from rest_framework import serializers
from .models import FacebookAds, GoogleAds


class FacebookAdsHeadlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacebookAds
        fields = '__all__'

class FacebookAdsCopySerializer(serializers.ModelSerializer):
    class Meta:
        model = FacebookAds
        fields = '__all__'

class GoogleAdsHeadlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoogleAds
        fields = '__all__'

class GoogleAdsDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoogleAds
        fields = '__all__'
        