import datetime
from django.db import models

# Create your models here.    

class Test(models.Model):
    id = models.BigAutoField(primary_key=True)
    test = models.CharField(verbose_name="Test", max_length=128)

    class Meta:
        managed = True
        db_table = 'testing_test'

    def __str__(self):
        return self.test


class Authorities(models.Model):
    # id = models.BigAutoField(primary_key=True, unique=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    authority = models.CharField(verbose_name="Authority", max_length=255, default="", unique=True)
    user_id = models.CharField(name="nuid", verbose_name="NUID", max_length=7, default="")
    name = models.CharField(verbose_name="First Name", max_length=255, blank=True, default="")
    middle = models.CharField(verbose_name="Middle Name", max_length=255, blank=True, default="")
    lastname = models.CharField(verbose_name="Last Name", max_length=255, blank=True, default="")
    wrk_class = models.CharField(verbose_name="Workforce Class", max_length=255, blank=True, default="")
    status = models.CharField(verbose_name="Status", max_length=255, blank=True, default="")
    company = models.CharField(verbose_name="Company Name", max_length=255, blank=True, default="")
    start_date = models.DateField(verbose_name="Start Date", default=datetime.date.fromisoformat('1900-01-01'), blank=True)
    end_date = models.DateField(verbose_name="Projected End Date", default=datetime.date.fromisoformat('1900-01-01'), blank=True) 
    region_code = models.CharField(verbose_name="Region Code", max_length=255, blank=True, default="")
    region = models.CharField(verbose_name="Region Name", max_length=255, blank=True, default="")
    entity = models.CharField(verbose_name="Entity Name", max_length=255, blank=True, default="")
    department = models.CharField(verbose_name="Department Name", max_length=255, blank=True, default="")
    location = models.CharField(verbose_name="Location Description", max_length=255, blank=True, default="")
    job_title = models.CharField(verbose_name="Job Title", max_length=255, blank=True, default="")
    job_position = models.CharField(verbose_name="Job Position", max_length=255, blank=True, default="")
    job_code = models.CharField(verbose_name="Job Code", max_length=255, blank=True, default="")
    cost_center = models.CharField(verbose_name="Cost Center Name", max_length=255, blank=True, default="")
    job_description = models.CharField(verbose_name="Job Description", max_length=255, blank=True, default="")
    address = models.CharField(verbose_name="Business Address", max_length=255, blank=True, default="")
    email = models.CharField(verbose_name="KP email address", max_length=255, blank=True, default="")
    site_id = models.CharField(verbose_name="Site ID", max_length=255, blank=True, default="")
    manager = models.CharField(verbose_name="KP Manager", max_length=255, blank=True, default="")
    institution = models.CharField(verbose_name="Institution", max_length=255, blank=True, default="")
    dor = models.CharField(verbose_name="DOR Status", max_length=255, blank=True, default="")
    is_oncologist = models.BooleanField(verbose_name="Is DOR Oncologist?", blank=True, default=False)
    

    class Meta:
        managed = True
        db_table = 'testing_authorities'
        verbose_name = "Authority"
        verbose_name_plural = "Authorities"

    def __str__(self):
        return self.authority