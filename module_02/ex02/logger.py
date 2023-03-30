import time
from random import randint
import os

def log(funct):
    def inner(*args, **kwargs):
        start_time = time.time()
        with open ("machine.log", 'a') as f:
            return_value = funct(*args, **kwargs)
            if return_value is not None:
                unit = "s"
                if ((time.time() - start_time) < 0.5):
                    unit = "ms"
                ttl = (funct.__name__.title()).replace('_', ' ')
                f.write(f"(cmaxime)Running:  {ttl}{' ' *  (17 - len(ttl))} [ exec-time = {(time.time() - start_time):02.4f} {unit} ]\n")
        return (return_value)
    return (inner)


class CoffeeMachine():

    water_level = 100

    @log
    def start_machine(self):
        if self.water_level > 20: 
            return True
        else:
            print("Please add water!")
            return False


    @log
    def boil_water(self):
        return "boiling..."


    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1 
            print(self.boil_water())
            print("Coffee is ready!")


    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")


if __name__ == "__main__":
        machine = CoffeeMachine()
        machine.start_machine()
        for i in range(0, 5):
            machine.make_coffee() 
        machine.make_coffee()
        machine.add_water(70)
