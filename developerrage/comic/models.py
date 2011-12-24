from django.db import models
from datetime import datetime

class Comic(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200, null=True, blank=True)
    image = models.CharField(max_length=500)
    votes = models.PositiveIntegerField(default=0)
    approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=datetime.now)

    def image_url(self):
        return "https://s3.amazonaws.com/developerrage/%s" % self.image

    def admin_thumbnail(self):
        return u'<a href="https://s3.amazonaws.com/developerrage/%s"><img src="https://s3.amazonaws.com/developerrage/%s" height="100px" width="100px" /></a>' % (self.image, self.image)
    
    admin_thumbnail.short_description = "Thumbnail"
    admin_thumbnail.allow_tags = True;
        

    def __unicode__(self):
        return self.title
