# Awesome DataOps [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://sindresorhus/awesome)

A curated list of awesome DataOps tools.

- [Awesome DataOps](#awesome-dataops)
    - [Data Catalog](#data-catalog)
    - [Data Exploration](#data-exploration)
    - [Data Ingestion](#data-ingestion)
    - [Data Processing](#data-processing)
    - [Data Quality](#data-quality)
    - [Data Serialization](#data-serialization)
        - [Data Compression](#data-compression)
        - [Data Table Format](#data-table-format)
    - [Data Visualization](#data-visualization)
    - [Data Warehouse](#data-warehouse)
    - [Data Workflow](#data-workflow)
    - [Database](#database)
        - [Columnar Database](#columnar-database)
        - [Document-Oriented Database](#document-oriented-database)
        - [Graph Database](#graph-database)
        - [Key-Value Database](#key-value-database)
        - [Relational Database](#relational-database)
        - [Time Series Database](#time-series-database)
        - [Vector Database](#vector-database)
    - [File System](#file-system)
    - [Logging and Monitoring](#logging-and-monitoring)
    - [Metadata Service](#metadata-service)
    - [SQL Playground](#sql-playground)
    - [SQL Query Engine](#sql-query-engine)
- [Resources](#resources)
    - [Books](#books)
    - [Other Lists](#other-lists)
    - [Slack](#slack)
- [Contributing](#contributing)

---

## Data Catalog

*Tools related to data cataloging.*

* [Amundsen](https://www.amundsen.io/) - Data discovery and metadata engine for improving the productivity when interacting with data.
* [Apache Atlas](https://atlas.apache.org) - Provides open metadata management and governance capabilities to build a data catalog.
* [CKAN](https://ckan/ckan) - Open-source DMS (data management system) for powering data hubs and data portals.
* [DataHub](https://linkedin/datahub) - LinkedIn's generalized metadata search & discovery tool.
* [Magda](https://magda-io/magda) - A federated, open-source data catalog for all your big data and small data.
* [Marquez](https://MarquezProject/marquez) - Service for the collection, aggregation, and visualization of a data ecosystem's metadata.
* [Metacat](https://Netflix/metacat) - Unified metadata exploration API service for Hive, RDS, Teradata, Redshift, S3 and Cassandra.
* [OpenLineage](https://OpenLineage/openlineage) - Open standard for metadata and lineage collection.
* [OpenMetadata](https://open-metadata.org/) - A Single place to discover, collaborate and get your data right.
* [Unity Catalog](https://www.unitycatalog.io/) - Industry’s only universal catalog for data and AI.

## Data Exploration

*Tools for performing data exploration.*

* [Apache Zeppelin](https://zeppelin.apache.org/) - Enables data-driven, interactive data analytics and collaborative documents.
* [Jupyter Notebook](https://jupyter.org/) - Web-based notebook environment for interactive computing.
* [JupyterLab](https://jupyterlab.readthedocs.io) - The next-generation user interface for Project Jupyter.
* [Jupytext](https://mwouts/jupytext) - Jupyter Notebooks as Markdown Documents, Julia, Python or R scripts.
* [Marimo](https://marimo-team/marimo) - A reactive Python notebook that's reproducible, git-friendly, and deployable as scripts or apps.
* [Polynote](https://polynote.org/) - The polyglot notebook with first-class Scala support.

## Data Ingestion

*Tools for performing data ingestion.*

* [Amazon Kinesis](https://aws.amazon.com/kinesis/) - Easily collect, process, and analyze video and data streams in real time.
* [Apache Gobblin](https://apache/gobblin) - A framework that simplifies common aspects of big data such as data ingestion.
* [Apache Kafka](https://apache/kafka) - Open-source distributed event streaming platform used by thousands of companies.
* [Apache Pulsar](https://apache/pulsar) - Distributed pub-sub messaging platform with a flexible messaging model and intuitive API.
* [Embulk](https://embulk/embulk) - A parallel bulk data loader that helps data transfer between various storages.
* [Fluentd](https://fluent/fluentd) - Collects events from various data sources and writes them to files.
* [Google PubSub](https://cloud.google.com/pubsub) - Ingest events for streaming into BigQuery, data lakes or operational databases.
* [Nakadi](https://zalando/nakadi) - A distributed event bus that implements a RESTful API abstraction on top of Kafka-like queues.
* [Pravega](https://pravega/pravega) - An open source distributed storage service implementing Streams.
* [RabbitMQ](https://www.rabbitmq.com/) - One of the most popular open source message brokers.

## Data Workflow

*Tools related to data workflow/pipeline.*

* [Apache Airflow](https://apache/airflow) - A platform to programmatically author, schedule, and monitor workflows.
* [Apache Oozie](https://apache/oozie) - An extensible, scalable and reliable system to manage complex Hadoop workloads.
* [Azkaban](https://azkaban/azkaban) - Batch workflow job scheduler created at LinkedIn to run Hadoop jobs.
* [Dagster](https://dagster-io/dagster) - An orchestration platform for the development, production, and observation of data assets.
* [Luigi](https://spotify/luigi) - Python module that helps you build complex pipelines of batch jobs.
* [Prefect](https://docs.prefect.io/) - A workflow management system, designed for modern infrastructure.

## Data Processing

*Tools related to data processing (batch and stream).*

* [Apache Beam](https://apache/beam) - A unified model for defining both batch and streaming data-parallel processing pipelines.
* [Apache Flink](https://apache/flink) - An open source stream processing framework with powerful capabilities.
* [Apache Hadoop MapReduce](https://hadoop.apache.org/docs/current/hadoop-mapreduce-client/hadoop-mapreduce-client-core/MapReduceTutorial.html) - A framework for writing applications which process vast amounts of data.
* [Apache Nifi](https://apache/nifi) - An easy to use, powerful, and reliable system to process and distribute data.
* [Apache Samza](https://apache/samza) - A distributed stream processing framework which uses Apache Kafka and Hadoop YARN.
* [Apache Spark](https://apache/spark) - A unified analytics engine for large-scale data processing.
* [Apache Storm](https://apache/storm) - An open source distributed realtime computation system.
* [Apache Tez](https://apache/tez) - A generic data-processing pipeline engine envisioned as a low-level engine.
* [Faust](https://robinhood/faust) - A stream processing library, porting the ideas from Kafka Streams to Python.
* [skrub](http://skrub-data.org) - Python library to ease preprocessing and feature engineering for tabular machine learning.

## Data Quality

*Tools for ensuring data quality.*

* [Cerberus](https://pyeve/cerberus) - Lightweight, extensible data validation library for Python.
* [Cleanlab](https://cleanlab/cleanlab) - Data-centric AI tool to detect (non-predefined) issues in ML data like label errors or outliers.
* [DataProfiler](https://capitalone/DataProfiler) - A Python library designed to make data analysis, monitoring, and sensitive data detection easy.
* [Deequ](https://awslabs/deequ) - A library built on top of Apache Spark for measuring data quality in large datasets.
* [Great Expectations](https://greatexpectations.io) - A Python data validation framework that allows to test your data against datasets.
* [JSON Schema](https://json-schema.org/) - A vocabulary that allows you to annotate and validate JSON documents.
* [SodaSQL](https://sodadata/soda-sql) - Data profiling, testing, and monitoring for SQL accessible data.

## Data Serialization

*Tools related to data serialization.*

* [Apache Avro](https://apache/avro) - A data serialization system which is compact, fast and provides rich data structures.
* [Apache ORC](https://apache/orc) - A self-describing type-aware columnar file format designed for Hadoop workloads.
* [Apache Parquet](https://apache/parquet-mr) - A columnar storage format which provides efficient storage and encoding of data.
* [Kryo](https://EsotericSoftware/kryo) - A fast and efficient binary object graph serialization framework for Java.
* [ProtoBuf](https://protocolbuffers/protobuf) - Language-neutral, platform-neutral, extensible mechanism for serializing structured data.

### Data Compression

* [Pigz](https://madler/pigz) - A parallel implementation of gzip for modern multi-processor, multi-core machines.
* [Snappy](https://google/snappy) - Open source compression library that is fast, stable and robuts.

### Data Table Format

* [Apache Hudi](https://apache/hudi) - Manages the storage of large analytical datasets on DFS.
* [Apache Iceberg](https://apache/iceberg) - Open table format for huge analytic datasets.
* [Delta Lake](https://delta-io/delta) - An open source project that enables building a Lakehouse architecture on top of data lakes.

## Data Visualization

*Tools for performing data visualization (DataViz).*

* [Apache Superset](https://apache/superset) - A modern data exploration and data visualization platform.
* [Count](https://count.co) - SQL/drag-and-drop querying and visualisation tool based on notebooks.
* [Dash](https://plotly/dash) - Analytical Web Apps for Python, R, Julia, and Jupyter.
* [Data Studio](https://datastudio.google.com) - Reporting solution for power users who want to go beyond the data and dashboards of GA.
* [HUE](https://cloudera/hue) - A mature SQL Assistant for querying Databases & Data Warehouses.
* [Lux](https://lux-org/lux) - Fast and easy data exploration by automating the visualization and data analysis process.
* [Metabase](https://www.metabase.com/) - The simplest, fastest way to get business intelligence and analytics to everyone.
* [Redash](https://redash.io/) - Connect to any data source, easily visualize, dashboard and share your data.
* [Tableau](https://www.tableau.com) - Powerful and fastest growing data visualization tool used in the business intelligence industry.

## Data Warehouse

*Tools related to storing data in data warehouses (DW).*

* [Amazon Redshift](https://aws.amazon.com/redshift/) - Accelerate your time to insights with fast, easy, and secure cloud data warehousing.
* [Apache Hive](https://apache/hive) - Facilitates reading, writing, and managing large datasets residing in distributed storage.
* [Apache Kylin](https://apache/kylin) - An open source, distributed analytical data warehouse for big data.
* [Google BigQuery](https://cloud.google.com/bigquery) - Serverless, highly scalable, and cost-effective multicloud data warehouse.

## Database

*Database tools for storing data.*

### Columnar Database

* [Apache Cassandra](https://apache/cassandra) - Open source column based DBMS designed to handle large amounts of data.
* [Apache Druid](https://apache/druid) - Designed to quickly ingest massive quantities of event data, and provide low-latency queries.
* [Apache HBase](https://apache/hbase) - An open-source, distributed, versioned, column-oriented store.
* [Scylla](https://scylladb/scylla) - Designed to be compatible with Cassandra while achieving higher throughputs and lower latencies.

### Document-Oriented Database

* [Apache CouchDB](https://apache/couchdb) - An open-source document-oriented NoSQL database, implemented in Erlang.
* [Elasticsearch](https://elastic/elasticsearch) - A distributed document oriented database with a RESTful search engine.
* [MongoDB](https://mongodb/mongo) - A cross-platform document database that uses JSON-like documents with optional schemas.
* [RethinkDB](https://rethinkdb/rethinkdb) - The first open-source scalable database built for realtime applications.

### Graph Database

* [Age](https://apache/age) - A multi-model database that supports both graph and relational data models.
* [ArangoDB](https://arangodb/arangodb) - A scalable open-source multi-model database natively supporting graph, document and search.
* [JanusGraph](https://JanusGraph/janusgraph) - Manage large graphs with billions of data distributed across a multi-machine cluster.
* [Memgraph](https://memgraph/memgraph) - An open source graph database, built for real-time streaming data, compatible with Neo4j.
* [Neo4j](https://neo4j/neo4j) - A high performance graph store with all the features expected of a mature and robust database.
* [Titan](https://thinkaurelius/titan) - A highly scalable graph database optimized for storing and querying large graphs.

### Key-Value Database

* [Apache Accumulo](https://apache/accumulo) - A sorted, distributed key-value store that provides robust and scalable data storage.
* [Dragonfly](https://dragonflydb/dragonfly) - A modern in-memory datastore, fully compatible with Redis and Memcached APIs.
* [DynamoDB](https://aws.amazon.com/dynamodb/) - Fast, flexible NoSQL database service for single-digit millisecond performance at any scale.
* [etcd](https://etcd-io/etcd) - Distributed reliable key-value store for the most critical data of a distributed system.
* [EVCache](https://Netflix/EVCache) - A distributed in-memory data store for the cloud.
* [Memcached](https://memcached/memcached) - A high performance multithreaded event-based key/value cache store.
* [Redis](https://redis/redis) - An in-memory key-value database that persists on disk.

### Relational Database

* [CockroachDB](https://cockroachdb/cockroach) - A distributed database designed to build, scale, and manage data-intensive apps.
* [Crate](https://crate/crate) - A distributed SQL database that makes it simple to store and analyze massive amounts of data.
* [MariaDB](https://MariaDB/server) - A replacement of MySQL with more features, new storage engines and better performance.
* [MySQL](https://mysql/mysql-server) - One of the most popular open source transactional databases.
* [PostgreSQL](https://postgres/postgres) - An advanced RDBMS that supports an extended subset of the SQL standard.
* [RQLite](https://rqlite/rqlite) - A lightweight, distributed relational database, which uses SQLite as its storage engine.
* [SQLite](https://sqlite/sqlite) - A popular choice as embedded database software for local/client storage.

### Time Series Database

* [Akumuli](https://akumuli/Akumuli) - Can be used to capture, store and process time-series data in real-time.
* [Atlas](https://Netflix/Atlas) - An in-memory dimensional time series database.
* [InfluxDB](https://influxdata/influxdb) - Scalable datastore for metrics, events, and real-time analytics.
* [QuestDB](https://questdb/questdb) - An open source SQL database designed to process time series data, faster.
* [TimescaleDB](https://timescale/timescaledb) - Open-source time-series SQL database optimized for fast ingest and complex queries.

### Vector Database

* [Milvus](https://milvus-io/milvus/) - An open source embedding vector similarity search engine powered by Faiss, NMSLIB and Annoy.
* [Pinecone](https://www.pinecone.io) - Managed and distributed vector similarity search used with a lightweight SDK.
* [Qdrant](https://qdrant/qdrant) - An open source vector similarity search engine with extended filtering support.

## File System

*Tools related to file system and data storage.*

* [Alluxio](https://Alluxio/alluxio) - A virtual distributed storage system.
* [Amazon Simple Storage Service (S3)](https://aws.amazon.com/s3/) - Object storage built to retrieve any amount of data from anywhere.
* [Apache Hadoop Distributed File System (HDFS)](https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-hdfs/HdfsDesign.html) - A distributed file system.
* [GlusterFS](https://gluster/glusterfs) - A software defined distributed storage that can scale to several petabytes.
* [Google Cloud Storage (GCS)](https://cloud.google.com/storage) - Object storage for companies of all sizes, to store any amount of data.
* [LakeFS](https://treeverse/lakeFS) - Open source tool that transforms your object storage into a Git-like repository.
* [LizardFS](https://lizardfs/lizardfs) - A highly reliable, scalable and efficient distributed file system.
* [MinIO](https://minio/minio) - High Performance, Kubernetes Native Object Storage compatible with Amazon S3 API.
* [SeaweedFS](https://chrislusf/seaweedfs) - A fast distributed storage system for blobs, objects, files, and data lake.
* [Swift](https://openstack/swift) - A distributed object storage system designed to scale from a single machine to thousands of servers.

## Logging and Monitoring

*Tools used for logging and monitoring data workflows.*

* [Grafana](https://grafana/grafana) - Visualize metrics, logs, and traces from multiple sources like Prometheus, Loki, InfluxDB and more.
* [Loki](https://grafana/loki) - A horizontally-scalable, highly-available, multi-tenant log aggregation system inspired by Prometheus.
* [Prometheus](https://prometheus/prometheus) - A monitoring system and time series database.
* [Whylogs](https://whylabs/whylogs) - A tool for creating data logs, enabling monitoring for data drift and data quality issues.

## Metadata Service

*Tools used for storing and serving metadata.*

* [Hive Metastore](https://cwiki.apache.org/confluence/display/hive/design#Design-Metastore) - Service that stores metadata related to Apache Hive and other services.
* [Metacat](https://Netflix/metacat) - Provides you information about what data you have, where it resides and how to process it.

## SQL Playground

*Tools for testing and sharing SQL snippets in mock databases.*

* [RunSQL](https://runsql.com/) - Free online SQL playground for MySQL, PostgreSQL, and SQL Server.
* [SQLFiddle](https://sqlfiddle.com/) - Online SQL compiler for learning and practicing SQL.

## SQL Query Engine

*Tools for parallel processing SQL statements.*

* [Apache Drill](https://apache/drill) - Schema-free SQL Query Engine for Hadoop, NoSQL and Cloud Storage.
* [Apache Impala](https://apache/impala) - Lightning-fast, distributed SQL queries for petabytes of data.
* [Dremio](https://www.dremio.com/) - Power high-performing BI dashboards and interactive analytics directly on data lake.
* [Presto](https://prestodb/presto) - A distributed SQL query engine for big data.
* [Trino](https://trinodb/trino) - A fast distributed SQL query engine for big data analytics.

---

# Resources

Where to discover new tools and discuss about existing ones.

## Books

* [Data Mesh: Delivering Data-Driven Value at Scale](https://www.oreilly.com/library/view/data-mesh/9781492092384/) (O'Reilly)
* [Designing Data-Intensive Applications](https://www.oreilly.com/library/view/designing-data-intensive-applications/9781491903063/) (O'Reilly)
* [Fundamentals of Data Engineering](https://www.oreilly.com/library/view/fundamentals-of-data/9781098108298/) (O'Reilly)
* [Getting Started with Impala](https://www.oreilly.com/library/view/getting-started-with/9781491905760/) (O'Reilly)
* [Learning and Operating Presto](https://www.oreilly.com/library/view/learning-and-operating/9781098141844/) (O'Reilly)
* [Learning Spark: Lightning-Fast Data Analytics](https://www.oreilly.com/library/view/learning-spark-2nd/9781492050032/) (O'Reilly)
* [Spark in Action](https://www.oreilly.com/library/view/spark-in-action/9781617295522/) (O'Reilly)
* [Spark: The Definitive Guide](https://www.oreilly.com/library/view/spark-the-definitive/9781491912201/) (O'Reilly)

## Other Lists

* [Awesome Data Engineering](https://igorbarinov/awesome-data-engineering)
* [Awesome MLOps](https://kelvins/awesome-mlops)
* [DataOps Resource](https://chen1649chenli/dataOpsResource)

## Slack

* [Delta Lake Workspace](https://delta-users.slack.com/ssb/redirect)
* [Trino Workspace](https://trinodb.slack.com/ssb/redirect)

---

# Contributing

All contributions are welcome! Please take a look at the [contribution guidelines](https://kelvins/awesome-dataops/blob/main/CONTRIBUTING.md) first.
