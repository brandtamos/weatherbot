import darksky, weather

darkSkyWeather = darksky.getWeather()

print darkSkyWeather["currently"]["temperature"]