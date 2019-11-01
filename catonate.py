import requests

api = 'https://cats.boorse.app/api/v1/cats'


cat_data = {
    "id":           10,
    "name":         "Gabriel Boorse",
    "sex":          "Male",
    "breed":        "in control",
    "color":        "Catinator is",
    "age":          5,
    "image_url":    "https://scontent.fewr1-3.fna.fbcdn.net/v/t1.0-9/1653990_270863329736549_1512230593_n.jpg?_nc_cat=109&_nc_oc=AQlYYDMppIRr4tKa3e6yRShvGOzB06Blnw-f76iVhEEq8ic3LaxcoyHf31vs_WjytGY&_nc_ht=scontent.fewr1-3.fna&oh=85440c37a31342aea8c87a045294cc89&oe=5E648BC2"
}

for i in range(20):
    response = requests.post(
        api,
        json=cat_data,
    )

print(response)