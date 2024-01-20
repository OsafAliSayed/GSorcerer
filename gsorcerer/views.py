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
    contributors = get_organizations_info(2023).json()
    for key in contributors[0].keys():
        print(key)
    # print(contributers)
    return render(request, 'gsorcerer/index.html', {
        'contributers': contributors
    })