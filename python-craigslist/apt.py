from craigslist import CraigslistHousing
from geopy.geocoders import Nominatim

class Apartment(object):
    def __init__(self, result):
        self.name = result['name']
        self.url = result['url']
        if result['price'] is None:
            self.price = 0
        else:
            self.price = result['price']
        self.geotag = result['geotag']

    def __dist__(self, location):
        return 1

def _get_office_location(addr):
    geolocator = Nominatim()
    location = geolocator.geocode(addr)
    print((location.latitude, location.longitude))

apt_list = list()

def _get_apt_list(my_site, my_area, max):
    cl_h = CraigslistHousing(site=my_site, area=my_area, category='roo',
                             filters={'private_room': True, 'has_image': True})

    count = 0
    for result in cl_h.get_results(sort_by='newest', geotagged=True):
        count += 1
        if count >= max:
            break
        else:
            print result
            #apt_list.append(Apartment(result))



def main():
    # print('main')
    # my_site = 'vancouver'
    # my_area = 'van'
    # _get_apt_list(my_site, my_area, 2)

    addr = "175 5th Avenue NYC"
    _get_office_location(addr)

if __name__ == '__main__':
    main()