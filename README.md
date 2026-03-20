# adi-ml-toolkit

Just a handy Python metapackage I put together to save time during hackathons. It installs all the common AI, ML, NLP, and web deployment libraries at once (with compatible minimum versions), so you don't have to keep running `pip install` for an hour during competitions.

## Quick Start

```bash
pip install adi-ml-toolkit
```

## What it installs (The Complete Arsenal)

Here is a detailed breakdown of every single library this toolkit instantly configures for your environment:

### Core Data Science & ML
*   **numpy:** High-performance numerical computing and array manipulation.
*   **pandas:** Essential tabular data manipulation and analysis structure.
*   **scipy:** Advanced scientific computing algorithms (integrations, solvers).
*   **scikit-learn:** Core foundational ML algorithms (classification, clustering, regression).
*   **xgboost:** Highly optimized gradient boosting library.
*   **lightgbm:** Microsoft's fast and highly efficient gradient boosting.
*   **catboost:** Yandex's gradient boosting specially tuned for categorical features.

### Deep Learning Frameworks
*   **torch:** PyTorch's core tensor and autograd deep learning framework.
*   **torchvision:** standard PyTorch image transformations and pre-trained CV models.
*   **torchaudio:** standard PyTorch tools for audio processing.
*   **pytorch-lightning:** High-level PyTorch wrapper to simplify training loops and make them robust.
*   **fastai:** High-level PyTorch wrapper optimized for incredibly rapid prototyping.
*   **tensorflow:** Google's enterprise deep learning framework.
*   **tensorflow-decision-forests:** Specialized TensorFlow models for structured data.
*   **keras:** Simple, high-level neural network API.
*   **jax[cpu]:** Google's super high-performance array computing and autograd framework.

### NLP & Foundation Models (HuggingFace)
*   **transformers:** Hugging Face's flagship LLM and foundation model repository.
*   **datasets:** One-line access to thousands of audio, vision, and text training datasets.
*   **accelerate:** PyTorch wrapper for seamless multi-GPU hardware acceleration.
*   **huggingface-hub:** Official client to download models from the Hugging Face Hub.
*   **sentence-transformers:** Create fast, state-of-the-art text and image embeddings.
*   **spacy:** Industrial-strength, production-ready NLP pipelines.
*   **nltk:** Traditional, academic natural language processing toolkit.
*   **gensim:** Unsupervised topic modeling and text similarity calculations.

### Generative AI, Agents & Vector DBs
*   **langchain:** The leading framework for chaining and building LLM applications.
*   **langchain-openai:** Official LangChain integrations for OpenAI models.
*   **langgraph:** Build complex, stateful agentic workflows and cycles with LLMs.
*   **openai:** Official GPT-4 and embeddings API client.
*   **anthropic:** Official Claude API client.
*   **google-generativeai:** Official Google Gemini API client.
*   **chromadb:** Simple, local, open-source vector database.
*   **pinecone-client:** Official client for Pinecone's cloud vector database.
*   **qdrant-client:** Fast vector search engine client.
*   **tiktoken:** OpenAI's hyper-fast byte pair encoding tokenizer.
*   **llama-index:** Data framework for securely connecting custom data to LLMs.
*   **crewai:** Framework for orchestrating autonomous, role-playing AI agents.
*   **autogen-agentchat & pyautogen:** Conversational framework for multi-agent systems.
*   **semantic-kernel:** Microsoft's enterprise-grade AI agent orchestration framework.

### Computer Vision & Healthcare
*   **opencv-python-headless:** Essential open-source computer vision processing (headless for server compatibility).
*   **pillow:** Standard Python imaging library (PIL) for basic image ops.
*   **scikit-image:** Advanced mathematical image processing linked with SciPy.
*   **monai:** Medical deep learning framework (the global standard for healthcare hackathons).

### Time Series, Audio, & Visualization
*   **librosa:** Extensive music and audio analysis feature extraction.
*   **statsmodels:** Traditional statistical modeling and hypothesis testing.
*   **prophet:** Robust time-series forecasting algorithm developed by Meta.
*   **matplotlib:** Foundational Python plotting library.
*   **seaborn:** Beautiful, high-level statistical data visualization.
*   **plotly:** Interactive, web-based, stunning graphical plots.

### Jupyter & MLOps (AutoML & Tracking)
*   **jupyterlab & notebook:** Classic web-based interactive coding environments.
*   **ipywidgets:** Interactive HTML widgets for dynamic notebooks.
*   **mlflow:** Manage the ML lifecycle and meticulously track experiments.
*   **wandb:** Weights & Biases for beautifully visualizing model training runs in the cloud.
*   **optuna:** Automated and hyper-efficient hyperparameter optimization.
*   **pycaret:** Low-code library for end-to-end rapid ML model deployment.
*   **autogluon:** Automates completely the process of model selection and ensembling.

### Web Apps & Server APIs
*   **fastapi:** Ultra-fast, modern web framework for Python APIs.
*   **uvicorn:** Lightning-fast ASGI server required for running FastAPI.
*   **flask:** Classic, extremely lightweight web application framework.
*   **streamlit:** Turn python data scripts into interactive shareable web apps in literally minutes.
*   **gradio:** Build quick, shareable web UIs specifically for machine learning models.
*   **pydantic:** Robust data validation parsing using Python type hints.
*   **python-multipart:** Support for parsing form data uploads (crucial for FastAPI file uploads).

### General Utilities & Databases
*   **requests:** The standard library to make HTTP requests easily.
*   **beautifulsoup4:** Parse HTML and XML documents effortlessly (web scraping standard).
*   **python-dotenv:** Read variables securely from `.env` files.
*   **sqlalchemy:** Powerful SQL toolkit and Object-Relational Mapper.
*   **pymongo:** Official driver for MongoDB NoSQL databases.
*   **redis:** High-performance Redis key-value store client.
*   **celery:** Distributed task queue processing mechanism.

## Setup Tools (Optional)

It also includes a small python script that helps you globally install common CLIs (like Vercel, Heroku, AWS CLI, Netlify) so your deployment environment is ready to go. Run:

```bash
ml-setup-clis
```

## Contributing

Feel free to open a PR if you think I missed a useful library or CLI tool.

