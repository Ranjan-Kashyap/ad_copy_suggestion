from django.urls import path
from .views import FacebookAdsHeadline, FacebookAdsCopy,\
    GoogleAdsDescription, GoogleAdsHeadline 

urlpatterns = [
    path('facebook/ad-copy/', FacebookAdsCopy.as_view(), name='facebook_ad_copy'),
    path('facebook/ad-headline/', FacebookAdsHeadline.as_view(), name='facebook_ad_headline'),
    path('google/ad-headline/', GoogleAdsHeadline.as_view(), name='google_ad_headline'),
    path('google/ad-descriptions/', GoogleAdsDescription.as_view(), name='google_ad_descriptions'),
]
