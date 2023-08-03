from django.contrib import admin
from .models import FacebookAds, GoogleAds, PromptSelector

@admin.register(FacebookAds)
class FacebookAdsAdmin(admin.ModelAdmin):
    list_filter = ["identifier"]


@admin.register(GoogleAds)
class GoogleAdsAdmin(admin.ModelAdmin):
    list_filter = ["identifier"]

@admin.register(PromptSelector)
class PromptSelectorAdmin(admin.ModelAdmin):
    list_filter = ["adType"]
    def render_change_form(self, request, context, *args, **kwargs):
        form_instance = context['adminform'].form
        placeholder = '''FACEBOOK ADS EXAMPLE: Here's a 10 Facebook ad headline prompt that incorporates the elements you mentioned:\n"Get ready for [Occasion] with [Product Name] - [Promotion]!"\n[Product Description] just got even better, and we can't wait to share it with you. Whether you're looking for a [Tone] twist on [Occasion] or simply want to make a statement, [Product/Brand Name] has you covered. Hurry, limited stock available!\nFeel free to customize the prompt by replacing the placeholders with your specific details. Let me know if there's anything else I can assist you with!
        \nGOOGLE ADS EXAMPLE:\nCreate google ads description with product name [Product Name]!\n[Product Description] just got even better, and we can't wait to share it with you. \nWhether you're looking for a [Tone] tone'''
        form_instance.fields['prompt'].widget.attrs['placeholder'] = placeholder
        return super().render_change_form(request, context, *args, **kwargs)

admin.site.site_header = "Accelmatic | Ad Tools"
admin.site.site_title = "Accelmatic | Ad Tools"
admin.site.index_title = "Admin Panel for Ad Tools"


