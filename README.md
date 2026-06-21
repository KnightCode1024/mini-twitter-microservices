# Full stack Knowledge Hub microservices app

Microservices practice and many new techologis

## Services

setup each services or execute setup script (script in progress)

```bash
chmod +x setup.sh
./setup.sh
```

### Setup Gateway

1. Create `.env`

`gateway/.env`

```env
POSTGRES_USER=gateway_user
POSTGRES_PASSWORD=12345678
POSTGRES_NAME=gateway_db
POSTGRES_HOST=db_gateway
POSTGRES_PORT=5432

REDIS_HOST=redis_gateway
REDIS_PORT=6379

EMAIL_HOST=smtp.yandex.ru
EMAIL_PORT=465
EMAIL_USERNAME=n17k17@yandex.ru
EMAIL_PASSWORD=SuperPsw
EMAIL_USE_SSL=True

RABBITMQ_URL=amqp://guest:guest@rabbitmq_gateway:5672

FRONTEND_URL=http://localhost:5173
```

2. Generate jwt certs

```bash
# Перейти в папку бекенда
cd gateway/

# Создание папки для ключей
mkdir certs

# Переходим в папку для ключей
cd certs

# Если есть openssl
# Генерация RSA приватного ключа
openssl genrsa -out jwt-private.pem 2048

# Генерация публичного ключа
openssl rsa -in jwt-private.pem -outform PEM -pubout -out jwt-public.pem
```

### Setup Note service

1. Create `.env`

```env
APP_HOST=0.0.0.0
APP_PORT=8003
APP_MODE=debug

DB_HOST=note_service_postgres
DB_PORT=5432
DB_USER=note_service_user
DB_NAME=note_service_db
DB_PASSWORD=12345678
```

### Up all services

```bash
docker compose up --build -d
```



## Services

- `Frontend` - http://127.0.0.1:5173
- `Gateway` - http://127.0.0.1:8002/docs
- `Note service` - http://127.0.0.1:8003/ping
