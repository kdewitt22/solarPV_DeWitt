from django.db import models
from django.forms import ModelForm
import datetime
from datetime import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.question_text
def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
was_published_recently.admin_order_field = 'pub_date'
was_published_recently.boolean = True
was_published_recently.short_description = 'Published recently?'
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

class Client (models.Model):
    clientCode = models.CharField(max_length=8)
    clientName = models.CharField(max_length=10)
    clientType = models.CharField(max_length=10)

class Product(models.Model):
    prodName = models.CharField(max_length=20)
    cellTech = models.CharField(max_length=20)
    cellManuf = models.CharField(max_length=20)
    numCells = models.CharField(max_length=20)
    numCellsSeries = models.CharField(max_length=20)
    numSeriesStrings = models.CharField(max_length=20)
    numDiodes = models.CharField(max_length=20)
    prodLength = models.CharField(max_length=20)
    prodWidth = models.CharField(max_length=20)
    superstrateType = models.CharField(max_length=20)
    superstrateManuf = models.CharField(max_length=20)
    substrateType = models.CharField(max_length=20)
    substrateManuf = models.CharField(max_length=20)
    frameType = models.CharField(max_length=20)
    frameAdhesive = models.CharField(max_length=20)
    encapsulantType = models.CharField(max_length=20)
    encapsulatManuf = models.CharField(max_length=20)
    junctionBoxType = models.CharField(max_length=20)
    junctionBoxManuf = models.CharField(max_length=20)

class Location(models.Model):
    address1 = models.CharField(max_length=10)
    address2= models.CharField(max_length=10)
    city = models.CharField(max_length=10)
    postalCode = models.CharField(max_length=10)
    country = models.CharField(max_length=10)
    phoneNumber = models.CharField(max_length=15)
    faxNumber = models.CharField(max_length=15)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

class TestStandard(models.Model):
    testStandName = models.CharField(max_length=20)
    testStandDesc = models.CharField(max_length=255)
    testStandPubDate = models.CharField(max_length=10)

#############################
#####Client from Dashboard####
#############################

class Certificate(models.Model):
    certID = models.CharField(max_length=8)
    reportNum = models.CharField(max_length=8)
    issueDate = models.CharField(max_length=10)
    testStandard = models.ForeignKey(TestStandard, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    modelNum = models.ForeignKey(Product, on_delete=models.CASCADE)

class CertificateForm(ModelForm):
    class Meta:
        model = Certificate
        fields = ['certID', 'reportNum', 'issueDate', 
        'testStandard', 'location', 'modelNum']
    certID = models.CharField(max_length=8)
    reportNum = models.CharField(max_length=8)
    issueDate = models.CharField(max_length=10)
    testStandard = models.ForeignKey(TestStandard, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    modelNum = models.ForeignKey(Product, on_delete=models.CASCADE)