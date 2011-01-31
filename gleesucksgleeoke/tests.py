from django.test import TestCase
from django.test.client import Client
from gleeoke.models import *
from django.utils import simplejson

class VotingTests(TestCase):
    
    fixtures = ['inital_data.json']
    
    def test_voting(self):
                        
        #Kill all votes
        for vote in Vote.objects.all():
            vote.delete()
            
        self.assertEquals(Vote.objects.count(), 0)
        
        badsong, worsesong = Song.objects.order_by('?')[:1]
        
        self.test_vote(badsong, worsesong)
        
        client = Client()
        rankings_page = client.get('/ranking')
        rankings = rankings_page.context['songs']
        self.assertEquals(rankings[0],worsesong)
        
    def test_vote(badsong, worsesong):
        c = Client()
        vote = c.post('/vote', {'badsong': badsong.short_id, 'worsesong': worsesong.short_id})
        self.assertEquals(response.status_code, 200)
        vote_json = simplejson.loads(vote.content)
        self.assertIn('left',vote_json)
        self.assertIn('right',vote_json)