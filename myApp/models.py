from django.db import models

# Create your models here.

def organizationInfoPath(instance, filename):
    folder_name = instance.orgName
    return f"{folder_name}/{filename}"


class organizationInfo(models.Model):
    orgName = models.CharField(max_length=50, verbose_name="Organization Name")
    orgEmail = models.EmailField(verbose_name="Organization Email")
    orgContact = models.CharField(max_length=14, verbose_name="Organization Contact")
    orgAddress = models.CharField(max_length=255, verbose_name="Organization Address")
    adminName = models.CharField(max_length=50, verbose_name="Admin Name")
    adminDesig = models.CharField(max_length=50, verbose_name="Admin Designation")
    adminEmail = models.EmailField(verbose_name="Admin Email")
    adminContact = models.CharField(max_length=14, verbose_name="Admin Contact")
    xmlForm = models.FileField(upload_to=organizationInfoPath, verbose_name="XML Form")


    class Meta:
        verbose_name_plural = "Organization Information"
        app_label = "myApp"

    def __str__(self):
        return self.orgName
	