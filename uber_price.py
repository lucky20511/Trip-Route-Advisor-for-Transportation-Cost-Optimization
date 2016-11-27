from uber_rides.session import Session
from uber_rides.client import UberRidesClient
import json



#response = client.get_products(37.77, -122.41)
#products = response.json.get('products')
#class NodeUber:
    #start_x = start_y = 0.0
    #end_x = end_y = 0.0
    #def __init__(self, xs, ys, xe, ye):
        #self.start_x = xs
        #self.start_y = ys
        #self.end_x = xe
        #self.end_y = ye
def uber(start_x, start_y, end_x, end_y):
    session = Session(server_token='bMyGEqYLPAovFbljyM2GUK3zFHaiOPS1u2sT7-K0')
    client = UberRidesClient(session)
    response = client.get_price_estimates(
        start_latitude=start_x,
        start_longitude=start_y,
        end_latitude=end_x,
        end_longitude=end_y,
        seat_count=1
    )

    estimate = response.json.get('prices')

    #cheap_uber = estimate[0];
    price_uber = (estimate[0]['high_estimate'] + estimate[0]['low_estimate']) / 2
    currency_uber = estimate[0]['currency_code']
    duration_uber = estimate[0]['duration'] / 60
    distance_uber = estimate[0]['distance']


    res = { "name" : "Uber",
            "total_costs_by_cheapest_car_type" : price_uber,
            "currency_code": currency_uber,
            "total_duration" : duration_uber,
            "duration_unit": "minute",
            "total_distance" : distance_uber,
            "distance_unit": "mile"
    }

    return res
    #print res