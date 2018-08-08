class Weather:
    def __init__(self, weatherData):
        self.currentTemperature = weatherData["currently"]["temperature"]