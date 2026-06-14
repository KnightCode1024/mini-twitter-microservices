# Full stack mini twitter microservices app

Microservices practice and many new techologis

## Services

![Services Schema](services-schema.png)

### User

- `Python`
- `FastApi`
- `Postgresql`
- `Redis`
- `RabbitMQ`
- `TaskIQ`
- `Dishka`
- `SQLalchemy`
- `Pydantic`
- `Pydantic-Settings`
- `Pip`

### Tweet

- `Python`
- `FastApi`
- `Mongo`
- `Dishka`
- `Pydantic`
- `Pydantic-Settings`
- `UV`

## Media

- `Go`

### Timeline

- `Go`

### Follow

- `Go`

### ML

- `Python`
- `Fastapi`

### Frontend

- `TypeScript`
- `React`

### Gateway
    pass

## Launch

### Setup user service

1. Create `.env`

`services/user-service/.env`

```env
POSTGRES_USER=user_service_user
POSTGRES_PASSWORD=12345678
POSTGRES_NAME=user_service_db
POSTGRES_HOST=db_user_service
POSTGRES_PORT=5432

REDIS_HOST=redis_user_service
REDIS_PORT=6379

EMAIL_HOST=smtp.yandex.ru
EMAIL_PORT=465
EMAIL_USERNAME=n17k17@yandex.ru
EMAIL_PASSWORD=SuperPsw
EMAIL_USE_SSL=True

RABBITMQ_URL=amqp://guest:guest@rabbitmq_user_service:5672

FRONTEND_URL=http://localhost:5173
```

2. Generate jwt certs

```bash
# Перейти в папку бекенда
cd services/user-service

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

### Setup tweet service

1. Create `.env`

```env
MONGO_USERNAME=tweet_service_user
MONGO_PASSWORD=12345678
MONGO_DATABASE=tweet_service_db
```

### Setup follow service

soon

### Setup media service

soon

### Setup ml service

soon

### Up all services

```bash
docker compose up --build -d
```

## Services

- `Frontend` - http://127.0.0.1:5173
- `Gateway`
- `User service` - http://127.0.0.1:8003/docs
- `Tweet service` - http://127.0.0.1:8003/docs
- `Media service`
- `Follow service`
- `ML service`
