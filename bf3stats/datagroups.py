
from bf3stats.utils import _to_str


class objDict(object):
    def __init__(self, d):
        for k, v in d.iteritems():
            if isinstance(v, dict):
                setattr(self, _to_str(k).title(), objDict(v))
            else:
                setattr(self, _to_str(k), v)

class DataGroup(object):

    def __init__(self):
        #self.list = []
        pass


class Onlinestats(DataGroup):

    @classmethod
    def _parse(self, data):
        if data['status'] == 'ok':
            onlinestats = objDict(data)
        elif data['status'] == 'error':
            pass

        return onlinestats


class Player(DataGroup):

    @classmethod
    def _parse(self, data):
        #player = Player()
        #for key, value in data.items():
        #    if key == 'stats':
        #        stats = objDict(data['stats'])
        #        setattr(player, 'Stats', stats)
        #    if key != 'stats':
        #        setattr(player, key, value)
        if data['status'] == 'data':
            player = objDict(data)

            setattr(player, '_asDict', data)
            return player


