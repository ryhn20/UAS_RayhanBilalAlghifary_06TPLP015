import matplotlib.pyplot as plt

class BaseFuzzy:
    def __init__(self):
        self.minimum = 0
        self.maximum = 0

    def up(self):
        pass

    def down(self):
        pass


class Pressure(BaseFuzzy):
    def __init__(self):
        super().__init__()
        self.minimum = 0
        self.maximum = 50  # Ubah nilai maximum sesuai kebutuhan

        self.p1 = 5
        self.p2 = 8
        self.p3 = 15
        self.p4 = 20
        self.p5 = 28
        self.p6 = 30
        self.p7 = 37
        self.p8 = 40
        self.p9 = 47

    def very_low(self, pressure):
        if pressure <= self.p1:
            return 1
        elif pressure <= self.p3:
            return (self.p3 - pressure) / (self.p3 - self.p1)
        else:
            return 0

    def low(self, pressure):
        if pressure <= self.p2:
            return 0
        elif pressure <= self.p4:
            return (pressure - self.p2) / (self.p4 - self.p2)
        else:
            return 0

    def medium(self, pressure):
        if pressure <= self.p3 or pressure > self.p7:
            return 0
        elif pressure <= self.p5:
            return (pressure - self.p3) / (self.p5 - self.p3)
        elif pressure <= self.p6:
            return 1
        elif pressure <= self.p7:
            return (self.p7 - pressure) / (self.p7 - self.p6)
        else:
            return 0

    def high(self, pressure):
        if pressure <= self.p6 or pressure > self.p9:
            return 0
        elif pressure <= self.p8:
            return (pressure - self.p6) / (self.p8 - self.p6)
        elif pressure <= self.p9:
            return 1
        else:
            return 0

    def very_high(self, pressure):
        if pressure <= self.p8:
            return 0
        elif pressure <= self.p9:
            return (pressure - self.p8) / (self.p9 - self.p8)
        else:
            return 0

    def graph(self, ax):
        x = list(range(self.minimum, self.maximum+1))
        y_low = [self.low(p) for p in x]
        y_medium = [self.medium(p) for p in x]
        y_high = [self.high(p) for p in x]

        ax.plot(x, y_low, label='Low')
        ax.plot(x, y_medium, label='Medium')
        ax.plot(x, y_high, label='High')

        ax.set_xlabel('Pressure')
        ax.set_ylabel('Membership')
        ax.set_title('Pressure Membership Functions')
        ax.legend()
        ax.grid(True)


class suhu():
    def __init__(self):
        self.minimum = 0
        self.maximum = 0

    def up(self, x):
        return (x - self.minimum) / (self.maximum - self.minimum)

    def down(self, x):
        return (self.maximum - x) / (self.maximum - self.minimum)


class Suhu_Input(suhu):
    def __init__(self):
        super().__init__()
        self.minimum = 0
        self.maximum = 50

    def very_cold(self, temperature):
        if temperature <= 10:
            return 1
        elif temperature <= 20:
            return (20 - temperature) / (20 - 10)
        else:
            return 0

    def cold(self, temperature):
        if temperature <= 10 or temperature >= 30:
            return 0
        elif temperature <= 20:
            return (temperature - 10) / (20 - 10)
        elif temperature < 30:
            return (30 - temperature) / (30 - 20)

    def warm(self, temperature):
        if temperature <= 20 or temperature >= 40:
            return 0
        elif temperature <= 30:
            return (temperature - 20) / (30 - 20)
        elif temperature < 40:
            return (40 - temperature) / (40 - 30)

    def hot(self, temperature):
        if temperature <= 30 or temperature >= 50:
            return 0
        elif temperature <= 40:
            return (temperature - 30) / (40 - 30)
        elif temperature < 50:
            return (50 - temperature) / (50 - 40)

    def very_hot(self, temperature):
        if temperature <= 40:
            return 0
        elif temperature <= 50:
            return (temperature - 40) / (50 - 40)
        else:
            return 1

    def graph(self, ax):
        x = list(range(self.minimum, self.maximum+1))
        y_very_cold = [self.very_cold(t) for t in x]
        y_cold = [self.cold(t) for t in x]
        y_warm = [self.warm(t) for t in x]
        y_hot = [self.hot(t) for t in x]
        y_very_hot = [self.very_hot(t) for t in x]

        ax.plot(x, y_very_cold, label='Very Cold')
        ax.plot(x, y_cold, label='Cold')
        ax.plot(x, y_warm, label='Warm')
        ax.plot(x, y_hot, label='Hot')
        ax.plot(x, y_very_hot, label='Very Hot')

        ax.set_xlabel('Temperature')
        ax.set_ylabel('Membership')
        ax.set_title('Temperature Membership Functions')
        ax.legend()
        ax.grid(True)


class Speed_Output(BaseFuzzy):
    def __init__(self):
        super().__init__()
        self.minimum = 0
        self.maximum = 130

    def slow(self, speed):
        if speed <= 40:
            return 1
        elif speed <= 60:
            return (60 - speed) / (60 - 40)
        else:
            return 0

    def medium(self, speed):
        if speed <= 40 or speed >= 100:
            return 0
        elif speed <= 60:
            return (speed - 40) / (60 - 40)
        elif speed <= 80:
            return 1
        elif speed <= 100:
            return (100 - speed) / (100 - 80)

    def fast(self, speed):
        if speed <= 80:
            return 0
        elif speed <= 100:
            return (speed - 80) / (100 - 80)
        else:
            return 1

    def graph(self, ax):
        x = list(range(self.minimum, self.maximum+1))
        y_slow = [self.slow(s) for s in x]
        y_medium = [self.medium(s) for s in x]
        y_fast = [self.fast(s) for s in x]

        ax.plot(x, y_slow, label='Slow')
        ax.plot(x, y_medium, label='Medium')
        ax.plot(x, y_fast, label='Fast')

        ax.set_xlabel('Speed')
        ax.set_ylabel('Membership')
        ax.set_title('Speed Membership Functions')
        ax.legend()
        ax.grid(True)


if __name__ == "__main__":
    fig, axs = plt.subplots(1, 3, figsize=(15, 5))

    temperature_input = Suhu_Input()
    pressure_input = Pressure()
    speed_output = Speed_Output()

    temperature_input.graph(axs[0])
    pressure_input.graph(axs[1])
    speed_output.graph(axs[2])

    plt.tight_layout()
    plt.show()