class Engine:
    def start(self):
        pass

    def stop(self):
        pass


class ElectricEngine(Engine):  # from Engine
    pass


class V8Engine(Engine):  # from Engine
    pass


class Car:
    engine_class = Engine  # simple engine class with non-args constructor

    def __init__(self):
        self.engine = self.engine_class()  # Has-A Engine

    def start(self):
        print(f'Starting engine {self.engine.__class__.__name__} for car {self.__class__.__name__}')
        self.engine.start()

    def stop(self):
        self.engine.stop()


class RaceCar(Car):  # Is-A Car
    engine_class = V8Engine


class CityCar(Car):  # Is-A Car
    engine_class = ElectricEngine


class F1Car(RaceCar):  # Is-A RaceCar and also Is-A Car
    pass  # engine_cls same as parent


class WithDefaultEngineCar(Car):  # Is-A RaceCar and also Is-A Car
    pass  # engine_cls same as Engine


def main():
    car = Car()
    racecar = RaceCar()
    citycar = CityCar()
    f1car = F1Car()
    withDefaultEngine = WithDefaultEngineCar()
    cars = [car, racecar, citycar, f1car, withDefaultEngine]

    for car in cars:
        car.start()


if __name__ == '__main__':
    main()
