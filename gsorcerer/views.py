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
    
def organization(request, org_slug):
    organization = Organization.objects.get(slug=org_slug)
    print(organization)
    return render(request, 'gsorcerer/organization.html', {
        'organization': organization
    })
    
def update_db():
    data = get_organizations_info("2023", "github")
    for org in data:
        org_obj = Organization.objects.create(
            name=org["name"],
            slug=org["slug"].replace(" ", "-").lower(),
            logo_url=org["logo_url"],
            website_url=org["website_url"],
            tagline=org["tagline"],
            description=org["description"],
            source_code=org["source_code"],
            year=2023
        )
        for cat in org["categories"]:
            cat_obj = Categories.objects.create(
                name=org_obj,
                category=cat
            )
            cat_obj.save()
        for tech in org["tech_tags"]:
            tech_obj = TechnologyTags.objects.create(
                name=org_obj,
                tech_tag=tech
            )
            tech_obj.save()
        for topic in org["topic_tags"]:
            topic_obj = TopicTags.objects.create(
                name=org_obj,
                topic_tag=topic
            )
            topic_obj.save()
        org_obj.save()
    
 