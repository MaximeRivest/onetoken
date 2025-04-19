# %% [markdown]
# # Onetoken Classifier Playground


#%%
import onetoken as ot
ot.classify([
    "This movie was amazing!",
    "The service was terrible.",
    "I had a great experience.",
    "Would not recommend."
],
"""Is this text positive?
Text: {text}
Answer with only Yes or No.

""")







# %% [markdown]
# This notebook demonstrates different ways to use the onetoken classifier with various data types and prompt templates.

# %%
from onetoken.classifier import classify
import pandas as pd
import huggingface_hub

# Ensure you are logged in if using private models or for quota management
# huggingface_hub.login("YOUR_HF_TOKEN") # Replace with your token or use login() for interactive
#huggingface_hub.login("REMOVED_TOKEN")


# %% [markdown]
# ## 1. Basic Classification (Auto-detect device, likely CPU)

# %%
data_df1 = pd.DataFrame({
    'text': [
        'This movie was amazing!',
        'The service was terrible.',
        'I had a great experience.',
        'Would not recommend.'
    ]
})

#%%

# Explicitly provide model path, assuming CPU for this basic test
# If you have a GPU and want to test auto-detection, you might need
# to provide a model compatible with vLLM (e.g., DEFAULT_GPU_MODEL)
results1 = classify(data_df1, 
                    """Is this text positive? 
Text: {text}
Answer with only Yes or No.""",
                    model_path="google/gemma-3-4b-it-qat-q4_0-gguf"
                    )
results1

#%%
results1["classification"]
# %% [markdown]
# ## 2. List Input (Explicit CPU)

# %%
data_list2 = [
    'The weather is beautiful today',
    'I feel sick and tired',
    'This is the best day ever',
    'I am so disappointed'
]

# Use {text} for list input
prompt_template2 = """Classify this text as Positive or Negative: {text}.

RESPOND ONLY WITH Positive or Negative

"""

# Explicitly specify CPU device and compatible model
results2 = classify(data_list2, prompt_template2, model_path="google/gemma-3-4b-it-qat-q4_0-gguf", device="cpu")
print("\n--- Results 2 (List, CPU) ---")
print(results2)
