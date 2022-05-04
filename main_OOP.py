from tkinter import *  # Import Tkinter
from configparser import ConfigParser
from tkinter import messagebox
import requests # This library needs to be downloaded through terminal in the IDE, With commando: pip install requests


main = Tk()  # instance of the Tkinter frame, displays main window
main.title("Weather prognosis")  # Title of the GUI
main.config(background="orange")  # Background-color of the GUI
main.geometry("500x250")  # Dimensions of the GUI

url_openweatherAPI = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}" #API url
api = "api.key" #Accessing the text-file containing my personal API-key
parser = ConfigParser() #To read configuration files
parser.read(api)

api_k = parser['Kevin_api_key']['openweatherkey'] #My personal API key

#Class so program becomes more OOP with function inside.
class Zeus:
    def find_weather(self,city_entered_by_user):
        self.final = requests.get(url_openweatherAPI.format(city_entered_by_user, api_k))

        if self.final:
            json_file = self.final.json()
            city = json_file['name']
            country_name = json_file['sys']['country']
            temperature_kelvin = json_file['main']['temp']
            temp = temperature_kelvin - 273.15
            weather_description = json_file['weather'][0]['description']
            results = (city, country_name, temp, weather_description)
            return results
        else:
            return None

#Class so program becomes more OOP with function inside.
class Printer:
    def print_results(self):
        emp2 = Zeus()
        self.city = search_for_city.get()
        self.weather = emp2.find_weather(self.city)
        if self.weather:
            city_entered_by_user['text'] = '{},{}'.format(self.weather[0], self.weather[1])
            weather_city['text'] = self.weather[3]
            temperature_city['text'] = '{:.2f} C'.format(self.weather[2])
        else:
            messagebox.showerror('System message',
                             'Cannot find inserted city, try spelling the name correctly')  # This is a popup window that shows up when the city name is spelled wrong.


emp1 = Printer()


search_for_city = StringVar()  # Holds the StringVar which is used in the Entry function
write_down_city = Entry(main, textvariable=search_for_city, fg="grey",
                        font=("Futura 20"))  # This function accepts a single line of string from the user
write_down_city.pack(ipady=10,
                     ipadx=20)  # The pack function adds a widget to the GUI

search_button = Button(main, text='Search for city', width=12, bg="grey", fg="white", font=("Futura", 20), command=emp1.print_results)
search_button.pack()  # Button widget that adds buttons in python app

city_entered_by_user = Label(main, font=("Futura", 20), bg="lightgrey")
city_entered_by_user.pack()  # Creates a widget for the

temperature_city = Label(main, font=("Futura", 20,), bg="lightgrey")
temperature_city.pack()  # Creates a widget for the temperature city

weather_city = Label(main, font=("Futura", 20), bg="lightgrey")
weather_city.pack()  # Creates a widget for the weather condition in that city

main.mainloop()  # This means that the program ends here
