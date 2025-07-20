# Frigate OpenAPI (Swagger) Docs 

This is a simple docker implementation of the Swagger documentation of the Frigate API implemented such that you can point to your own installation of Frigate as a learning tool on how to access your data. 

It uses a modified frigate.yml from the following [GitHub page](https://github.com/intruder-detection/frigate-http-api-typescript).


# To run

1. Update the SERVER_URL in docker-compose.yml to point to your Frigate URL.

2. Build the docker image

    ```
    docker build -t frigateswagger:latest .
    ```

3. Then run

    ```
    docker compose up
    ```
