from abc import abstractmethod


class FlyBehavior:
    @abstractmethod
    def fly(self):
        raise NotImplementedError()


class FlyWithWings(FlyBehavior):
    def fly(self):
        print("Flying with wings")


class FlyNoWay(FlyBehavior):
    def fly(self):
        print("Cannot fly")


class FlyWithDroneSupport(FlyBehavior):
    def fly(self):
        print("Flying with drone support")


class QuackBehavior:
    @abstractmethod
    def quack(self):
        raise NotImplementedError()


class Quack(QuackBehavior):
    def quack(self):
        print("Quack")


class Squeak(QuackBehavior):
    def quack(self):
        print("Squeak")


class Mute(QuackBehavior):
    def quack(self):
        print("")


class Duck:
    def __init__(self):
        self.type = ""
        self.fly_behavior = None
        self.quack_behavior = None

    def quack(self):
        self.quack_behavior.quack()

    def swim(self):
        print("Duck is swimming")

    def fly(self):
        if self.fly_behavior is not None:
            self.fly_behavior.fly()

    @abstractmethod
    def display(self):
        raise NotImplementedError()


class Mallard(Duck):
    def __init__(self):
        self.type = "Mallard"
        self.fly_behavior = FlyWithWings()
        self.quack_behavior = Quack()

    def display(self):
        print("MALLARD DUCK")


class Redhead(Duck):
    def __init__(self):
        self.type = "Redhead"
        self.fly_behavior = FlyWithWings()
        self.quack_behavior = Quack()

    def display(self):
        print("REDHEAD DUCK")



class Alabio(Duck):
    def __init__(self):
        self.type = "Alabio"
        self.fly_behavior = FlyWithWings()
        self.quack_behavior = Quack()

    def display(self):
        print("ALABIO DUCK")


class Rubber(Duck):
    def __init__(self):
        self.type = "Rubber"
        self.fly_behavior = FlyNoWay()
        self.quack_behavior = Squeak()

    def display(self):
        print("RUBBER DUCK")


class Decoy(Duck):
    def __init__(self):
        self.type = "Decoy"
        self.fly_behavior = FlyNoWay()
        self.quack_behavior = Mute()

    def display(self):
        print("DECOY DUCK")



if __name__ == '__main__':
    ducks = [Mallard(), Redhead(), Alabio(), Rubber(), Decoy()]

    ducks[1].fly_behavior = FlyWithDroneSupport()
    ducks[2].quack_behavior = Mute()

    for duck in ducks:
        duck.fly()
        duck.quack()
