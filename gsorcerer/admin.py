from django.contrib import admin
from .models import Organization, Categories, TechnologyTags, TopicTags
# Register your models here.
admin.site.register(Organization)
admin.site.register(Categories)
admin.site.register(TechnologyTags)
admin.site.register(TopicTags)