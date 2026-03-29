# 🔧 MLOps & Workflow Orchestration

Production ML lifecycle management, pipeline orchestration, and infrastructure.

## Overview

This directory contains 15 submodules covering the complete MLOps stack — from experiment tracking and data versioning to workflow orchestration, feature stores, model serving, and data quality monitoring.

## Submodules (15)

### Workflow Orchestration
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`kubeflow`](https://github.com/kubeflow/kubeflow) | Kubeflow | ML toolkit for Kubernetes (~14k★) |
| [`dagster`](https://github.com/dagster-io/dagster) | Dagster | Cloud-native data orchestrator (~12k★) |
| [`prefect`](https://github.com/PrefectHQ/prefect) | Prefect | Modern workflow management (~17k★) |
| [`flyte`](https://github.com/flyteorg/flyte) | Flyte | Kubernetes-native ML workflows |
| [`argo-workflows`](https://github.com/argoproj/argo-workflows) | Argo | Container-native workflow engine (~15k★) |

### Experiment Tracking & Data Versioning
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`clearml`](https://github.com/allegroai/clearml) | ClearML | Auto-magical ML lifecycle platform |
| [`dvc`](https://github.com/iterative/dvc) | DVC | Data version control for ML (~14k★) |
| [`evidently`](https://github.com/evidentlyai/evidently) | Evidently | ML model monitoring and testing |

### Feature Store & Data Quality
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`feast`](https://github.com/feast-dev/feast) | Feast | Open-source feature store (~6k★) |
| [`great-expectations`](https://github.com/great-expectations/great_expectations) | GX | Data quality validation (~10k★) |

### Model Serving
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`triton-server`](https://github.com/triton-inference-server/server) | NVIDIA | High-performance inference server |
| [`seldon-core`](https://github.com/SeldonIO/seldon-core) | Seldon | ML deployment on Kubernetes |

### ML Lifecycle Frameworks
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`zenml`](https://github.com/zenml-io/zenml) | ZenML | Extensible MLOps framework |
| [`metaflow`](https://github.com/Netflix/metaflow) | Netflix | Data science lifecycle framework |

### Learning
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`mlops-zoomcamp`](https://github.com/DataTalksClub/mlops-zoomcamp) | DataTalksClub | MLOps engineering bootcamp |

## Usage

```bash
git submodule update --init --depth 1 mlops/kubeflow
git submodule update --init --depth 1 mlops/dagster
```
