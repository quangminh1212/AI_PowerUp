# 📊 Data & RAG Pipelines

Web crawling, document parsing, vector databases, RAG engines, OCR, and annotation tools.

## Overview

This directory contains **40 submodules** covering the complete data processing pipeline for AI applications — from web scraping and document parsing through vector database storage and retrieval-augmented generation (RAG). Build production-grade knowledge systems that connect LLMs to your data.

## Submodules (40)

### Web Crawling & Scraping
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`firecrawl`](https://mendableai/firecrawl) | Mendable | Turn websites into LLM-ready markdown |
| [`crawl4ai`](https://unclecode/crawl4ai) | unclecode | Fast async web crawler optimized for AI/LLM data extraction |
| [`scrapegraph-ai`](https://VinciGit00/Scrapegraph-ai) | VinciGit00 | AI-powered web scraping with knowledge graphs |

### RAG Engines & Knowledge Systems
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`ragflow`](https://infiniflow/ragflow) | InfiniFlow | Deep document understanding RAG engine |
| [`graphrag`](https://microsoft/graphrag) | Microsoft | Knowledge-graph-based RAG for complex queries |
| [`storm`](https://stanford-oval/storm) | Stanford OVAL | LLM-powered research and wiki-article generation |
| [`khoj`](https://khoj-ai/khoj) | Khoj AI | Personal AI assistant with long-term memory |
| [`kotaemon`](https://Cinnamon/kotaemon) | Cinnamon | Open-source RAG-based chat with documents |
| [`quivr`](https://QuivrHQ/quivr) | Quivr | Second brain powered by generative AI |
| [`txtai`](https://neuml/txtai) | neuml | All-in-one embeddings + RAG + workflows |
| [`r2r`](https://SciPhi-AI/R2R) | SciPhi AI | Production-ready RAG engine with auth, observability |
| [`autorag`](https://Marker-Inc-Korea/AutoRAG) | Marker Inc | AutoML-style optimization for RAG pipelines |

### Document Parsing & Extraction
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`docling`](https://DS4SD/docling) | IBM | Universal document converter (PDF, DOCX, PPTX → structured) |
| [`docling-ibm`](https://DS4SD/docling-ibm-models) | IBM | Pre-trained models for Docling |
| [`marker`](https://VikParuchuri/marker) | Vik Paruchuri | Convert PDF/EPUB/MOBI to markdown with high accuracy |
| [`markitdown`](https://microsoft/markitdown) | Microsoft | Convert any document type to Markdown |
| [`unstructured`](https://Unstructured-IO/unstructured) | Unstructured | ETL pipeline for unstructured documents |
| [`llama-parse`](https://run-llama/llama_parse) | LlamaIndex | Cloud-based document parser for complex PDFs |
| [`MegaParse`](https://QuivrHQ/MegaParse) | Quivr | Parse any document type with high fidelity |
| [`langextract`](https://google/langextract) | Google | Structured information extraction from documents |

### OCR & Text Recognition
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`surya`](https://VikParuchuri/surya) | Vik Paruchuri | Multilingual OCR, layout analysis, reading order detection |
| [`tesseract`](https://tesseract-ocr/tesseract) | Tesseract | Industry-standard open-source OCR engine |
| [`EasyOCR`](https://JaidedAI/EasyOCR) | JaidedAI | Ready-to-use OCR for 80+ languages |
| [`doctr`](https://mindee/doctr) | Mindee | Deep learning OCR with layout analysis |

### Vector Databases
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`chroma`](https://chroma-core/chroma) | Chroma | Embedded AI-native vector database |
| [`faiss`](https://facebookresearch/faiss) | Meta | Efficient billion-scale similarity search |
| [`weaviate`](https://weaviate/weaviate) | Weaviate | Cloud-native vector search engine |
| [`lancedb`](https://lancedb/lancedb) | LanceDB | Serverless vector database built on Lance format |
| [`milvus`](https://milvus-io/milvus) | Milvus | Cloud-native vector database for enterprise |
| [`pgvector`](https://pgvector/pgvector) | pgvector | Vector similarity search for PostgreSQL |
| [`qdrant`](https://qdrant/qdrant) | Qdrant | High-performance vector search engine in Rust |

### Embeddings & Retrieval
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`embeddings`](https://huggingface/text-embeddings-inference) | Hugging Face | High-performance text embeddings inference |
| [`sentence-transformers`](https://UKPLab/sentence-transformers) | UKP Lab | State-of-the-art sentence and text embeddings |
| [`nemo-retriever`](https://NVIDIA/NeMo-Retriever) | NVIDIA | Enterprise retrieval models and microservices |
| [`kg-gen`](https://whyhow-ai/kg-gen) | WhyHow AI | Knowledge graph generation from text |

### Datasets & Curation
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`hf-datasets`](https://huggingface/datasets) | Hugging Face | The standard library for ML datasets |
| [`nemo-curator`](https://NVIDIA/NeMo-Curator) | NVIDIA | GPU-accelerated dataset curation and deduplication |
| [`fiftyone`](https://voxel51/fiftyone) | Voxel51 | Visual dataset exploration, annotation, and curation |

### Annotation & Labeling
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`label-studio`](https://HumanSignal/label-studio) | HumanSignal | Multi-type data labeling — text, image, audio, video |
| [`cvat`](https://cvat-ai/cvat) | CVAT AI | Computer vision annotation tool |

## Key Capabilities

| Capability | Best Options |
|-----------|--------|
| **Web Scraping** | firecrawl, crawl4ai, scrapegraph-ai |
| **RAG (Simple)** | ragflow, txtai, r2r |
| **RAG (Graph-based)** | graphrag, kg-gen, storm |
| **PDF Parsing** | docling, marker, surya |
| **Vector DB (Embedded)** | chroma, lancedb |
| **Vector DB (Distributed)** | milvus, qdrant, weaviate |
| **Embeddings** | sentence-transformers, embeddings |
| **Labeling** | label-studio, cvat, fiftyone |

## Usage

```bash
# Init a vector database
git submodule update --init --depth 1 data-rag/chroma
pip install chromadb

# Parse PDFs to markdown
git submodule update --init --depth 1 data-rag/marker
cd data-rag/marker && pip install marker-pdf

# Web crawling for AI
git submodule update --init --depth 1 data-rag/firecrawl
cd data-rag/firecrawl && pip install firecrawl-py
```
