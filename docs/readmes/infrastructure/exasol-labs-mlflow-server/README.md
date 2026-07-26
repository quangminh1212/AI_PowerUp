<!-- source: https://github.com/exasol-labs/exasol-labs-mlflow-server.git sha: 91d68b60ca65d3442daff3b4e53340c2a5ca83a5 readme: main/README.md -->
# exasol-labs/exasol-labs-mlflow-server

A MLflow HTTP API service for AI inference, designed for serving HuggingFace models through a robust, scalable web service for the Exasol RDBMS.

---

# Exasol MLflow Server

[![CI](https://github.com/exasol/exasol-labs-mlflow-server/actions/workflows/ci.yml/badge.svg)](https://github.com/exasol/exasol-labs-mlflow-server/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A MLflow HTTP API service for AI inference, designed for serving HuggingFace models through a robust, scalable web service for the Exasol RDBMS.

## Features

- **Fast HTTP API** - FastAPI-based service with automatic OpenAPI documentation
- **HuggingFace Integration** - Seamless integration with HuggingFace Transformers
- **Model Hot-Swapping** - Dynamic model loading and switching
- **Concurrent Processing** - Built-in request limiting and parallel processing
- **MLflow Integration** - Full MLflow model registry and tracking support
- **JWT Authentication** - Optional token-based authentication with model access control
- **Docker Ready** - Production-ready containerization
- **Comprehensive Testing** - Full test suite with coverage reporting
- **Production Grade** - Security scanning, linting, and CI/CD pipeline

## Quick Start

### Installation

```bash
# Install the package
pip install exasol-mlflow-server

# Or for development
git clone https://github.com/exasol/exasol-labs-mlflow-server.git
cd exasol-labs-mlflow-server
pip install -e .[dev]
```

### Running the Service

```bash
# Start the service with default configuration
mlflow-server

# Or with custom configuration
python -m mlflow_service.server --config configs/models.yaml --api-port 50051
```

The service will start this server:
- **AI API Server**: `http://localhost:50051` (Model inference API)

### Basic Usage

```python
from mlflow_service.client import AIClient
import pandas as pd

# Connect to the service
client = AIClient(host="localhost", port=50051)

# Prepare input data
data = pd.DataFrame({"text": ["I love this product!", "This is terrible."]})

# Get predictions
predictions = client.predict(data)
print(predictions)
# Output: [{"label": "POSITIVE", "score": 0.95}, {"label": "NEGATIVE", "score": 0.89}]
```

### Using cURL

```bash
# Check service status
curl http://localhost:50051/status

# Run inference on specific model
curl -X POST http://localhost:50051/model/small/infer \
  -H "Content-Type: application/json" \
  -d '{"text": ["I love this!", "Not great."]}'

# List available models
curl http://localhost:50051/models
```

## Authentication

The service supports optional JWT-based authentication with fine-grained model access control.

### Enabling Authentication

Set environment variables to enable authentication:

```bash
export MLFLOW_AUTH_ENABLED=true
export MLFLOW_JWT_SECRET_KEY="your-secret-key-change-this-in-production"
export MLFLOW_TOKEN_EXPIRE_MINUTES=1440  # 24 hours (optional)
```

### Token Management

#### POST /auth/token
Generate JWT access tokens with model permissions.

**Request:**
```json
{
  "subject": "user123",
  "models": ["small", "medium"],
  "admin": false,
  "expire_minutes": 1440
}
```

**Response:**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer",
  "expires_in": 86400
}
```

**Note**: This endpoint requires admin privileges when authentication is enabled.

#### GET /auth/me
Get current token information and permissions.

**Response:**
```json
{
  "subject": "user123",
  "models": ["small", "medium"],
  "admin": false,
  "expires_at": 1640995200,
  "issued_at": 1640908800
}
```

### Using Authenticated Endpoints

Include the JWT token in the Authorization header:

```bash
curl -H "Authorization: Bearer YOUR_JWT_TOKEN" \
     -H "Content-Type: application/json" \
     -d '{"text": ["Hello world"]}' \
     http://localhost:50051/model/small/infer
```

### Token Permissions

- **Model Access**: Tokens specify which models the user can access
- **Admin Privileges**: Admin tokens can access all models and manage authentication
- **Wildcard Access**: Use `["*"]` in models array for access to all models

### Security Considerations

- Change the default JWT secret key in production
- Use HTTPS in production environments
- Tokens expire automatically (default: 24 hours)
- Admin tokens should be carefully managed and rotated regularly

## Configuration

### Model Configuration

Models are configured in `configs/models.yaml`:

```yaml
# Example model configuration
small:
  hf_model_name: "cardiffnlp/twitter-roberta-base-sentiment-latest"
  mlflow_class: "HFSentimentModel"
  batch_size: 8

medium:
  hf_model_name: "nlptown/bert-base-multilingual-uncased-sentiment"
  mlflow_class: "HFSentimentModel"
  batch_size: 4
```

### Command Line Options

```bash
python -m mlflow_service.server --help

Options:
  --config PATH              Model configuration file (default: configs/models.yaml)
  --api-port INT            AI API port (default: 50051)
  --max-parallel-requests   Maximum concurrent requests (default: 2)
  --memory-limit-mb INT     Memory limit in MB (default: 0, unlimited)
  --gpu-memory-fraction     GPU memory fraction (default: 0.0, auto-growth)
```

## API Reference

The service provides a comprehensive REST API with full OpenAPI documentation available at `http://localhost:50051/docs` when running.

### Core Endpoints

#### POST /model/{model_tag}/infer
Run AI model inference on a specific model.

**Parameters:**
- `model_tag` - Model identifier (e.g., "small", "medium")

**Request:**
```json
{
  "text": ["I love this product!", "This is terrible."]
}
```

**Response:**
```json
{
  "predictions": [
    {"label": "POSITIVE", "score": 0.95},
    {"label": "NEGATIVE", "score": 0.89}
  ],
  "model_used": "small"
}
```

**Features:**
- Automatic model loading if not currently active
- Thread-safe model switching
- Structured response format with confidence scores

#### POST /model/{model_tag}/load
Explicitly load or reload a specific model.

**Parameters:**
- `model_tag` - Model identifier to load

**Request:** Empty body

**Response:**
```json
{
  "status": "model loaded",
  "model_uri": "models:/small/1",
  "tag": "small"
}
```

#### GET /models
List available models with enriched configuration and registry details.

**Response (example):**
```json
{
  "default": "small",
  "models": {"small": "models:/small/1", "medium": "models:/medium/1"},
  "current": "small",
  "details": {
    "small": {
      "tag": "small",
      "model_uri": "models:/small/1",
      "is_default": true,
      "is_loaded": true,
      "exists_in_registry": true,
      "mlflow_class": "HFSentimentModel",
      "hf_model_name": "cardiffnlp/twitter-roberta-base-sentiment-latest",
      "batch_size": 8,
      "registry_versions": [
        {
          "version": "1",
          "stage": "Staging",
          "status": "READY",
          "run_id": "abc123",
          "source": "runs:/abc123/small",
          "last_updated_timestamp": 1700000000,
          "size_bytes": 123456789
        }
      ]
    }
  }
}
```

#### GET /status
Get service status and performance metrics.

**Response:**
```json
{
  "max_parallel_requests": 2,
  "active_requests": 1,
  "waiting_requests": 0,
  "total_requests": 42,
  "current_model": "small",
  "queue_available": 1
}
```

### Model Management Endpoints (Admin Only)

#### POST /model/{model_tag}
Add a new model to the service at runtime.

**Parameters:**
- `model_tag` - Unique identifier for the new model

**Request:**
```json
{
  "model_uri": "models:/custom-model/1",
  "hf_model_name": "distilbert-base-uncased-finetuned-sst-2-english",
  "mlflow_class": "HFSentimentModel",
  "batch_size": 1
}
```

**Response:**
```json
{
  "status": "success",
  "message": "Model 'custom-model' added successfully",
  "tag": "custom-model",
  "model_uri": "models:/custom-model/1"
}
```

#### DELETE /model/{model_tag}
Remove a model from the service.

**Parameters:**
- `model_tag` - Model identifier to remove

**Response:**
```json
{
  "status": "success",
  "message": "Model 'custom-model' removed successfully",
  "tag": "custom-model",
  "model_uri": "models:/custom-model/1"
}
```

**Note:** Cannot remove the default model or currently loaded model.

### Class Management Endpoints (Admin Only)

#### POST /class/{class_name}
Register an external model class at runtime.

**Parameters:**
- `class_name` - Name to register the class under

**Request:**
```json
{
  "module_name": "examples.custom_models",
  "class_name": "CustomSentimentModel"
}
```

**Response:**
```json
{
  "status": "success",
  "message": "Successfully registered model class: CustomSentiment",
  "class_name": "CustomSentiment"
}
```

#### DELETE /class/{class_name}
Remove a model class from the service.

**Parameters:**
- `class_name` - Name of the class to remove

**Response:**
```json
{
  "status": "success",
  "message": "Successfully removed model class: CustomSentiment",
  "class_name": "CustomSentiment"
}
```

**Note:** Built-in model classes cannot be removed.

#### GET /classes
List all registered model classes.

**Response:**
```json
{
  "model_classes": ["HFSentimentModel", "CustomSentiment"],
  "details": {
    "HFSentimentModel": "HFSentimentModel",
    "CustomSentiment": "CustomSentimentModel"
  }
}
```

### Interactive API Documentation

- **Swagger UI**: `http://localhost:50051/docs`
- **ReDoc**: `http://localhost:50051/redoc`
- **OpenAPI Spec**: `http://localhost:50051/openapi.json`

## Development

### Setting up Development Environment

```bash
# Clone the repository
git clone https://github.com/exasol/exasol-labs-mlflow-server.git
cd exasol-labs-mlflow-server

# Install development dependencies
pip install -e .[dev]

# Install pre-commit hooks
pre-commit install
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=mlflow_service --cov-report=html
```

### Code Quality

The project uses several tools for code quality:

```bash
# Format code
make format

# Lint code
make lint

# Run all pre-commit checks
pre-commit run --all-files
```

### Project Structure

```
mlflow_service/             # Main service implementation
    __init__.py
    server.py               # FastAPI server and MLflow integration
    client.py               # HTTP client for the API
    models.py               # MLflow model wrappers
    sql/                    # UDF SQL files
configs/                    # Configuration files
    models.yaml             # Model definitions
tests/                      # Test suite
.github/workflows/          # CI/CD pipelines
Dockerfile                  # Container definition
pyproject.toml              # Project configuration
```

## Docker Deployment

### Building the Image

```bash
docker build -t mlflow-server .
```

### Running with Docker

```bash
# Run with default configuration
docker run -p 50051:50051 mlflow-server

# Run with custom configuration
docker run -p 50051:50051 \
  -v $(pwd)/configs:/app/configs \
  mlflow-server --config configs/models.yaml
```

### Docker Compose

```yaml
version: '3.8'
services:
  mlflow-server:
    image: mlflow-server
    ports:
      - "5000:5000"   # MLflow UI
      - "50051:50051" # API Server
    volumes:
      - ./configs:/app/configs
      - ./mlruns:/app/mlruns
    environment:
      - MLFLOW_BACKEND_STORE_URI=sqlite:///mlflow.db
```

## Extending the Service

### Adding External Model Classes

The MLflow server supports loading custom model classes externally in two ways:

#### 1. Command Line Arguments

Load external model classes when starting the server:

```bash
# Load a single external model class
python -m mlflow_service.server \
  --external-models "examples.custom_models:CustomSentimentModel"

# Load multiple classes with custom names
python -m mlflow_service.server \
  --external-models \
    "examples.custom_models:CustomSentimentModel:CustomSentiment" \
    "my_package.models:AdvancedClassifier:Advanced"
```

## Client CLI

The package ships a command-line client `mlflow-client` to help with operations, Exasol integration, and token management.

### Install and Build

- Install: `make install` (or `pip install -e .`)
- Build wheel: `make build` → creates `dist/*.whl`

### Environment Configuration (.env)

- The client and server both support loading a `.env` file via `--env .env`.
- Example variables (see `.env.example`):
  - Server/auth: `MLFLOW_AUTH_ENABLED`, `MLFLOW_JWT_SECRET_KEY`, `MLFLOW_JWT_ALGORITHM`, `MLFLOW_TOKEN_EXPIRE_MINUTES`, `MLFLOW_HTTP_PORT`, `MLFLOW_CONFIG_PATH`
  - Client/API: `MLFLOW_API_HOST`, `MLFLOW_API_PORT`
  - Exasol: `EXA_DSN`, `EXA_USER`, `EXA_PASSWORD`, `EXA_SCHEMA`, `EXA_CONNECTION_NAME`
  - Token: `MLFLOW_ADMIN_TOKEN` (only where needed; avoid committing!)
  - BucketFS (preferred single URL):
    - `EXA_BUCKETFS_URL=http://USER:BASE64_PASSWORD@HOST:PORT/buckets/BUCKET/PATH`
    - Example: `http://w:dw==@127.0.0.1:6583/buckets/default/mlflow` (`dw==` is base64("w"))
    - Or use components: `EXA_BUCKETFS_HOST`, `EXA_BUCKETFS_PORT`, `EXA_BUCKETFS_BUCKET`, `EXA_BUCKETFS_PATH`, `EXA_BUCKETFS_USER`, `EXA_BUCKETFS_PASSWORD`

### Generate Tokens

Create tokens by calling the server (preferred) or by signing offline.

- Server-side (requires admin token when auth is enabled):
  - `mlflow-client create-token --subject admin --models '*' --admin --expire-minutes 43200 --env .env`
  - If auth is enabled, provide an admin token: `--token "$MLFLOW_ADMIN_TOKEN"` or set `MLFLOW_ADMIN_TOKEN` in `.env`.

- Offline signing (no server call; needs server secret locally):
  - `mlflow-client create-token --offline --subject user1 --models small,large --expire-minutes 1440 --env .env`
  - Reads `MLFLOW_JWT_SECRET_KEY` and `MLFLOW_JWT_ALGORITHM` from `.env` unless `--secret`/`--algorithm` are given.
  - Output is a JWT printed to stdout.

Bootstrap tip: If you don’t have an admin token yet, you can temporarily start the server with `MLFLOW_AUTH_ENABLED=false` to mint the first admin token via `/auth/token`, then restart with auth enabled.

### Store Admin Token in Exasol

Store a token securely in Exasol using `CREATE CONNECTION`:

```bash
mlflow-client store-admin-token --env .env
# Or pass explicit flags: --dsn --user --password --connection --token
```

UDFs will read the token from the connection specified by `EXA_CONNECTION_NAME` (default `MLFLOW_ADMIN_TOKEN`).

### Create UDFs in Exasol

Create Python UDFs to call the MLflow service:

```bash
mlflow-client create-udfs --env .env
# Or pass: --dsn --user --password --schema --connection
```

This creates scripts in the target schema:
- `MLFLOW_INFER_JSON(model_tag VARCHAR, text VARCHAR) RETURNS JSON`
- `MLFLOW_LOAD_MODEL(model_tag VARCHAR) RETURNS JSON`
- `MLFLOW_LIST_MODELS() RETURNS JSON`
- `MLFLOW_STATUS() RETURNS JSON`

These UDFs call `http://MLFLOW_API_HOST:MLFLOW_API_PORT` and add `Authorization: Bearer <token>` if the token connection exists.

### Upload Wheel to BucketFS

Upload the client/server wheel to BucketFS for Exasol environments:

```bash
# Upload newest dist/*.whl using EXA_BUCKETFS_URL from .env
mlflow-client bucketfs-upload --env .env

# Or specify a file and components explicitly
mlflow-client bucketfs-upload --file dist/exasol_mlflow_server-0.1.0-py3-none-any.whl \
  --host 127.0.0.1 --port 6583 --bucket default --path mlflow --user w --password w
```

### Programmatic Client Notes

The programmatic client requires a model tag in calls, matching the API:

```python
from mlflow_service.client import AIClient
import pandas as pd

client = AIClient()  # reads MLFLOW_API_HOST/PORT if set
client.token = "<JWT>"  # optional

client.load("small")
resp = client.predict("small", pd.DataFrame({"text": ["great", "bad"]}))
print(resp)
```

Set `MLFLOW_API_HOST` and `MLFLOW_API_PORT` in `.env` or pass `host`/`port` to `AIClient`.


#### 2. Runtime API Registration

Register model classes at runtime using the REST API:

```bash
# Register a new model class
curl -X POST http://localhost:50051/register-model-class \
  -H "Content-Type: application/json" \
  -d '{
    "module_name": "examples.custom_models",
    "class_name": "CustomSentimentModel",
    "register_name": "CustomSentiment"
  }'

# List all registered model classes
curl http://localhost:50051/model-classes
```

#### 3. Programmatic Registration

```python
from mlflow_service.models import register_model_class, load_external_model_class

# Method 1: Register an already imported class
from examples.custom_models import CustomSentimentModel
register_model_class("CustomSentiment", CustomSentimentModel)

# Method 2: Load and register from module
load_external_model_class(
    "examples.custom_models",
    "CustomSentimentModel",
    "CustomSentiment"
)
```

### Creating Custom Model Classes

1. Create a custom model class that inherits from `HFModel`:

```python
from mlflow_service.models import HFModel
import pandas as pd

class MyCustomModel(HFModel):
    def _load_pipeline(self):
        """Load your HuggingFace pipeline."""
        self.pipeline = self._pipeline_fn(
            "text-classification",  # or your task
            model=self.hf_model_name,
            device=self.device,
            batch_size=self.batch_size,
        )

    def predict(self, context, model_input, params=None):
        """Implement your prediction logic."""
        texts = model_input["text"].astype(str).tolist()
        outputs = self.pipeline(texts, batch_size=self.batch_size)

        # Process outputs as needed
        results = []
        for output in outputs:
            results.append({
                "label": output["label"],
                "score": output["score"],
                # Add custom fields
                "custom_field": "custom_value"
            })

        return pd.DataFrame(results)

    def input_example(self):
        """Return example input for signature inference."""
        return pd.DataFrame({"text": ["example text"]})
```

2. Save your model in a Python module (e.g., `my_models.py`)

3. Load it using one of the methods above

4. Configure it in your `models.yaml`:

```yaml
my_custom_model:
  hf_model_name: "your-model-name"
  mlflow_class: "MyCustomModel"  # Use the registered name
  batch_size: 4
```

### Example Custom Models

See `examples/custom_models.py` for complete examples including:

- **CustomSentimentModel**: Enhanced sentiment analysis with preprocessing/postprocessing
- **TextClassificationModel**: Generic text classification for various tasks

### Model Class Requirements

All custom model classes must:

1. Inherit from `mlflow_service.models.HFModel`
2. Implement the abstract methods:
   - `_load_pipeline()`: Initialize your HuggingFace pipeline
   - `predict()`: Process input and return predictions
   - `input_example()`: Return example input DataFrame
3. Follow the expected input/output format (DataFrame with "text" column)

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests and ensure they pass (`pytest`)
5. Run code quality checks (`pre-commit run --all-files`)
6. Commit your changes (`git commit -m 'Add amazing feature'`)
7. Push to the branch (`git push origin feature/amazing-feature`)
8. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with [MLflow](https://mlflow.org/) for model management
- Powered by [FastAPI](https://fastapi.tiangolo.com/) for HTTP service
- Integrated with [HuggingFace Transformers](https://huggingface.co/transformers/) for model inference
- Developed by [Exasol Labs](https://github.com/exasol)
