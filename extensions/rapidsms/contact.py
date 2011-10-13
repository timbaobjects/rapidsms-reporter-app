from django.db import models
from reporter.models import ReporterGroup
from locations.models import Location

class Reporter(models.Model):
	group = models.ForeignKey(ReporterGroup, blank=True, null=True, related_name="reporters")
	location = models.ForeignKey(Location, blank=True, null=True, related_name="reporters")

	def __unicode__(self):
		return "%s" % self.pk