# adi-ml-toolkit

Just a handy Python metapackage I put together to save time during hackathons. It installs all the common AI, ML, NLP, and web deployment libraries at once (with compatible minimum versions), so you don't have to keep running `pip install` for an hour during competitions.

## Quick Start

```bash
pip install adi-ml-toolkit
```

## What it installs

*   **Deep Learning:** torch, torchvision, jax, fastai, tensorflow
*   **NLP & Agents:** transformers, langchain, langgraph, openai, huggingface-hub, autogen
*   **Classic ML:** scikit-learn, xgboost, lightgbm
*   **Web Frameworks:** fastapi, flask, streamlit, gradio
*   **Data Science:** pandas, numpy, matplotlib, seaborn

*Note: Check `pyproject.toml` for the full list of dependencies.*

## Setup Tools (Optional)

It also includes a small python script that helps you globally install common CLIs (like Vercel, Heroku, AWS CLI, Netlify) so your deployment environment is ready to go. Run:

```bash
ml-setup-clis
```

## Contributing

Feel free to open a PR if you think I missed a useful library or CLI tool.

