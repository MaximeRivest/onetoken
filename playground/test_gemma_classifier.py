from onetoken import classify
import huggingface_hub

huggingface_hub.login("REMOVED_TOKEN")

def main():
    # Test data
    reviews = [
        "This product is amazing! Best purchase ever!",
        "The quality is terrible, complete waste of money.",
        "It's okay, nothing special but gets the job done."
    ]
    
    # Prompt template
    prompt_template = "Classify the sentiment of this product review as 'positive', 'negative', or 'neutral': {text}"
    
    print("Testing Gemma classifier with llama.cpp...")
    results = classify(
        data=reviews,
        prompt_template=prompt_template,
        model_path="google/gemma-3-1b-it-qat-q4_0-gguf",  # Hugging Face repo ID
        device="cpu"
    )
    
    print("\nResults:")
    print(results)

if __name__ == "__main__":
    main() 