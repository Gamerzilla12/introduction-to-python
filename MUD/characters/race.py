from utils import Stats


## Base Race Class
class Race:
    def __init__(
        self,
        d={
            "stats_modifier": [1, 1, 1, 1, 1, 1],
            "innate_abilities": [],
            "size": "medium",
        },
        statlist=Stats,
    ):
        self.stats_modifiers = d["stats_modifier"]

    def get_mod(self, stat):
        if type(stat) == int:
            return self.stats_modifiers[stat]
        elif type(stat) == str:
            for k in Stats:
                if stat == k.abv:
                    return self.stats_modifiers[k.value]
        return None
