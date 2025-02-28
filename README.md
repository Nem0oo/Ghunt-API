# Ghunt api
## Usage
1. Build containers : `docker compose build`
2. Run all containers : `docker compose up -d`
3. Connect to ghunt container to login (see ghunt doc) :
   ```bash
   docker exec -it ghunt bash
   ghunt login
   ```
4. Copy api_data/exemple_key.txt to api_data/key.txt
5. Change the content of api_data/key.txt to a long and secret key
6. Finally connect using the key you just choose: `http://localhost:8000/ghunt?command=email&params=example@gmail.com&key=LongSecretKey`
7. Output is in json format : 
   1. output.text : contains the text output normaly displayed in terminal
   2. output.json : contains the json exported with the --json argument
   3. error : contains the stderr from the subprocess command

## Note
- creds.m saved in `./ghunt_data` and mounted in container
- json files of searched accounts are saved in `./accounts_info` and mounted in both containers