# Moon phase
from moon.dialamoon import Moon

def get_moon_phase_name():
    moon = Moon()
    moon.set_moon_phase()
    return moon.phase_name  # returns something like "Full Moon"
