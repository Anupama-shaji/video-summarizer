import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

MODEL_NAME = "Qwen/Qwen2.5-3B-Instruct"

tokenizer = None
model = None

def load_model():
    global tokenizer, model
    if model is not None:
        return

    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

    model = AutoModelForCausalLM.from_pretrained(
        MODEL_NAME,
        device_map="auto",
        torch_dtype=torch.float16
    )


def summarize_text(text, length="medium"):
    load_model()   # Lazy loading (loads only once)

    # 🎯 Control summary size based on frontend selection
    if length == "short":
        max_tokens = 60
    elif length == "long":
        max_tokens = 180
    else:  # medium
        max_tokens = 120

    prompt = f"""
Summarize the following transcript clearly.
Focus on the main ideas and important points.

Transcript:
{text}

Summary:
"""

    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        truncation=True,
        max_length=2048
    ).to(model.device)

    outputs = model.generate(
        **inputs,
        max_new_tokens=max_tokens,
        do_sample=False
    )

    result = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # Return only the summary part
    return result.split("Summary:")[-1].strip()
