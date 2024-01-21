from django.db import models

# Create your models here.
class Organization(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    logo_url = models.CharField(max_length=200)
    website_url = models.CharField(max_length=200)
    tagline = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    source_code = models.CharField(max_length=200)
    year = models.IntegerField()

    def __str__(self):
        return self.name
    
class Categories(models.Model):
    # categories foreign key from organization and one to many relation
    name = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='categ_org')
    category = models.CharField(max_length=200)
    def __str__(self):
        return self.name.name + " : " + self.category
    
class TechnologyTags(models.Model):
    # tech_tags foreign key from organization and one to many relation
    name = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='tech_org')
    tech_tag = models.CharField(max_length=200)
    def __str__(self):
        return self.name.name + " : " + self.tech_tag
class TopicTags(models.Model):
    # topic_tags foreign key from organization and one to many relation
    name = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='topic_org')
    topic_tag = models.CharField(max_length=200)    
    def __str__(self):
        return self.name.name + " : " + self.topic_tag