# GenAI Launchpad Boilerplate

With AI innovation moving beyond the speed of light, your time to develop is now more precious than ever. That’s why we’ve built the GenAI Launchpad – your secret weapon to shipping production-ready AI apps, faster.

## Introduction

Welcome to the GenAI Launchpad – your all-in-one repository for building powerful, scalable Generative AI applications. Whether you’re prototyping or deploying at scale, this Docker-based setup has you covered with everything from event-driven architecture to seamless AI pipeline integration.

No need to start from scratch or waste time on repetitive configurations. The GenAI Launchpad is engineered to get you up and running fast, with a flexible design that fits your workflow – all while keeping things production-ready from day one

## Table of Contents

- [GenAI Launchpad Boilerplate](#genai-launchpad-boilerplate)
  - [Introduction](#introduction)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Key Features](#key-features)
  - [Project Structure](#project-structure)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Quick Start](#quick-start)
      - [1. Clone the repository](#1-clone-the-repository)
      - [2. Set up environment files](#2-set-up-environment-files)
      - [3. Build and start the Docker containers](#3-build-and-start-the-docker-containers)
      - [4. Make database migrations](#4-make-database-migrations)
      - [5. Create virtual environment and install requirements](#5-create-virtual-environment-and-install-requirements)
      - [6. Check database](#6-check-database)
      - [7. Build Your Project](#7-build-your-project)

## Overview

The GenAI Launchpad isn’t just another framework – it’s your shortcut to a production-ready AI infrastructure. Built for speed and control, its modular architecture brings together the best tools and design patterns to help you deploy faster without compromising flexibility.

Here’s what you’re working with:

- FastAPI for lightning-fast API development
- Celery for background task processing
- PostgreSQL to handle all your data, includding embeddings
- Redis for fast task queue management
- Caddy for reverse proxy and automatic HTTPS

All services are containerized using Docker, ensuring consistency across development and deployment environments.

## Key Features

- **Event-Driven Architecture**: Built-in support for designing and implementing event-driven systems.
- **AI Pipeline Support**: Pre-configured setup for integrating AI models and pipelines.
- **Scalability**: Designed with scalability in mind, allowing easy expansion as your application grows.
- **Flexibility**: Modular architecture that allows for easy customization and extension.
- **Production-Ready**: Includes essential components for a production environment, including logging, monitoring, and security features.
- **Rapid Development**: Boilerplate code and project structure to accelerate development.
- **Docker-Based Deployment**: Complete Docker-based strategy for straightforward deployment.

## Project Structure

The Launchpad follows a logical, scalable, and reasonably standardized project structure for building event-driven GenAI apps.

```text
├── app
│   ├── alembic            # Database migration scripts
│   ├── api                # API endpoints and routers
│   ├── config             # Configuration files
│   ├── core               # Components for pipeline and task processing
│   ├── database           # Database models and utilities
│   ├── pipelines          # AI pipeline definitions
│   ├── prompts            # Prompt templates for AI models
│   ├── services           # Business logic and services
│   ├── tasks              # Background task definitions
│   └── utils              # Utility functions and helpers
├── docker                 # Docker configuration files
├── docs                   # Project documentation
├── playground             # Run experiments for pipeline design
└── requests               # Event definitions and handlers
```

## Getting Started

### Prerequisites

- Git
- Python 3
- Docker (Updated to support docker compose)
- VS Code or Cursor (optional, but recommended)

### Quick Start

#### 1. Clone the repository

```bash
git clone https://github.com/datalumina/genai-launchpad.git
cd genai-launchpad
```

#### 2. Set up environment files

```bash
cp app/.env.example app/.env
cp docker/.env.example docker/.env
```

You can leave the `docker/.env` file as is for the quick start. However, you need to add your OpenAI API key to the `app/.env` file. Open `app/.env` and locate the `OPENAI_API_KEY` variable. Replace its value with your actual OpenAI API key:

```yaml
OPENAI_API_KEY=your_openai_api_key_here
```

#### 3. Build and start the Docker containers

```bash
cd ./docker
./start.sh
```

To run .sh scripts on Windows, install [Git Bash](https://git-scm.com/downloads/win), then right-click in the script’s folder and select “Git Bash Here.” Use ./scriptname.sh in the Git Bash terminal to execute the script.

#### 4. Make database migrations

```bash
cd ../app
./makemigration.sh  # Create a new migration
./migrate.sh        # Apply migrations
```

#### 5. Create virtual environment and install requirements

```bash
# Create a new virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS and Linux:
source venv/bin/activate

# Install the required packages
cd app
pip install -r requirements.txt
```

#### 6. Check database

Connect to the database using your favorite database explorer. The default settings are:

- Host: localhost
- Port: 5432
- Database: launchpad
- Username: postgres
- Password: super-secret-postgres-password

In the `events` table, you should see the event you just processed. It contains the raw data (JSON) in the `data` column and the processed event (JSON) with in the `task_context` column.

#### 7. Build Your Project 

Here's a high-level action plan to update the template for your unique project:

1. Update the '.env' files with your API keys and passwords
2. Update your settings in `app/config`
3. Define the event(s) in `requests/events` (your incoming data)
4. Update the API schema in `app/api/event_schema.py` (matching your events)
5. Define your AI pipelines and processing steps in `app/pipelines/`
6. Register your pipeline(s) in `app/pipelines/registry.py`
7. Test your pipeline with sample events in the playground