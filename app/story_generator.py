from transformers import AutoTokenizer, AutoModelForCausalLM
import torch


model_name = "databricks/dolly-v2-3b"

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float16  # Reduce memory footprint
).to("cuda")  

def generate_story(topic: str) -> str:
    prompt = (
        f"Story Title: James Frostheart and the Fall of Civilization\n\n"
        f"Write a story in a literary, immersive tone. No user comments, reviews, ratings, or summaries.\n"
        f"James Frostheart is an 18-year-old genius living in a fortified outpost in a post-apocalyptic Earth. "
        f"His AI companion Stella, blunt and strategic, helps him defend against marauders, cyborg armies, and internal breakdowns. "
        f"Include a rich world, deep inner conflict, emotional growth, and a meaningful resolution.\n\n"
        f"Topic: {topic}\n"
        f"Begin the story:"
    )

    
    inputs = tokenizer(prompt, return_tensors="pt").to("cuda")

    
    outputs = model.generate(
        **inputs,
        max_new_tokens=1024,
        do_sample=True,
        top_k=50,
        top_p=0.9,
        temperature=0.85,
        repetition_penalty=1.2
    )
    
    return tokenizer.decode(outputs[0], skip_special_tokens=True)
