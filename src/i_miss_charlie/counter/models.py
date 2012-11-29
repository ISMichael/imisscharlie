from django.db import models

class Visit(models.Model):
	visit_date = models.DateTimeField()
	def __unicode__(self):
        	return self.question
