from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint
import yaml

# Load the OpenAPI YAML file
with open("frigate.yml", "r") as f:
    swagger_data = yaml.safe_load(f)


app = Flask(__name__)

# Serve the YAML file as JSON at /swagger.json


@app.route("/swagger.json")
def swagger_json():
    return swagger_data


# Swagger UI configuration
SWAGGER_URL = "/swagger"
API_URL = "/swagger.json"

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={"app_name": "Frigate API"}
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

# Optional: serve root redirect to Swagger UI


@app.route("/")
def index():
    return """
    <html>
        <body>
            <h2>Redirecting to Swagger docs...</h2>
            <script>window.location.href = "/swagger";</script>
        </body>
    </html>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
