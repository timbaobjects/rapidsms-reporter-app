from django.db import models
try:
	from mptt.models import MPTTModel, TreeForeignKey
except ImportError:
	raise ImportError('django-mptt is a requirement for this app')

class ReporterGroup(MPTTModel):
	title = models.CharField(max_length=160)
	description = models.TextField(blank=True)
	parent = TreeForeignKey('self', blank=True, null=True, related_name='children')

	def __unicode__(self):
		return self.title
	
	def members(self):
		return self.reporters.all()