import torch
from transformers import MT5ForConditionalGeneration, MT5Tokenizer

def add_prefix_to_texts(texts: list[str], prefix: str) -> list[str]:
    return [f"{prefix}{text}" for text in texts]

def generate_translation_batch(texts : list[str], model_dir, max_input_len=128, max_output_len=128, batch_size=32):
    tokenizer = MT5Tokenizer.from_pretrained(model_dir)
    model = MT5ForConditionalGeneration.from_pretrained(model_dir, torch_dtype=torch.float32)

    all_outputs = []

    prefixed_texts = add_prefix_to_texts(texts, 'translate Vietnamese_nom to Vietnamese: ')

    for i in range(0, len(prefixed_texts), batch_size):
        batch_texts = prefixed_texts[i:i+batch_size]
        inputs = tokenizer(batch_texts, return_tensors="pt", padding=True, truncation=True, max_length=max_input_len)
        input_ids = inputs.input_ids.to(model.device)
        attention_mask = inputs.attention_mask.to(model.device)

        with torch.no_grad():
            outputs = model.generate(
                input_ids=input_ids,
                attention_mask=attention_mask,
                max_length=max_output_len,
                num_beams=4,
                early_stopping=True
            )

        decoded = tokenizer.batch_decode(outputs, skip_special_tokens=True)
        all_outputs.extend(decoded)

    return all_outputs