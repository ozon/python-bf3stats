from unittest import TestCase
from StringIO import StringIO
import urllib
from bf3stats.api import API

# patch urllib.urlopen so we make sure our tests won't really make http calls
def urlopen_mock(*args, **kwargs):
    return StringIO("{}")

original_urlopen = urllib.urlopen
def setUp():
    urllib.urlopen = urlopen_mock

def tearDown():
    urllib.urlopen = original_urlopen


class Test_without_ident(TestCase):
    """Just make sure no python error occurs while calling our API methods while not providing ident/secret"""

    def setUp(self):
        self.api = API(ident=None, secret=None)

    def test_playerlist(self):
        self.api.playerlist(players="foo,bar")

    def test_call_player(self):
        self.api.player(player_name='f00')
        self.api.player(player_name='f00', parts='clear,score')

    def test_dogtags(self):
        self.api.dogtags(player_name="f00")

    def test_onlinestats(self):
        self.api.onlinestats()

    def test_playerupdate(self):
        self.assertRaises(AssertionError, self.api.playerupdate, player_name="f00")

    def test_playerlookup(self):
        self.assertRaises(AssertionError, self.api.playerlookup, player_name="f00")

    def test_setupkey(self):
        self.assertRaises(AssertionError, self.api.setupkey, client_ident="f00", name='bar')

    def test_getkey(self):
        self.assertRaises(AssertionError, self.api.getkey, client_ident="f00")



class Test_with_ident(TestCase):
    """Just make sure no python error occurs while calling our API methods while providing ident/secret"""

    def setUp(self):
        self.api = API(ident='myidentity', secret='mysecret')

    def test_playerlist(self):
        self.api.playerlist(players="foo,bar")

    def test_call_player(self):
        self.api.player(player_name='f00')
        self.api.player(player_name='f00', parts='clear,score')

    def test_dogtags(self):
        self.api.dogtags(player_name="f00")

    def test_onlinestats(self):
        self.api.onlinestats()

    def test_playerupdate(self):
        self.api.playerupdate(player_name="f00")

    def test_playerlookup(self):
        self.api.playerlookup(player_name="f00")

    def test_setupkey(self):
        self.api.setupkey(client_ident="f00", name='bar')

    def test_getkey(self):
        self.api.getkey(client_ident="f00")