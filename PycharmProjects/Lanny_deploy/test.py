import requests
import json

url = "http://127.0.0.1:5000/predict"
input_data = {
'Levy' : 2003, 'Prod_year' : 2000, 'Engine volume' : 2233, 'Mileage' : 192
, 'Cylinders' : 91,
       'Gear box type' : 292, 'Doors' : 33, 'Color': 37, 'Airbags' : 37
, 'Leather interior_No' : 0,
       'Leather interior_Yes' : 1, 'Front': 23, 'Rear':33 ,'Left Wheel':37, 'Right Wheel'
: 23,
       'Mileage sqr': 3883, 'Levy sqr':378, 'mil / year': 7373
}

response = requests.post(url,
                         json = input_data)
print(response.json())