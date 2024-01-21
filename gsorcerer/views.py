from django.shortcuts import render
from .helpers import get_organizations_info
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

def index(request):
    organizations = get_organizations_info(year=2023,filter='github')

    # print(contributers)
    return render(request, 'gsorcerer/index.html', {
        'organizations': organizations
    })