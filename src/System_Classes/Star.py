import Planet

class Star():

    def __init__(self, star_dict):

        self.star_dict = star_dict

        initialize_star_dict_values()

        self.planets = []
        for planet in self.star_dict['planet']:
            temp_planet = Planet(planet)
            self.planets += temp_planet


    def initialize_star_dict_values():
        self.mag_R_error_minus = self.star_dict['magR']['@errorminus']
        self.mag_R_error_plus = self.star_dict['magR']['@errorplus']
        self.mag_R = self.star_dict['magR']

        self.mag_I_error_minus = self.star_dict['magI']['@errorminus']
        self.mag_I_error_plus = self.star_dict['magI']['@errorplus']
        self.mag_I = self.star_dict['magI']

        self.mag_H_error_minus = self.star_dict['magH']['@errorminus']
        self.mag_H_error_plus = self.star_dict['magH']['@errorplus']
        self.mag_H = self.star_dict['magH']

        self.mag_K_error_minus = self.star_dict['magK']['@errorminus']
        self.mag_K_error_plus = self.star_dict['magK']['@errorplus']
        self.mag_K = self.star_dict['magK']

        self.name = self.star_dict['name']
        self.mass = self.star_dict['mass']
        self.mass_error_minus = self.star_dict['mass']['@errorminus']
        self.mass_error_plus = self.star_dict['mass']['@errorplus']

        self.radius = self.star_dict['radius']
        self.radius_error_minus = self.star_dict['radius']['@errorminus']
        self.radius_error_plus = self.star_dict['radius']['@errorplus']

        self.temperature = self.star_dict['temperature']
        self.temperature_error_minus = self.star_dict['temperature']
        ['@errorminus']
        self.temperature_error_plus = self.star_dict['temperature']
        ['@errorplus']

        self.mag_J = self.star_dict['magJ']
        self.mag_J_error_minus = self.star_dict['magJ']['@errorminus']
        self.mag_J_error_plus = self.star_dict['magJ']['@errorplus']

        self.age = self.star_dict['age']

        self.metallicity = self.star_dict['metallicity']
        self.metallicity_error_minus = self.star_dict['metallicity']
        ['@errorminus']
        self.metallicity_error_plus = self.star_dict['metallicity']
        ['@errorplus']

        self.spectral_type = self.star_dict['spectraltype']

    '''(Star, Star) -> list(list(string))
    Takes another System and compares the values and updates it to other's
    values.
    Returns a list of all the updated values
    '''
    def update(self, other):

        updates = update_star_values(other)
        
        for planet in self.planets:
            updates.update(planet.update(planet))
        
        return updates

    def update_star_values(other):
        updates = []
        if not self.mag_R_error_minus == self.star_dict['magR']['@errorminus']:
            updates.append(['system', 'star', 'magR', '@errorminus'])
        if not self.mag_R_error_plus == self.star_dict['magR']['@errorplus']:
            updates.append(['system', 'star', 'magR', '@errorplus'])
        if not self.mag_R == self.star_dict['magR']:
            updates.append(['system', 'star', 'magR'])

        if not self.mag_I_error_minus == self.star_dict['magI']['@errorminus']:
            updates.append(['system', 'star', 'magI', '@errorminus'])
        if not self.mag_I_error_plus == self.star_dict['magI']['@errorplus']:
            updates.append(['system', 'star', 'magI', '@errorplus'])
        if not self.mag_I == self.star_dict['magI']:
            updates.append(['system', 'star', 'magI'])

        if not self.mag_H_error_minus == self.star_dict['magH']['@errorminus']:
            updates.append(['system', 'star', 'magH', '@errorminus'])
        if not self.mag_H_error_plus == self.star_dict['magH']['@errorplus']:
            updates.append(['system', 'star', 'magH','@errorplus'])
        if not self.mag_H == self.star_dict['magH']:
            updates.append(['system', 'star', 'magH'])

        if not self.mag_K_error_minus == self.star_dict['magK']['@errorminus']:
            updates.append(['system', 'star', 'magK', '@errorminus'])
        if not self.mag_K_error_plus == self.star_dict['magK']['@errorplus']:
            updates.append(['system', 'star', 'magK', '@errorplus'])
        if not self.mag_K == self.star_dict['magK']:
            updates.append(['system', 'star', 'magK'])

        if not self.name == self.star_dict['name']:
            updates.append(['system', 'star', 'name'])

        if not self.mass == self.star_dict['mass']:
            updates.append(['system', 'star', 'mass'])
        if not self.mass_error_minus == self.star_dict['mass']['@errorminus']:
            updates.append(['system', 'star', 'mass', '@errorminus'])
        if not self.mass_error_plus == self.star_dict['mass']['@errorplus']:
            updates.append(['system', 'star', 'mass', '@errorplus'])

        if not self.radius == self.star_dict['radius']:
            updates.append(['system', 'star', 'radius'])
        if not self.radius_error_minus == self.star_dict['radius'][
            '@errorminus']:
            updates.append(['system', 'star', 'radius', '@errorminus'])
        if not self.radius_error_plus == self.star_dict[
            'radius']['@errorplus']:
            updates.append(['system', 'star', 'radius', '@errorplus'])

        if not self.temperature == self.star_dict['temperature']:
            updates.append(['system', 'star', 'temperature'])
        if not self.temperature_error_minus == self.star_dict[
            'temperature']['@errorminus']:
            updates.append(['system', 'star', 'temperature', '@errorminus'])
        if not self.temperature_error_plus == self.star_dict[
            'temperature']['@errorplus']:
            updates.append(['system', 'star', 'temperature', '@errorplus'])

        if not self.mag_J == self.star_dict['magJ']:
            updates.append(['system', 'star', 'magJ'])
        if not self.mag_J_error_minus == self.star_dict['magJ']['@errorminus']:
            updates.append(['system', 'star', 'magJ', '@errorminus'])
        if not self.mag_J_error_plus == self.star_dict['magJ']['@errorplus']:
            updates.append(['system', 'star', 'magJ', '@errorplus'])

        if not self.age == self.star_dict['age']:
            updates.append(['system', 'star', 'age'])

        if not self.metallicity == self.star_dict['metallicity']:
            updates.append(['system', 'star', 'metallicity'])
        if not self.metallicity_error_minus == self.star_dict[
            'metallicity']['@errorminus']:
            updates.append(['system', 'star', 'metallicity', '@errorminus'])
        if not self.metallicity_error_plus == self.star_dict[
            'metallicity']['@errorplus']:
            updates.append(['system', 'star', 'metallicity', '@errorplus'])

        if not self.spectral_type == self.star_dict['spectraltype']:
            updates.append(['system', 'star', 'spectraltype'])