docker exec -it flask_flask_1 bash

docker exec -it flask_flask_1 bash python train_model.py

curl.exe --header "Content-Type: application/json" --request POST --data "{"flower":"1, 2, 5, 6"}" http://localhost/:5000/iris_post