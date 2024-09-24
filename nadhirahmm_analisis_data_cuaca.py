# API call request, Pandas, Numpy, Seaborn, and Matplotlib modules
import requests
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Import math to get a good number of temp (without decimal) and other math operations
import math

# Name the cities which we want to get for data reference
# We can find the cities list of OpenWeatherMap here: https://openweathermap.org/storage/app/media/cities_list.xlsx
city_name = ["Palembang", "Mecca", "Tokyo", "Berlin", "Oslo", "Moscow", "Denver", "Nairobi", "Helsinki", "Rio"] # Money Heist coded lol ^o^

# My API key (nadhirahmm) from OpenWeatherMap
api_key = "4460098fb41bf9fb9628a1ce2b282d1f"

# List to store weather data for each city
weather_data = []

def get_weather(api_key, city):
    # Get the data from the OpenWeatherMap url using F-String
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    
    # Get the data in response
    response = requests.get(url)
    
    # Check for valid response of API call
    if response.status_code == 200:
        data = response.json()
        # print(data)

        # Extract the weather details needed
        city_name = data['name']
        temp = data['main']['temp']
        temp = math.floor((temp - 273.15)) # Convert to Celcius degree
        weather = data['weather'][0]['description']

        # Append the data to the list
        weather_data.append({
            "Kota": city_name,
            "Suhu (°C)": temp,
            "Cuaca": weather
        })

        # Print the weather data
        # print(f"Kota: {city_name}")
        # print(f"Suhu: {temp}°C")
        # print(f"Cuaca: {weather}\n")
    else:
        # To prints an error for the specific city
        print(f"Data cuaca untuk '{city}' tidak ditemukan!")

# Loop through each city in the city_name
for city in city_name:
    get_weather(api_key, city)


# ==================================== Data analysis using Pandas and NumPy ====================================
# Convert the weather_data list to a DataFrame using Pandas
df = pd.DataFrame(weather_data)

# Save the DataFrame to a CSV file
df.to_csv("weather_data.csv", index=False)

# print("Data cuaca tersimpan dengan file 'weather_data.csv'.")

# 1. Menghitung rata-rata suhu dari semua kota menggunakan Numpy
mean_temp = np.mean(df['Suhu (°C)'])
print(f"Rata-rata suhu dari semua kota adalah {mean_temp:.2f}°C")

# 2.1 Menentukan kota dengan suhu tertinggi dan terendah
max_temp = np.max(df['Suhu (°C)'])
min_temp = np.min(df['Suhu (°C)'])

# 2.2 Mendapatkan kota dengan suhu tertinggi dan terendah
city_max_temp = df[df['Suhu (°C)'] == max_temp]['Kota'].values[0]
city_min_temp = df[df['Suhu (°C)'] == min_temp]['Kota'].values[0]
print(f"Kota dengan suhu tertinggi adalah {city_max_temp} dengan suhu {max_temp}°C")
print(f"Kota dengan suhu terendah adalah {city_min_temp} dengan suhu {min_temp}°C")

# 3. Menganalisis pola cuaca yang paling sering muncul
most_common_weather = df['Cuaca'].value_counts().idxmax() # Mengambil pola cuaca yang paling sering muncul menggunakan Pandas
weather_count = df['Cuaca'].value_counts().max() # Mengambil jumlah kemunculan pola cuaca
print(f"Pola cuaca yang paling sering muncul adalah '{most_common_weather}' muncul sebanyak {weather_count} kali")


# ==================================== Data visualization using Matplotlib and Seaborn ====================================
# Distribusi Suhu (Bar Plot)
plt.figure(figsize=(8, 4))
sns.barplot(x='Kota', y='Suhu (°C)', hue='Cuaca', data=df, palette='coolwarm', legend=False) # Membuat bar chart yang menunjukkan suhu di setiap kota, palette memberikan warna yang menggambarkan suhu dari dingin ke hangat
plt.title('Distribusi Suhu pada Berbagai Kota di Dunia', fontsize=14)
plt.xlabel('Kota', fontsize=10)
plt.ylabel('Suhu (°C)', fontsize=10)
plt.show()

# Distribusi Pola Cuaca (Pie Chart and Count Plot)
plt.figure(figsize=(6, 6))
df['Cuaca'].value_counts().plot.pie(autopct='%1.1f%%', colors=sns.color_palette('pastel'))
plt.title('Distribusi Pola Cuaca', fontsize=14)
plt.ylabel('')
plt.show()

plt.figure(figsize=(8, 5))
sns.countplot(x='Cuaca', hue='Kota', data=df, palette='Set2', legend=False) # Menghitung dan menampilkan frekuensi kemunculan pola cuaca yang berbeda
plt.title('Distribusi Pola Cuaca', fontsize=14)
plt.xlabel('Pola Cuaca', fontsize=10)
plt.ylabel('Jumlah kemunculan', fontsize=10)
plt.show()