from django.db import models

# Create your models here.


class Startup(models.Model):

    name = models.CharField(max_length=255)
    start = models.DateField()

    categories = (
        ('Software', "Software"),
        ('Web', 'Web'),
        ('Mobile', 'Mobile'),
        ('Enterprise', 'Enterprise'),
        ('Advertising', 'Advertising'),
        ('Gaming Co.', 'Gaming Co.'),
        ('E-ommerce', 'E-commerce'),
        ('Bio-tech', 'Bio-tech'),
        ('Consulting', 'Consulting'),
        ('Others', 'Others'),
    )
    category = models.CharField(max_length=100, choices=categories)

    relationship_num = models.IntegerField(max_length=100)
    milestones_num = models.IntegerField(max_length=100)
    first_milestone = models.DateField()
    last_milestone = models.DateField()

    total_fund = models.IntegerField()
    first_funding = models.DateField()
    last_funding = models.DateField()
    funding_round_num = models.IntegerField(max_length=100)
    has_angel = models.BooleanField(default=False)
    has_vc = models.BooleanField(default=False)

    has_A = models.BooleanField(default=False)
    has_B = models.BooleanField(default=False)
    has_C = models.BooleanField(default=False)
    has_D = models.BooleanField(default=False)

    class Meta:
        db_table = 'Startup'

    def __str__(self):
        return self.name
