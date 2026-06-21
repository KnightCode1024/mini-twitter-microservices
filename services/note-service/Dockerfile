# Builder
FROM golang:1.26-alpine AS builder

WORKDIR /app

COPY go.mod go.sum ./
RUN go mod download

COPY . .

RUN go build -o app ./cmd/app

# Runtime
FROM alpine:3.24

WORKDIR /app

COPY --from=builder /app/app .