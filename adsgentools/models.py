from django.db import models
from django.utils.translation import gettext_lazy as _

TYPE_CHOICES = (
    ('default','.......'),
    ('facebook_ad_copy','Facebook Ad Copy'),
    ('facebook_ad_headline', 'Facebook Ad headline'),
    ('google_ad_headline', 'Google Ad headline'),
    ('google_ad_description', 'Google Ad Description'),
)

class FacebookAds(models.Model):
    productName = models.CharField(verbose_name=_('Product/Brand Name'), max_length=100)
    productDescription = models.TextField(verbose_name=_("Product Description"))
    occasion = models.CharField(verbose_name=_("Occasion"), max_length=100, null=True, blank=True)
    promotion = models.CharField(verbose_name=_("Promotion"), max_length=100, null=True, blank=True)
    tone = models.CharField(verbose_name=_("Choose a tone"), max_length=100, null=True, blank=True)
    adType = models.CharField(max_length=30, choices=TYPE_CHOICES, default='default')
    prompt = models.TextField(verbose_name=_("Prompt"))
    content = models.TextField(verbose_name=_("OpenAI Generated content"))
    identifier = models.CharField(verbose_name=_('Identifier'), max_length=100)
    
    def __str__(self):
        return self.productName +", looking for "+ self.adType.replace("_"," ").capitalize()   
    
    class Meta:
        verbose_name = 'Facebook Ads'
        verbose_name_plural = 'Facebook Ads'
        db_table = 'tbl_facebook_ads'

class GoogleAds(models.Model):
    productName = models.CharField(verbose_name=_('Product/Brand Name'), max_length=100)
    productDescription = models.TextField(verbose_name=_("Product Description"))
    tone = models.CharField(verbose_name=_("Choose a tone"), max_length=100, null=True, blank=True)
    adType = models.CharField(max_length=30, choices=TYPE_CHOICES, default='default')
    prompt = models.TextField(verbose_name=_("Prompt"))
    content = models.TextField(verbose_name=_("OpenAI Generated content"))
    identifier = models.CharField(verbose_name=_('Identifier'), max_length=100)
    
    def __str__(self):
        return self.productName +", looking for "+ self.adType.replace("_"," ").capitalize()
    
    class Meta:
        verbose_name = 'Google Ads'
        verbose_name_plural = 'Google Ads'
        db_table = 'tbl_google_ads'

class PromptSelector(models.Model):
    adType = models.CharField(max_length=30, choices=TYPE_CHOICES, default='default',help_text="NOTE: In Google ads only 3 field need to be added in prompt as Dynamic.")
    prompt = models.TextField(verbose_name=_("Prompt"),help_text="NOTE: Add '[]' square bracket for dynamic text change.")
    
    def __str__(self):
        return self.adType.replace("_"," ").capitalize()
    
    class Meta:
        verbose_name = 'Prompt Selector'
        verbose_name_plural = 'Prompt Selector'
        db_table = 'tblPromptSelector'
