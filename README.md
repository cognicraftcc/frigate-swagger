# Setup
    ```
    uv init .
    uv add flask flask-swagger-ui pyyaml
    ```

# Run

1. Create .env using env-sample as example.

2. Run from terminal

    ```
    uv run python app.py
    ```

3. Run in Docker
Set the env settings in docker-compose.yml then run the following:

    ```
    docker build -t frigateswagger:latest .
    docker compose up
    ```
