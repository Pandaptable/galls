import json
import random
import time
from datetime import datetime
from main import write_command, press_key
from enum import Enum

class TimeOfDay(Enum):
    Morning = 0
    Afternoon = 1
    Evening = 2
    Night = 3

class SeaWeatherCondition(Enum):
    ClearSkies = 0
    PartlyCloudy = 1
    Overcast = 2
    Fog = 3
    Rain = 4
    Thunderstorms = 5
    Windy = 6
    Calm = 7

class FishData:
    def __init__(self):
        self.Categories = []

class FishCategory:
    def __init__(self):
        self.Rarity = ""
        self.FishList = []

class Fish:
    def __init__(self):
        self.Name = ""
        self.Price = 0.0
        self.Weight = None

class FishWeight:
    def __init__(self):
        self.Min = 0.0
        self.Max = 0.0

def cast_line(username):
    time.sleep(1)
    write_command(f"say [GOFISH] ♌︎ Player {username} is casting their line...")
    press_key()
    time.sleep(1)
    weather = get_weather()
    write_command(f"say [GOFISH] >> {username}: ☁︎ You casted your line on {weather[1]} weather")
    press_key()
    time.sleep(1)
    if random.randint(0, 2) == 0:
        write_command(f"say [GOFISH] >> {username}: (ó﹏ò｡) You didnt catch anything, try again later...")
        press_key()
    else:
        fish_name, price, weight = get_fish_result(weather[0])
        write_command(f"say [GOFISH] >> {username}: 〈͜͡˒ ⋊ You caught a {fish_name}! ⚖️ It weighs {round(weight, 2)}kg and is worth around ${round(price, 2)}")
        press_key()

def load_fish_db():
    with open("fishbase.json", "r") as file:
        json_data = file.read()
        fish_data = json.loads(json_data)
    return fish_data

def get_fish_result(sea_weather):
    fish_data = load_fish_db()
    if fish_data:
        rarity_modifier = get_rarity_modifier(sea_weather)
        rarity_roll = random.random()
        chosen_rarity = choose_rarity(rarity_roll, fish_data["Categories"], rarity_modifier)

        chosen_category = next((category for category in fish_data["Categories"] if category["Rarity"] == chosen_rarity), None)
        if chosen_category:
            fish_list = chosen_category["FishList"]
            chosen_fish = random.choice(fish_list)
            random_weight = random.uniform(chosen_fish["Weight"]["Min"], chosen_fish["Weight"]["Max"])
            usd_price = chosen_fish["Price"] * random_weight
            return chosen_fish["Name"], usd_price, random_weight
    else:
        raise ValueError("fishData was null")

def get_weather():
    forecasted_weather = forecast_sea_weather()
    weather_description = get_weather_description(forecasted_weather)
    return forecasted_weather, weather_description

def forecast_sea_weather():
    current_time_of_day = get_current_time_of_day()
    base_condition = {
        TimeOfDay.Morning: SeaWeatherCondition.ClearSkies,
        TimeOfDay.Afternoon: SeaWeatherCondition.PartlyCloudy,
        TimeOfDay.Evening: SeaWeatherCondition.Overcast,
        TimeOfDay.Night: SeaWeatherCondition.ClearSkies,
    }.get(current_time_of_day, SeaWeatherCondition.ClearSkies)

    if random.random() <= 0.25:
        base_condition = random.choice(list(SeaWeatherCondition))

    return base_condition

def get_current_time_of_day():
    current_hour = datetime.now().hour

    if 6 <= current_hour < 12:
        return TimeOfDay.Morning
    elif 12 <= current_hour < 18:
        return TimeOfDay.Afternoon
    elif 18 <= current_hour < 24:
        return TimeOfDay.Evening
    else:
        return TimeOfDay.Night

def get_weather_description(condition):
    return {
        SeaWeatherCondition.ClearSkies: "Clear skies with calm seas",
        SeaWeatherCondition.PartlyCloudy: "Partly cloudy skies with gentle breeze",
        SeaWeatherCondition.Overcast: "Overcast skies with potential for rain",
        SeaWeatherCondition.Fog: "Foggy conditions with reduced visibility",
        SeaWeatherCondition.Rain: "Rainfall with choppy seas",
        SeaWeatherCondition.Thunderstorms: "Thunderstorms with rough seas and lightning",
        SeaWeatherCondition.Windy: "Windy conditions with high waves",
        SeaWeatherCondition.Calm: "Calm seas with little to no wind",
    }.get(condition, "Unknown weather condition")

def get_rarity_modifier(sea_weather):
    return {
        SeaWeatherCondition.ClearSkies: 1.0,
        SeaWeatherCondition.PartlyCloudy: 1.1,
        SeaWeatherCondition.Overcast: 1.2,
        SeaWeatherCondition.Fog: 0.8,
        SeaWeatherCondition.Rain: 0.7,
        SeaWeatherCondition.Thunderstorms: 0.5,
        SeaWeatherCondition.Windy: 0.9,
        SeaWeatherCondition.Calm: 1.1,
    }.get(sea_weather, 1.0)

def choose_rarity(roll, categories, modifier):
    cumulative_chance = 0.0
    for category in categories:
        cumulative_chance += rarity_chance(category["Rarity"]) * modifier
        if roll <= cumulative_chance:
            return category["Rarity"]
    return categories[-1]["Rarity"]

def rarity_chance(rarity):
    return {
        "Common": 0.4,
        "Uncommon": 0.3,
        "Rare": 0.2,
        "Very Rare": 0.1,
        "Epic": 0.05,
        "Legendary": 0.025,
    }.get(rarity, 0.0)
