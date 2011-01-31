from django.db import models
from django.contrib.auth.models import User

class Song(models.Model):
    """A Gleeoke Song"""
    
    user_handle = models.CharField(blank=True, max_length=255)
    name = models.CharField(blank=True, max_length=255)
    uuid = models.CharField(blank=True, max_length=255)
    
    type = models.IntegerField()
    track_id = models.IntegerField()
    short_id = models.IntegerField()
    
    latitude = models.FloatField()
    longitude = models.FloatField()
        
    url = models.URLField(blank=True, verify_exists=False)
    url_hq = models.URLField(blank=True, verify_exists=False)
    
    class Meta:
        pass

    def mpeg_url(self):
        return ("/media/songs/solo_%s/%s_s.m4a" % (self.short_id, self.uuid))

    def __unicode__(self):
        return self.name
        
class Vote(models.Model):
    badsong = models.ForeignKey(Song, related_name='badvotes')
    worsesong = models.ForeignKey(Song, related_name='worsevotes')
    
    def __unicode__(self):
        return '"%s" over "%s"' % (self.badsong, self.worsesong)

class Gleek(models.Model):
    """Gleek"""
    
    song = models.ForeignKey(Song)
    install_uuid = models.CharField(blank=True, max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    user_handle =  models.CharField(blank=True, max_length=255)
    
    class Meta:
        pass

    def __unicode__(self):
        return self.user_handle
        
class Comment(models.Model):
    """(Comment description)"""
    
    song = models.ForeignKey(Song)
    comment = models.CharField(blank=True, max_length=255)
    comment_uuid = models.CharField(blank=True, max_length=255)
    fb_user_id = models.CharField(blank=True, max_length=255)
    plist_id = models.IntegerField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    user_handle =  models.CharField(blank=True, max_length=255)
    
    class Meta:
        pass

    def __unicode__(self):
        return self.comment
