from django.test import TestCase
from django.test.client import Client
from gleeoke.models import *
from django.utils import simplejson

class VotingTests(TestCase):
    
    fixtures = ['inital_data.json']
    
    def test_voting(self):
        
        def test_vote(badsong, worsesong):
            c = Client()
            vote = c.post('/vote', {'badsong': badsong.short_id, 'worsesong': worsesong.short_id})
            self.assertEquals(vote.status_code, 200)
            vote_json = simplejson.loads(vote.content)
            self.assertEquals('left' in vote_json, True)
            self.assertEquals('right' in vote_json, True)
             
        #Kill all votes
        for vote in Vote.objects.all():
            vote.delete()
            
        self.assertEquals(Vote.objects.count(), 0)
        
        random_songs = Song.objects.order_by('?')
        
        song1 = random_songs[0]
        song2 = random_songs[1]
        song3 = random_songs[2]
        
        print("song1: %s" % song1)
        print("song2: %s" % song2)
        print("song3: %s" % song3)
        
        #Test the random songs
        test_vote(song2, song1)
        
        self.assertEquals(song1.worsevotes.count(),1)
        self.assertEquals(song1.badvotes.count(),0)   
        self.assertEquals(song2.worsevotes.count(),0)
        self.assertEquals(song2.badvotes.count(),1)
        self.assertEquals(song3.worsevotes.count(),0)
        self.assertEquals(song3.badvotes.count(),0)
        
        #Check the rankings
        client = Client()
        rankings_page = client.get('/rankings')
        rankings = rankings_page.context['songs']
        self.assertEquals(rankings[0],song1)
        
        #Vote again
        test_vote(song2, song1)
        
        self.assertEquals(song1.worsevotes.count(),2)
        self.assertEquals(song1.badvotes.count(),0)   
        self.assertEquals(song2.worsevotes.count(),0)
        self.assertEquals(song2.badvotes.count(),2)
        self.assertEquals(song3.worsevotes.count(),0)
        self.assertEquals(song3.badvotes.count(),0)
        
        #Check the rankings again
        client = Client()
        rankings_page = client.get('/rankings')
        rankings = rankings_page.context['songs']
        self.assertEquals(rankings[0],song1)
        
        #Vote the other way
        test_vote(song1, song2)
        
        self.assertEquals(song1.worsevotes.count(),2)
        self.assertEquals(song1.badvotes.count(),1)   
        self.assertEquals(song2.worsevotes.count(),1)
        self.assertEquals(song2.badvotes.count(),2)
        self.assertEquals(song3.worsevotes.count(),0)
        self.assertEquals(song3.badvotes.count(),0)
        
        #Check the rankings yet again
        client = Client()
        rankings_page = client.get('/rankings')
        rankings = rankings_page.context['songs']
        self.assertEquals(rankings[0],song1)
        self.assertEquals(rankings[1],song2)
        
        #Add a third vote
        test_vote(song2, song3)
        
        self.assertEquals(song1.worsevotes.count(),2)
        self.assertEquals(song1.badvotes.count(),1)   
        self.assertEquals(song2.worsevotes.count(),1)
        self.assertEquals(song2.badvotes.count(),3)
        self.assertEquals(song3.worsevotes.count(),1)
        self.assertEquals(song3.badvotes.count(),0)

        #Check the rankings yet again
        client = Client()
        rankings_page = client.get('/rankings')
        rankings = rankings_page.context['songs']
        self.assertEquals(rankings[0],song1)
        self.assertEquals(rankings[1],song3)
        self.assertEquals(rankings[1],song2)