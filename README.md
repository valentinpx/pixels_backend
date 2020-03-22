# pixels
Epitech Jam about street art

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
        "id" : "10"
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
    "id" : "10"
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
```json
```json
{
    "color" : "000000",
    "id" : "10"
}
```
- `404 Not Found` if pixel does not exist

