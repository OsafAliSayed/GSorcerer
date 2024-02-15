from django.shortcuts import render
from .helpers import get_organizations_info
from .models import Organization, Categories, TechnologyTags, TopicTags
from datetime import datetime
# Create your views here.

# name
# slug
# logo_url
# website_url
# tagline
# license
# categories
# contributor_guidance_url
# description
# tech_tags
# topic_tags
# contact_links
# source_code
# ideas_link
# direct_comm_methods
# social_comm_methods
# github token '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'
def index(request):
    organizations = Organization.objects.all()    
                
    # print(contributers)
    return render(request, 'gsorcerer/index.html', {
        'organizations': organizations
    })