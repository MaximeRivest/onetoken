# onetokenpy

[![PyPI version](https://badge.fury.io/py/onetokenpy.svg)](https://badge.fury.io/py/onetokenpy) [![License: Apache-2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

**A flexible, open-source Python library for fast and easy data classification and clustering using Large Language Models (LLMs), optimized for performance.**

## Current Status (April 21, 2025)

**Targeting Beta Release (v0.2.0): June 2025**

This project is under active development, focusing on high-performance local processing and core features for the initial beta release. We are committed to building a robust tool driven by community feedback.

**Feature Status (Targeting v0.2.0 Beta):**

* ✅ Core `ot.classify()` function
* ✅ Support for Pandas DataFrames as input
* ✅ Basic remote classification via Onetoken.ai (Free Tier)
* ✅ **Initial local classification support (via vLLM/GPU for high performance)**
* ⏳ Local classification support via CPU (Ollama, Hugging Face)
* ⏳ Advanced `ot.cluster()` functionality
* ⏳ Support for other LLM providers (OpenAI, Anthropic, etc.)

## Overview

`onetokenpy` aims to make leveraging the power of LLMs for data classification and clustering incredibly simple and **fast** within your Python workflows. Get meaningful insights from your data with just a few lines of code, running efficiently on your local GPU or using our convenient managed service.

## Key Features

* **Simple API:** Designed for ease of use, abstracting away complex LLM interactions.
* **Performance Focused:** Prioritizes high-throughput local processing using **vLLM on compatible NVIDIA GPUs**.
* **Flexible Execution:** You choose how to run your tasks:
    * **Local GPU Processing:** Achieve maximum performance and data privacy by running directly on your own hardware with vLLM. (CPU support coming soon!)
    * **Managed Service:** Use the optional, convenient `Onetoken.ai` service (includes a free tier) for zero-setup classification – perfect for getting started quickly or when GPU resources aren't available.
* **Pandas Integration:** Works seamlessly with your existing Pandas DataFrames.
* **Open Source:** MIT licensed, encouraging community involvement and transparency.

## Our Philosophy: Performance, Choice, and Sustainability

Our primary goal is to build `onetokenpy` into a powerful, community-driven open-source library with a strong emphasis on performance. We also believe in giving users choice and control.

* **Run Locally (GPU First):** We are launching with high-performance local GPU support via vLLM. This allows you to leverage your hardware for speed and ensure data privacy. We are actively working on adding CPU-based local backends (like Ollama) for broader accessibility soon after launch.
* **Use the Service:** We also offer the `Onetoken.ai` managed service as a convenient option. The **free tier** provides an easy way to get started without any local setup.
* **Sustainability:** To support the ongoing development and maintenance of *both* the open-source library (including adding CPU support) and the managed service infrastructure, we plan to introduce premium tiers for the `Onetoken.ai` service in the future. This ensures the project's long-term health and allows us to keep improving `onetokenpy` for everyone.

## Installation

Choose the installation method that suits your needs:

```bash
# Core library (includes client for Onetoken.ai free tier access)
pip install onetokenpy

# --- For High-Performance Local GPU Processing ---
# This is the primary local backend for the initial release.
pip install "onetokenpy[gpu]"

# will install vllm backend

# --- For Local CPU Processing (Coming Soon!) ---
# Support for Ollama and Hugging Face Transformers is planned for a future release.
# pip install onetokenpy[ollama]
# pip install onetokenpy[hf]
```

## Quick Start Example (Coming soon)

Classify Canadian postal codes in three simple steps:

```python
import pandas as pd
import onetokenpy as ot

# 1. Create your data
df = pd.DataFrame({
    'postal_codes': ['H2X 1Y1', '12345', 'ABC123', 'K1A 0B1']
})

# 2. Classify data with a prompt
# This example might default to the Onetoken.ai free tier for ease of use.
# To run locally with high performance, ensure you have a compatible GPU setup
# (see Installation) and specify execution_provider='vllm' as shown below.
result = ot.classify(
    df,
    "Classify this {postal_codes} as whether it is a correctly formatted Canadian postal code. Answer only by Yes or No"
)

# 3. Filter the results
print(result)
# Output:
#   postal_codes generated_text
# 0     H2X 1Y1            Yes
# 1       12345             No
# 2      ABC123             No
# 3     K1A 0B1            Yes

# Find only valid Canadian postal codes
canadian_postals = result[result["generated_text"] == "Yes"]
print(canadian_postals)
# Output:
#   postal_codes generated_text
# 0     H2X 1Y1            Yes
# 3     K1A 0B1            Yes
```

That's it! With just a few lines of code, you can classify any dataset using the power of LLMs.

### Planned Function Structure

```python
# Default approach used in the example above
ot.classify.remotely.onetoken.gemma_4b()

# General pattern
ot.classify.remotely.provider.model()

# Clustering is also being developed
ot.cluster...

# Local processing options (planned)
ot.classify.locally.vllm.model()         # Fastest for GPU when model fits in VRAM
ot.classify.locally.ollama.model()
ot.classify.locally.huggingface.model()
ot.classify.locally.llama_cpp.model()
```


  * **`onetoken` (Remote):**
      * **Pros:** Easiest setup, no local dependencies needed, managed infrastructure.
      * **Cons:** Requires network access, relies on `Onetoken.ai` availability, free tier limits (paid tiers planned).
  * **`vllm` (Local GPU):**
      * **Pros:** **Highest performance/throughput**, full control over models, data stays local (privacy), no external service dependency.
      * **Cons:** **Requires compatible NVIDIA GPU and setup (CUDA, vLLM)**, higher hardware cost/access barrier.
  * **`ollama` / `hf` (Local CPU - Coming Soon):**
      * **Pros:** Broader accessibility (runs on CPU), data stays local.
      * **Cons:** Lower performance than GPU, requires managing local backend (Ollama/HF).

## Full API (Targeting Beta v0.2.0)

```python
ot.classify(
    data,                           # DataFrame or list of strings/dicts
    template_prompt,                # String with {column_name} placeholders
    system_prompt=None,             # Optional system prompt for the LLM
    execution_provider='onetoken',  # 'onetoken', 'vllm' (initially). 'ollama', 'hf' planned.
    model=None,                     # Specific model name (optional, defaults per provider)
                                    # e.g., 'google/gemma-7b' for 'onetoken',
                                    # 'meta-llama/Llama-2-7b-chat-hf' for 'vllm' (examples)
    response_col_name='generated_text', # Name for the column with LLM results
    add_model_id_col=False,         # Add column identifying the model used
    add_prompt_col=False,           # Add column showing the exact prompt sent
    return_only_results_as_list=False, # Return only the generated text as a list
    filter_on=None                  # Convenience filter (e.g. 'Yes') to apply post-generation
)

# Clustering (API Design TBD)
# ot.cluster(...)
```

## Roadmap

We are focused on building `onetokenpy` sustainably for the long term, starting with performance.

  * **Near-Term (Post-Beta v0.2.0):**
      * **Add Local CPU Support:** Implement backends for Ollama and Hugging Face Transformers (`execution_provider='ollama'`, `execution_provider='hf'`).
      * Refine and expand `ot.cluster()` functionality.
      * Enhance documentation with more performance tuning tips, tutorials, and use cases.
      * Actively incorporate community feedback from beta users.
  * **Mid-Term:**
      * Introduce **paid tiers** for the `Onetoken.ai` service (higher rate limits, access to more powerful models, potential team features, support options) to fund development.
      * Develop `onetokenjs`: A JavaScript version targeting Node.js and browsers (likely starting with `Onetoken.ai` service integration).
      * Add support for using external LLM providers via their APIs (OpenAI, Anthropic, Gemini, etc.), likely requiring user-provided API keys.
  * **Long-Term:**
      * Explore libraries for other data science languages (R, Julia).
      * Add more sophisticated classification/clustering techniques.
      * Potential enterprise features/support for the `Onetoken.ai` service.
      * Continuous improvement based on LLM advancements and community needs.

## Contributing

We welcome contributions from the community\! Whether it's reporting bugs, suggesting features, improving documentation, optimizing performance, or submitting code, your help is valued.


## License

This project is licensed under the Apache 2.0 License

## Author

Maxime Rivest


