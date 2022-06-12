# GEOFIX CHALLANGE

### INSTALASI EXTENSI POSTGIS
1. kalo belum ada venv
```
CREATE EXTENSION postgis;
```
### INSTALASI API FLASK
1. kalo belum ada venv
```
python3 -m venv venv
```
2. Nyalakan venv
 ```
 venv/bin/activate
 ```
3. install semua dependency ke venv
```
 install -r requirements
```
4. nyalakan flask
```
flask run 
```


### SETELAH BERHASIL RUN FLASK
ENDPOINT YANG DAPAT DIGUNAKAN
```
localhost:5000/data
```
```
localhost:5000/data/{{id}}
```
PAYLOAD JSON
```
{
    "name": "GEOFIX",
    "geometry": {
        "type": "LineString",
        "coordinates": [
          [102.022, 0.0], [103.0, 1.0], [104.0, 0.0], [105.0, 1.0]
        ]
      }
}
```
