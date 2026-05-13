"""
zones.the_void.objects
──────────────────────
Object templates for The Void zone.

Add an entry to TEMPLATES for every object that can appear in this zone.
The "class" key picks the instantiation class (Object / Item / Weapon).
Omitting "class" defaults to Object.

Call spawn(key) to get a fresh independent instance.
"""

from ashenmoor.world import Object, Item, Weapon
from ashenmoor.world.zone import make_spawner

TEMPLATES: dict[str, dict] = {
    "green_marker": {
        "spawn_as":         Object,
        "name":             "a &ggreen expo marker&N",
        "key_words":        ("green", "expo", "marker"),
        "room_description": "a {g&wgreen expo marker&N has been carelessly discarded here.",
        "description":      "A forest green low-scent dry-erase marker, about half used.",
    },

    "sack_of_darkness": {
        "spawn_as":         Item,
        "name":             "a sack of darkness",
        "key_words":        ("darkness", "sack"),
        "room_description": "A plain looking sack lies on the ground.",
        "description":      "The bag looks simple. It is a brown canvas. When you look inside you see a black void.",
        "weight":           2,
    },
    "windsong" : {
        "spawn_as":         Weapon,
        'name': "&+ga &wg&Wl&wi&Wtt&wer&Wi&wng &N&+gelven scimitar&N",
        'key_words': ('scimitar', 'elven', 'glittering'),
        'room_description': "&+gA glittering elven scimitar is lying on the ground here.&N",
        'description': """&+gIts blade encrusted with diamond dust, this magically light
&+gelven blade glitters in the sunlight and seems to hum softly
&+gwhen wielded in battle.&N""",
        "weight":           3,
        "dice":             "2d8",
        "hitroll":          2,
        "damroll":          4,
    },

}

# Module-level spawn — rooms.py calls  O.spawn("red_marker")
spawn = make_spawner(TEMPLATES, lambda: Object)
