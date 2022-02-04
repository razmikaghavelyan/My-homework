class Country:
    def __init__(self, country_name, continent):
        self.country_name = country_name
        self.continent = continent

    def continent_return(self):
        return f"Name of country is {self.country_name} and continent {self.continent}."


my_country = Country("USA", "North America")
print(my_country.continent_return())


class Brand:
    def __init__(self, brand_name, business_date):
        self.brand_name = brand_name
        self.business_date = business_date

    def presentation(self):
        return f"My brand name is {self.brand_name} and I start my business {self.business_date}."


my_business = Brand("Star Inc", "2022.01.24" )
print(my_business.presentation())


class Season:
    def __init__(self, season_name, avarage_temp):
        self.season_name = season_name
        self.avarage_temp = avarage_temp

    def present(self):
        return f"In season {self.season_name} average temp is {self.avarage_temp}."


my_season = Season("Summer", 35)
print(my_season.present())

#
class Product(Country, Brand, Season):
    def __init__(
            self, country_name, continent,
            brand_name, business_date,
            season_name, avarage_temp,
            product_name, type, price, quantity
    ):
        Country.__init__(self, country_name, continent)
        Brand.__init__(self, brand_name, business_date)
        Season.__init__(self, season_name, avarage_temp)
        self.product_name = product_name
        self.type = type
        self.price = price
        self.quantity = quantity

    def present_product(self):
        return f"My product name is {self.product_name},{self.country_name} his type {self.type}.It coast {self.price}$ for {self.quantity} piece."

    def discount(self, percent):
        return f"With {percent}% discount it cost {self.price - ((self.price*percent) / 100)}."

    def increase_quantity(self, new_quantity):
        self.quantity += new_quantity
        return f"New quantity of product is {self.quantity}."

    def decrease_quantity(self, new_quant):
        self.quantity -= new_quant
        return f"New quantity of product is {self.quantity}."


my_product = Product("USA", "North America", "Star Inc", "2022.01.24", "Summer", 35, "Vision Pro", "glasses", 200, 1)
print(my_product.present_product())

class Hotel(object):
    def __init__(self, hotel_name, place, room_mid_quant,  room_mid_price, lux_room_quant , lux_room_price, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.hotel_name = hotel_name
        self.place = place
        self.room_mid_price = room_mid_price
        self.lux_room_price = lux_room_price
        self.room_mid = {}
        for i in range(1, room_mid_quant +1):
            self.room_mid[f"room_{i}"] = "free"
        self.lux_room = {}
        for u in range(1, lux_room_quant +1):
            self.lux_room[f"lux_room_{u}"] = "free"

    def present(self):
        count_room = 0
        for k,v in self.room_mid.items():
            if v == "free":
                count_room += 1

        count_lux_room = 0
        for k, v in self.lux_room.items():
            if v == "free":
                count_lux_room += 1

        return f"Welcome to {self.hotel_name} in {self.place}.We glad to see you here. We have mid rooms amount {count_room}" \
               f" and lux room {count_lux_room}." \
               f"\nMid rooms coast {self.room_mid_price} and for lux {self.lux_room_price}"

    def booking(self, room_class, number_of_room):
        if type(room_class) is int or room_class != "mid" and room_class != "lux":
            raise ValueError("Give me mid or lux")

        if room_class == "mid":
            number = f"room_{number_of_room}"
            if number_of_room > len(self.room_mid) :
                raise TypeError(f"We have {len(self.room_mid)} rooms, please choose one of it")

            if self.room_mid[number] == "bussy":
                print("This room is bussy, please choose another one")
            else:
                self.room_mid[number] = "bussy"
        if room_class == "lux":
            number = f"lux_room_{number_of_room}"
            if number_of_room > len(self.lux_room) :
                raise TypeError(f"We have {len(self.lux_room)} rooms, please choose one of it")

            if self.lux_room[number] == "bussy":
                print("This room is bussy, please choose another one")
            else:
                self.lux_room[number] = "bussy"

    def room_check(self):
        free_mid_rooms = 0
        for k, v in self.room_mid.items():
            if v == "free":
                free_mid_rooms += 1

        free_lux_rooms = 0
        for u, i in self.lux_room.items():
            if i == "free":
                free_lux_rooms += 1
        return f"Quantity free lux rooms is {free_lux_rooms}.Quantity free mid rooms is {free_mid_rooms}"

    def discount(self):
        return f"I give you 20% discount if you booking room for 5 days." \
               f"It coast {self.lux_room_price - (self.lux_room_price * 20) /100} for lux room" \
               f"and for mid room {self.room_mid_price - (self.room_mid_price * 20) /100}"



class Taxi:
    def __init__(self, taxi_name, car_types, price_for_tour, *args, **kwargs):
        super().__init__(*args, *kwargs)
        self.taxi_name = taxi_name
        self.car_types = car_types
        self.price_for_tour = price_for_tour

    def present(self):
        return f"Taxi's name is {self.taxi_name}. We drive {self.car_types}. For tour it coast{self.price_for_tour}"

    def discount(self):
        return f"If i drive more than 5km i give you discount." \
               f"It wiil be {self.price_for_tour - (self.price_for_tour * 20) / 100}"


class Tour(Hotel, Taxi):
    def __init__(self, price_for_tour, tour_name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tour_name = tour_name
        self.price_for_tour = price_for_tour
        self.price_lux = self.lux_room_price + self.price_for_tour
        self.price_mid = self.room_mid_price + self.price_for_tour

    def tour_from_me(self):
        return f"Tour\n{self.tour_name} tour\nprice lux {self.price_lux} and price mid{self.price_mid}" \
               f"including\ntaxi\ntype of car {self.car_types}\nprice for a tip {self.price_for_tour}" \
               f"hotel\n{self.hotel_name}\nplace {self.place}\nrooms {self.room_mid}\nand rooms{self.lux_room}" \
               f"\nprice for lux {self.price_lux} price for mid {self.room_mid_price}"

print(Tour.__mro__)
my_tour = Tour(100, "Little Tai", "Bali", "Thailand", 5, 500, 3, 1000, "Pantera", "Comfort", 50,)
print(my_tour.tour_from_me())