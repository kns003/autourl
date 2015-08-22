from django.db import models
# Create your models here.
class logs(models.Model):
	requestMethod= models.CharField(max_length=100)
	remoteAddr= models.CharField(max_length=100)
	httpRefer= models.CharField(max_length=100)
	time= models.DateTimeField(auto_now_add=True)
	headder= models.TextField()

	class Meta:
		ordering=["-time"]

	def __unicode__(self):
		return "%s-%s-%s-%s" % (self.requestMethod,self.httpRefer,self.remoteAddr,self.time)

class urls(models.Model):
	httpRefer= models.CharField(max_length=100)
	count= models.PositiveSmallIntegerField(default=0)

	class Meta:
		ordering=["-count"]

	def __unicode__(self):
		return "%s-%s" % (self.httpRefer,self.count)