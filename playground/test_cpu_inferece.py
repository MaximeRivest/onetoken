import llama_cpp

llm = llama_cpp.Llama(model_path="/home/maxime/.cache/huggingface/hub/models--google--gemma-3-1b-it-qat-q4_0-gguf/snapshots/d1be121d36172a4b0b964657e2ee859d61138593/gemma-3-1b-it-q4_0.gguf")  # <-- update the filename if different

response = llm("Hello, how are you?", max_tokens=1000)    # OR: llm(prompt="Hello, how are you?")

print(response['choices'][0]['text'])   # The completion is in this key.