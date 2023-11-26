# CoffeeDev
Сервис автоматизации системы учета киберспортивных мероприятий

## Стек технологий
Backend:
* Python, FastAPI, PostgreSQL, Docker

Frontend:
* Vue.js, Vite, Bootstrap

## Установка и запуск
1. Убедитесь, что у вас установлен [Docker](https://www.docker.com/).
2. Склонируйте данный репозиторий
    ```shell
    git clone https://github.com/arsuhinars/fsp-cup-2023-backend
    ```
3. Перейдите в директорию проекта и запустите Docker Compose:
    ```shell
    docker compose up --build -d
    ```
4. После успешного запуска сервис будет доступен локально по адресу http://localhost:5173/
5. Для остановки работы сервиса воспользуйтесь следующей командой:
    ```shell
    docker compose down
    ```
