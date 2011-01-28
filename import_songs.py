import os
import plistlib
from gleeoke.models import *

song_folder = '/Users/chris/Development/Personal/glee_xml'

def import_songs():
    for item in os.listdir(song_folder):
        path = os.path.join(song_folder, item)
        if os.path.isfile(path):
            plist = plistlib.readPlist(path)
            song = Song()
            
            song.user_handle = plist['objects'][0]['user_handle']
            song.name = plist['objects'][0]['name']
            song.uuid = plist['objects'][0]['uuid']

            song.type = plist['objects'][0]['type']
            song.track_id = plist['objects'][0]['track_id']
            song.short_id = plist['objects'][0]['short_id']

            song.latitude = plist['objects'][0]['lat']
            song.longitude = plist['objects'][0]['long']

            song.url = plist['objects'][0]['url']
            song.url_hq = plist['objects'][0]['url_hq']
            
            song.save()
            
            for gleek in plist['objects'][0]['gleeks']:
                gleekobj = Gleek()
                
                gleekobj.song = song
                gleekobj.install_uuid = gleek['install_uuid']
                gleekobj.latitude = gleek['lat']
                gleekobj.longitude = gleek['long']
                gleekobj.user_handle = gleek['user_handle']
                
                gleekobj.save()
                
            for comment in plist['objects'][0]['comments']:
                commentobj = Comment()
                
                commentobj.song = song
                commentobj.comment = comment['comment']
                commentobj.comment_uuid = comment['comment_uuid']
                commentobj.fb_user_id = comment['fb_user_id']
                commentobj.plist_id = comment['id']
                commentobj.latitude = comment['lat']
                commentobj.longitude = comment['long']
                commentobj.user_handle = comment['user_handle']
                commentobj.save()
            
            song.save()