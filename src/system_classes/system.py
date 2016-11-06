import collections
from star import *

class System():

    '''(System, Dictionary) -> NoneType
    Initialises the System object, which also initialises the Star
    and Planet objects.
    Requires the dictionary representation of a System
    '''
    def __init__(self, system_dict):

        self.system_dict = system_dict

        self.initialize_system_dict_values()

        # the case where there are multiple stars
        if isinstance(self.system_dict['system']['star'], list):
            self.stars = []
            for star in self.system_dict['system']['star']:
                temp_star = Star(star)
                self.stars.append(temp_star)
        else:
            self.stars = Star(self.system_dict['system']['star'])

    def initialize_system_dict_values(self):
        self.name = self.system_dict['system']['name']
        self.right_ascension = self.system_dict['system']['rightascension']
        self.declination = self.system_dict['system']['declination']

        self.distance = self.system_dict['system']['distance']['#text']
        self.distance_error_minus = self.system_dict['system'][
	    'distance']['@errorminus']
        self.distance_error_plus = self.system_dict['system'][
	    'distance']['@errorplus']

    '''(System, System) -> list(list(string))
    Takes another System and compares the values and updates it to other's
    values.
    Returns a list of all the updated values
    '''
    def update(self, other):

        updates = []
        updates += self.update_system_values(other)

        if isinstance(self.system_dict['system']['star'], list):
            for i, star in enumerate(self.stars):
                star_updates = self.star.update(other.stars[i],
		                                self.system_dict[
		                                    'system']['name'])
                updates += star_updates
        else:
            updates += self.stars.update(other.stars,
	                                     self.system_dict[
	                                         'system']['name'])
        return updates


    def update_system_values(self, other):
        updates = []
        if not self.name == other.name:
            updates.add([self.system_dict['name']])

        if not self.right_ascension == other.right_ascension:
            updates.add([self.system_dict['name'], 'rightascension'])

        if not self.declination == other.declination:
            updates.add[self.system_dict['name'], 'declination']

        if not self.distance == other.distance:
            updates.add[self.system_dict['name'], 'distance']
        if not self.distance_error_minus == other.distance_error_minus:
            updates.add([self.system_dict['name'], 'distance', '@errorminus'])
        if not self.distance_error_plus == other.distance_error_plus:
            updates.add([self.system_dict['name'], 'distance', '@errorplus'])
        return updates