Okay, let's embrace the ambition\! We'll structure the README around the fluent API (`ot.classify.locally.vllm.model()`) as the target design, acknowledging the significant work required to make the dynamic, context-aware autocomplete a reality.

This version presents the fluent API as the core vision for usability, while noting the initial Beta release will use a more conventional approach as a stepping stone.

````markdown
# onetokenpy

[![PyPI version](https://badge.fury.io/py/onetokenpy.svg)](https://badge.fury.io/py/onetokenpy) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
**A flexible, open-source Python library for fast and easy data classification and clustering using Large Language Models (LLMs), optimized for performance and designed for an intuitive user experience.**

## Current Status (April 21, 2025)

**Targeting Beta Release (v0.2.0): June 2025**

This project is under active development. The immediate focus is on delivering core functionality with high-performance local GPU support (vLLM) and remote access via Onetoken.ai. The revolutionary fluent API with dynamic autocomplete is our key post-Beta goal.

**Feature Status (Targeting v0.2.0 Beta):**

* ✅ Core classification engine
* ✅ Support for Pandas DataFrames
* ✅ Remote classification via `Onetoken.ai` (Free Tier) through keyword arguments
* ✅ **Local classification via `vLLM/GPU`** through keyword arguments
* ⏳ **Fluent API Structure (`ot.classify.<type>.<provider>.<model>`)** - Post-Beta Target
* ⏳ **Dynamic Autocomplete for Models (Context-Aware)** - Post-Beta Target
* ⏳ Local classification support via CPU (Ollama, Hugging Face) - Post-Beta Target
* ⏳ Advanced `ot.cluster()` functionality

## Overview

`onetokenpy` aims to make leveraging the power of LLMs for data classification and clustering incredibly simple and **fast**. Our vision is an API so intuitive that discovering and using the right models – whether remote or running locally on your hardware – feels effortless, aided by dynamic, context-aware autocomplete features built right into your development environment.

## Key Features

* **Performance Focused:** High-throughput local processing using **vLLM on compatible NVIDIA GPUs** is prioritized from the start.
* **Flexible Execution:** Run tasks locally (GPU now, CPU planned) for control and privacy, or use the managed `Onetoken.ai` service for convenience.
* **Pandas Integration:** Works seamlessly with Pandas DataFrames.
* **Open Source:** MIT licensed, fostering community involvement.
* **(Vision) Intuitive Fluent API:** Designed for effortless discovery via a chained `ot.classify.<type>.<provider>.<model>()` structure.
* **(Vision) Dynamic Autocomplete:** Aiming for groundbreaking IDE autocomplete that suggests models based on your environment (Ollama list, GPU VRAM, benchmarks, downloaded models).

## Our Philosophy: Simplicity through Ambition

We believe interacting with powerful LLMs shouldn't require complex configuration. Our goal is to abstract complexity away behind a clean, fluent API. We are committed to tackling the technical challenges required to deliver a truly intuitive experience, including dynamic model discovery and context-aware suggestions directly in your IDE. While the initial Beta provides core functionality, our long-term focus is on realizing this ambitious vision.

## Installation

Get started with the core functionality:

```bash
# Core library (includes client for Onetoken.ai free tier access)
pip install onetokenpy

# --- For High-Performance Local GPU Processing (Required for Local Beta Usage) ---
pip install "onetokenpy[gpu]"

# IMPORTANT: Requires a compatible NVIDIA GPU, CUDA toolkit (matching PyTorch version),
# and Python 3.8+. vLLM will be installed as a dependency.
# Please consult the vLLM documentation for detailed setup requirements.

# --- For Local CPU Processing (Coming Post-Beta!) ---
# Support for Ollama and Hugging Face Transformers is planned.
# pip install onetokenpy[ollama] # Future
# pip install onetokenpy[hf] # Future
````

## Quick Start Example (Using Beta API)

Classify Canadian postal codes using the initial Beta API structure:

```python
import pandas as pd
import onetokenpy as ot

# 1. Create your data
df = pd.DataFrame({
    'postal_codes': ['H2X 1Y1', '12345', 'ABC123', 'K1A 0B1']
})

# 2. Classify data using the Beta's keyword arguments
#    This example uses the default provider (likely 'onetoken').
result = ot.classify(
    data=df,
    template_prompt="Is '{postal_codes}' a valid Canadian postal code format (LNL NLN)? Answer Yes or No."
    # To use local vLLM in Beta:
    # execution_provider='vllm',
    # model='meta-llama/Llama-2-7b-chat-hf' # Or another model compatible with your vLLM setup
)

# 3. Inspect the results
print(result)
# Expected Output:
#   postal_codes generated_text
# 0     H2X 1Y1            Yes
# 1       12345             No
# 2      ABC123             No
# 3     K1A 0B1            Yes
```

*See the "Fluent API Vision" section below for the planned future usage.*

## The Fluent API Vision (Target Design Post-Beta)

Our goal is to move beyond simple keyword arguments towards a highly intuitive, discoverable fluent API.

**Planned Structure:**

The core interaction point will become the `ot.classify` object itself, allowing you to chain calls to specify execution type, provider, and model:

```python
# --- Target API Structure ---

# Remotely using Onetoken.ai's gemma-7b model:
results = ot.classify.remotely.onetoken.gemma_7b(
    data=df, template_prompt=prompt
)

# Locally using vLLM with a specific (user-known) model:
results = ot.classify.locally.vllm.model( 'org/custom-model-id' )( # Call returns executor?
    data=df, template_prompt=prompt, temperature=0.5 # Pass data/params here? TBD
)
# Or maybe directly if model name is attribute-friendly:
# results = ot.classify.locally.vllm.Mistral_7B_Instruct(
#     data=df, template_prompt=prompt
# )

# Locally using Ollama (Future):
# results = ot.classify.locally.ollama.llama3(
#     data=df, template_prompt=prompt
# )

# Clustering (Future):
# results = ot.cluster.locally.vllm.some_embedding_model(...)
```

*(Note: The exact mechanism for passing data/prompts and parameters within this fluent chain is part of the ongoing design and implementation.)*

**The Autocomplete Ambition:**

This structure is designed to enable powerful IDE autocomplete:

1.  Type `ot.classify.` -\> suggests `locally`, `remotely` (and later `cluster`).
2.  Type `ot.classify.locally.` -\> suggests `vllm` (and later `ollama`, `hf`, `llama_cpp`).
3.  **The Goal:** Type `ot.classify.locally.vllm.` -\> **Here's the ambition\!** The suggestions should dynamically include:
      * Models already downloaded locally (detected from cache).
      * Top-performing models known to fit your detected GPU VRAM (requires runtime checks and benchmark data).
      * Potentially common model names as direct attributes/methods (e.g., `.Mistral_7B_Instruct`).
      * A generic `.model('model-id')` method to specify any model identifier directly.
4.  Similarly, `ot.classify.locally.ollama.` would suggest models from `ollama list`.
5.  `ot.classify.remotely.onetoken.` would suggest models available on the Onetoken.ai service.

**Realizing the Vision:** Achieving this level of dynamic, context-aware autocomplete directly within the IDE requires exploring advanced Python techniques and potentially novel approaches to IDE integration. It's a challenging but core part of the `onetokenpy` vision for ultimate ease-of-use.

## Provider Capabilities (Beta v0.2.0)

While the fluent API is developed, the Beta release uses keyword arguments (`execution_provider`, `model`) with the following providers:

  * **`onetoken` (Remote):**
      * **Pros:** Easiest setup, managed infrastructure.
      * **Cons:** Network dependency, service limits.
  * **`vllm` (Local GPU):**
      * **Pros:** Highest performance, data privacy, model control.
      * **Cons:** Requires NVIDIA GPU, CUDA, vLLM setup.
  * **`ollama` / `hf` (Local CPU - Coming Soon):** For broader accessibility.

## Full API (Targeting Beta v0.2.0 - Interim API)

The initial Beta release will use this function signature:

```python
ot.classify(
    data,                           # DataFrame or list of strings/dicts
    template_prompt,                # String with {column_name} placeholders
    system_prompt=None,             # Optional system prompt for the LLM
    # --- Beta Keyword Arguments ---
    execution_provider='onetoken',  # 'onetoken', 'vllm'. Others planned.
    model=None,                     # Specific model name (e.g., 'meta-llama/Llama-2-7b-chat-hf' for vllm)
    # --- Common Arguments ---
    response_col_name='generated_text',
    add_model_id_col=False,
    add_prompt_col=False,
    return_only_results_as_list=False,
    filter_on=None
)
```

## Roadmap

Our roadmap is driven by the vision of delivering the fluent API and its dynamic capabilities.

  * **Near-Term (Post-Beta v0.2.0):**
      * **Implement Fluent API Structure:** Build the core `ot.classify.<type>.<provider>.<model>` object structure.
      * **Develop Dynamic Discovery Engine:** Create the underlying logic for runtime checks (Ollama list, VRAM checks, cache scanning, benchmark integration, remote API querying).
      * **Explore Autocomplete Integration:** Research and implement techniques to expose dynamic suggestions to IDEs as effectively as possible.
      * **Add Local CPU Support:** Integrate Ollama and Hugging Face backends within the new fluent structure (`ot.classify.locally.ollama`, `ot.classify.locally.hf`).
      * Refine `ot.cluster()` functionality.
  * **Mid-Term:**
      * Introduce **paid tiers** for the `Onetoken.ai` service.
      * Develop `onetokenjs`.
      * Add support for external LLM providers (`ot.classify.remotely.openai`, etc.).
  * **Long-Term:**
      * R/Julia support, advanced features, enterprise options, continuous improvement.

## Contributing

We welcome ambitious contributors\! If you're interested in tackling the challenges of dynamic autocomplete, optimizing performance, or expanding provider support, please see `CONTRIBUTING.md` (link to be added) for guidelines.

## License

This project is licensed under the MIT License - see the [LICENSE](https://www.google.com/search?q=LICENSE) file for details.

## Author

Maxime Rivest ([email address removed])

```

**Key Changes:**

1.  **API Vision First:** The fluent API (`ot.classify.<type>.<provider>.<model>`) is now presented prominently as the core design goal ("The Fluent API Vision").
2.  **Autocomplete Ambition:** Explicitly describes the desired dynamic, context-aware autocomplete behavior as a central, ambitious goal.
3.  **Technical Challenge Acknowledged:** Frames the dynamic autocomplete as requiring innovation ("exploring advanced techniques", "challenging but core part").
4.  **Beta API as Interim:** Clearly positions the keyword-argument `ot.classify()` function as the initial Beta implementation, managing expectations for the first release.
5.  **Examples Updated:** Quick start shows Beta usage, while the Fluent API section shows examples of the target syntax (with notes about evolving details).
6.  **Roadmap Prioritization:** Implementing the fluent API and the dynamic discovery engine is now the top Near-Term priority post-Beta.
7.  **Removed Conflicting Designs:** Previous alternative API designs are omitted.

This README aligns with the ambitious vision for the fluent API and dynamic autocomplete, setting it as the guiding principle for future development while providing a clear picture of the initial Beta release.
```