from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .serializers import  FacebookAdsHeadlineSerializer, FacebookAdsCopySerializer,\
    GoogleAdsDescriptionSerializer,GoogleAdsHeadlineSerializer
from .models import PromptSelector
from Project import settings
from .ads_utils import ads_generator
import random
import logging

logger = logging.getLogger(__name__)

def prompt_selector(ad_type, data, prompt_collection):
    """
    Selects and customizes a random prompt based on the given ad type and data.

    Parameters:
        ad_type (str): The type of ad (e.g., 'facebook', 'google', etc.).
        data (dict): A dictionary containing data for prompt customization.
                     Possible keys: 'productName', 'productDescription', 'tone', 'occasion', 'promotion'.
        prompt_collection (QuerySet): A QuerySet of PromptSelector objects filtered by ad_type.

    Returns:
        str: A customized prompt string with placeholders replaced by data values.
    """
    is_facebook_ad = "facebook" in ad_type
    try:
        prompt = random.choice([item.prompt for item in prompt_collection])
    except IndexError:
        logger.warning(f"No prompts found for ad type '{ad_type}'. Using default prompt.")
        prompt = '''Give me top 10 Facebook ads headline for the occasion [Occasion] with product name [Product Name]\n[Product Description] just got even better, and we can't wait to share it with you. 
\nWhether you're looking for a [Tone] twist on [Occasion] or simply want to make a statement,\nPromotion for [Promotion]'''
    
    replacements = {
        "[Product Name]": data.get("productName", ""),
        "[Product Description]": data.get("productDescription", ""),
        "[Tone]": data.get("tone", "Friendly" if is_facebook_ad else "Professional"),
        "[Occasion]": data.get("occasion", "Sale") if is_facebook_ad else "",
        "[Promotion]": data.get("promotion", data.get("productName", "")) if is_facebook_ad else ""
    }

    for key, value in replacements.items():
        prompt = prompt.replace(key, value)

    return prompt

class FacebookAdsHeadline(APIView): 
    def post(self, request, *args, **kwargs):
        '''
        Create the Facebook Ads Headline with given data
        '''
        if request.META.get('HTTP_AUTHORIZATION') == f'Bearer {settings.token}':
            ad_type = 'facebook_ad_headline'
            prompt_collection = prompt_collection = PromptSelector.objects.filter(adType=ad_type)
            prompt = prompt_selector(ad_type,request.data,prompt_collection)
            # calling openAI api to generate ads
            content = ads_generator.generate_ads(prompt,settings.openAIkey)
            data = {
                'productName': request.data.get('productName'), 
                'productDescription': request.data.get('productDescription'), 
                'occasion': request.data.get('occasion'),
                'promotion': request.data.get('promotion'),
                'tone': request.data.get('tone'),
                'adType':ad_type,
                'prompt':prompt,
                'content':content,
                'identifier':request.data.get('identifier')
            }

            serializer = FacebookAdsHeadlineSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                result = serializer.data.get('content')
                identifier = serializer.data.get('identifier')
                return Response({'content':result,'identifier':identifier}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error':'In valid token passed'}, status=status.HTTP_400_BAD_REQUEST)
    
class FacebookAdsCopy(APIView): 
    def post(self, request, *args, **kwargs):
        '''
        Create the Facebook Ads copy with given data
        '''
        if request.META.get('HTTP_AUTHORIZATION') == f'Bearer {settings.token}':
            ad_type = 'facebook_ad_copy'
            prompt_collection = prompt_collection = PromptSelector.objects.filter(adType=ad_type)
            prompt = prompt_selector(ad_type,request.data,prompt_collection)
            # calling openAI api to generate ads
            content = ads_generator.generate_ads(prompt,settings.openAIkey)
            data = {
                'productName': request.data.get('productName'), 
                'productDescription': request.data.get('productDescription'), 
                'occasion': request.data.get('occasion'),
                'promotion': request.data.get('promotion'),
                'tone': request.data.get('tone'),
                'adType':ad_type,
                'prompt':prompt,
                'content':content,
                'identifier':request.data.get('identifier')
            }
            serializer = FacebookAdsCopySerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                result = serializer.data.get('content')
                identifier = serializer.data.get('identifier')
                return Response({'content':result,'identifier':identifier}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error':'In valid token passed'}, status=status.HTTP_400_BAD_REQUEST)

class GoogleAdsDescription(APIView): 
    def post(self, request, *args, **kwargs):
        '''
        Create the Google Ads Description with given data
        '''
        if request.META.get('HTTP_AUTHORIZATION') == f'Bearer {settings.token}':
            ad_type = 'google_ad_description'
            prompt_collection = prompt_collection = PromptSelector.objects.filter(adType=ad_type)
            prompt = prompt_selector(ad_type,request.data,prompt_collection)
            # calling openAI api to generate ads
            content = ads_generator.generate_ads(prompt,settings.openAIkey)
            data = {
                'productName': request.data.get('productName'), 
                'productDescription': request.data.get('productDescription'), 
                'tone': request.data.get('tone'),
                'adType': ad_type,
                'prompt': prompt,
                'content': content,
                'identifier':request.data.get('identifier')
            }
            serializer = GoogleAdsDescriptionSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                result = serializer.data.get('content')
                identifier = serializer.data.get('identifier')
                return Response({'content':result,'identifier':identifier}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error':'In valid token passed'}, status=status.HTTP_400_BAD_REQUEST)
    
class GoogleAdsHeadline(APIView): 
    def post(self, request, *args, **kwargs):
        '''
        Create the Google Ads Headline with given data
        '''
        if request.META.get('HTTP_AUTHORIZATION') == f'Bearer {settings.token}':
            ad_type = 'google_ad_headline'
            prompt_collection = prompt_collection = PromptSelector.objects.filter(adType=ad_type)
            prompt = prompt_selector(ad_type,request.data,prompt_collection)
            # calling openAI api to generate ads
            content = ads_generator.generate_ads(prompt,settings.openAIkey)
            data = {
                'productName': request.data.get('productName'), 
                'productDescription': request.data.get('productDescription'), 
                'tone': request.data.get('tone'),
                'adType':ad_type,
                'prompt': prompt,
                'content': content,
                'identifier':request.data.get('identifier')
            }
            serializer = GoogleAdsHeadlineSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                result = serializer.data.get('content')
                identifier = serializer.data.get('identifier')
                return Response({'content':result,'identifier':identifier}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error':'In valid token passed'}, status=status.HTTP_400_BAD_REQUEST)