# 🔄 MLOps & Pipeline Orchestration

End-to-end ML lifecycle tools — from experiment tracking and data versioning to workflow orchestration and model serving.

## Overview

This directory contains **15 submodules** covering production MLOps infrastructure — workflow orchestration (Kubeflow, Metaflow, Prefect), experiment tracking (ClearML, W&B via evaluation/), data versioning (DVC), feature stores (Feast), model monitoring (Evidently), and model serving (Seldon, Triton).

## Submodules (15)

### Workflow Orchestration
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`kubeflow`](https://github.com/kubeflow/kubeflow) | Kubeflow | ML toolkit for Kubernetes |
| [`metaflow`](https://github.com/Netflix/metaflow) | Netflix | Human-centric ML workflow framework |
| [`prefect`](https://github.com/PrefectHQ/prefect) | Prefect | Modern workflow orchestration |
| [`dagster`](https://github.com/dagster-io/dagster) | Dagster | Data orchestration with software-defined assets |
| [`flyte`](https://github.com/flyteorg/flyte) | Flyte | Scalable ML and data workflow engine |
| [`argo-workflows`](https://github.com/argoproj/argo-workflows) | Argo | Kubernetes-native workflow engine |
| [`zenml`](https://github.com/zenml-io/zenml) | ZenML | MLOps framework for reproducible pipelines |

### Experiment Tracking & Registry
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`clearml`](https://github.com/allegroai/clearml) | ClearML | End-to-end ML experiment management |
| [`mlops-zoomcamp`](https://github.com/DataTalksClub/mlops-zoomcamp) | DataTalks | Free MLOps engineering course |

### Data & Feature Management
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`dvc`](https://github.com/iterative/dvc) | Iterative | Data version control for ML projects |
| [`feast`](https://github.com/feast-dev/feast) | Feast | Open-source feature store |
| [`great-expectations`](https://github.com/great-expectations/great_expectations) | GX | Data quality validation and testing |

### Model Monitoring
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`evidently`](https://github.com/evidentlyai/evidently) | Evidently | ML model monitoring and data drift detection |

### Model Serving
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`seldon-core`](https://github.com/SeldonIO/seldon-core) | Seldon | ML model deployment on Kubernetes |
| [`triton-server`](https://github.com/triton-inference-server/server) | NVIDIA | High-performance multi-framework inference server |

## Key Capabilities

| Capability | Best Options |
|-----------|--------|
| **Pipeline Orchestration** | kubeflow, prefect, dagster, flyte |
| **Data Versioning** | dvc |
| **Feature Store** | feast |
| **Model Serving** | triton-server, seldon-core |
| **Monitoring** | evidently, great-expectations |
| **Experiment Tracking** | clearml |

## Usage

```bash
# Init MLflow (in infrastructure/) + DVC
git submodule update --init --depth 1 mlops/dvc

# Start Prefect workflow
git submodule update --init --depth 1 mlops/prefect
pip install prefect && prefect server start
```
