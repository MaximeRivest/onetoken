# onetoken

A Python library for running local LLM classification tasks on data. Supports both GPU (using vLLM) and CPU (using Ollama) inference.

## Installation

### Basic Installation (CPU only)
```bash
pip install onetoken
```

### GPU Support
If you have a GPU and want to use vLLM for faster inference:
```bash
pip install "onetoken[gpu]"
```

## Usage

```python
import onetoken as ot
import pandas as pd

# Create a sample dataframe
df = pd.DataFrame({
    'postal_codes': ['H2X 1Y1', '12345', 'ABC123', 'K1A 0B1']
})

# Classify the postal codes
result = ot.classify(
    df,
    """Classify this {col_value} as whether it is a correctly formatted postal code. Answer only by Yes or No"""
)

print(result)
```

## Features

- Run local LLM classification tasks on pandas DataFrames or lists
- Automatic GPU detection and backend selection
- Uses vLLM for GPU inference (faster)
- Uses Ollama for CPU inference (more accessible)
- Default model is Gemma 3 4B for GPU, Gemma 2B for CPU
- Returns results with original data, classifications, and prompts

## Requirements

- Python 3.8+
- For GPU support: CUDA-compatible GPU and vLLM
- For CPU support: Ollama

## License

MIT License

## Author

Maxime Rivest (mrive052@gmail.com) 