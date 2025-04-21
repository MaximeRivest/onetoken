# onetokenpy [v0.1.1 - Work In Progress]

A Python library for quick and efficient data classification and clustering.

## Current Status
This project is under active development. The README outlines both currently implemented features and our roadmap. Features marked with ✅ are available in v0.1.1, while others are planned for future releases.

## Overview

onetokenpy will provide multiple ways to classify your data:

1. **Remote service** (Coming soon) - Access OneToken.AI's free-tier hosted classification service for the fastest and easiest setup
2. **Local processing** (Coming soon) - Run on your own hardware (CPU or GPU) for complete control and data privacy
3. **LLM providers** (Coming soon) - Connect to your preferred LLM service for specialized classification tasks

## Installation

### Basic Installation (Remote only) (Coming soon)
```bash
pip install onetokenpy
```

### With local CPU Support (Coming soon)
```bash
pip install onetokenpy
```
*Note: Will require Ollama or use Huggingface as a fallback. Will leverage llama.cpp if installed.*

### With local GPU Support (Coming soon)
```bash
pip install "onetokenpy[gpu]"
```
*Will install and use vllm as backend.*

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

## Roadmap: Advanced Usage (Coming Soon)

onetokenpy is being designed for easy discovery of supported providers and models. Your code editor will provide autocompletion as you type (in VS Code or Cursor, try typing `ot.classify.remotely.` and press tab).

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

### Full API (Partially Implemented)

```python
ot.classify(
    data,                           # DataFrame or list
    template_prompt,                # String with {column_name} placeholders
    system_prompt=None,             # Optional system prompt
    model_provider='onetoken',      # Default provider
    model='gemma_4b',               # Default model
    response_col_name='generated_text',
    add_model_id_col=False,         # Add column with model identifier
    add_prompt_col=False,           # Add column with generated prompts
    return_only_results_as_list=False,
    filter_on=None                  # Convenience filter (e.g. 'Yes')
)
```

## License

MIT License

## Author

Maxime Rivest (mrive052@gmail.com) 