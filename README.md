# Ghunt api
## Usage
1. Build containers : `docker compose build`
2. Run all containers : `docker compose up -d`
3. Connect to ghunt container to login (see ghunt doc) :
   ```bash
   docker exec -it ghunt bash
   ghunt login
   ```
4. Finally : `http://localhost:8000/ghunt?command=email&params=example@gmail.com`

## Note
- creds.m saved in `./ghunt_data` and mounted in container