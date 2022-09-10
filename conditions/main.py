# Do not modify these lines
__winc_id__ = "25596924dffe436da9034d43d0af6791"
__human_name__ = "conditions"

# Add your code after this line

from importlib.resources import read_binary


def farm_action(
    weather,
    time_of_day,
    cow_milking_status,
    location_cows,
    season,
    slurry_tank,
    grass_status,
):
    if weather == "rainy":
        return True
    elif location_cows == "pasture":
        return True
