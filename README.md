# Pixels
Réalisé lors d'une Jam sur le thème du street art.

Les utilisateurs peuvent ajouter des pixels grace à des coordonées et une couleur.
![preview/pixel.png preview](https://raw.githubusercontent.com/valentinpx/pixels_backend/master/preview/pixel.png)

Les pixels créés apparaissent sur le mur.
![preview/wall.png preview](https://raw.githubusercontent.com/valentinpx/pixels_backend/master/preview/wall.png)

Ce repo contient le backend, du projet. Le frontend est disponible sur le profil de [Lucas Decrock](https://github.com/lucasdcrk/pixels-frontend)

## API
###  List all pixels color by id
***Definition***
- `GET /api/pixels`

***Response***
- `200 OK` on success
```json
[
    {
        "color" : "FFFFFF",
        "id" : "1"
    },
    {
        "color" : "000000",
        "id" : "103680"
    }
]
```

### Get a specified pixel
***Definition***
- `GET /api/pixels/<id>`

***Response***
- `200 OK` on success
```json
{
    "color" : "000000",
    "id" : 10
}
```
- `404 Not Found` if "Q" does not exist

### Modify a pixel color
***Definition***
- `POST /api/pixels/<id>/edit`

***Arguments***
- `"color":string` hexadecimal color without any '#'

***Response***
- `200 OK` on success
- `404 Not Found` if pixel does not exist
- `401 Invalid Color` if color is not hexadecimal with 6 characters

### Surprise
***Definition***
- `GET /api`

***Response***
This is endpoint is usefull to check wether if the api works, the response is a surprise 👀


*Inspired by r/places.*