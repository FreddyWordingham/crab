# crab

Crud Restful Api dataBase

## Quickstart

Simply download the repo, and then run `docker-compose`:

```shell
git clone github.com/digiLab-ai/crab.git
cd crab
docker-compose up --build --force-recreate --no-deps -d
```

## Configuration

The `/crab/.env` file sets the environment variables:

```env
MONGO_INITDB_ROOT_USERNAME=admin
MONGO_INITDB_ROOT_PASSWORD=pinecone
MONGO_INITDB_DATABASE=data
```
