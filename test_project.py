import pytest
from project import showActualWeather, askToContinue, make_request

def test_showActualWeather():
    data = {"location":{"name":"Minsk","region":"Minsk","country":"Belarus","lat":53.9,"lon":27.57,"tz_id":"Europe/Minsk","localtime_epoch":1695552966,"localtime":"2023-09-24 13:56"},"current":{"last_updated_epoch":1695552300,"last_updated":"2023-09-24 13:45","temp_c":16.0,"temp_f":60.8,"is_day":1,"condition":{"text":"Partly cloudy","icon":"//cdn.weatherapi.com/weather/64x64/day/116.png","code":1003},"wind_mph":9.4,"wind_kph":15.1,"wind_degree":10,"wind_dir":"N","pressure_mb":1022.0,"pressure_in":30.18,"precip_mm":0.22,"precip_in":0.01,"humidity":100,"cloud":75,"feelslike_c":16.0,"feelslike_f":60.8,"vis_km":10.0,"vis_miles":6.0,"uv":4.0,"gust_mph":9.4,"gust_kph":15.2}}
    showActualWeather(data)

def test_askToContinue(monkeypatch):
    def testInput(text):
        monkeypatch.setattr('builtins.input', lambda _: text)
        askToContinue()

    with pytest.raises(SystemExit):
        testInput('n')
    
    testInput('y')


def test_make_request():
    def testRequest(city, code):
        validStatusCode = make_request(city)
        assert code == validStatusCode
    
    testRequest('Minsk', 200)
    testRequest('Invalid', 400)


