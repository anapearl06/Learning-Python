import arrow

brewing_time = arrow.utcnow()
brewing_time.to("Europe/Rome")

from collections import namedtuple

chai_profile = namedtuple("ChaiProfile", ["type", "size", "sugar_level", "extra_flavour"])
my_chai = chai_profile(type="Masala Chai", size="Large", sugar_level=3, extra_flavour="Ginger") 
