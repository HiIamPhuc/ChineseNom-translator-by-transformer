# ChineseNom-translator-by-transformer

This repository contains a Chinese-Nom translation system built using the MT5 transformer model. The project is designed to translate Chinese-Nom text into Vietnamese using a pre-trained MT5 model fine-tuned for this specific task.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Model Details](#model-details)
- [Contributing](#contributing)
- [License](#license)

## Features
- **Translation**: Translate Chinese-Nom text into Vietnamese.
- **Streamlit UI**: A user-friendly web interface for translation.
- **Pre-trained Model**: Utilizes the MT5 model fine-tuned for Chinese-Nom to Vietnamese translation.

## Installation

### Prerequisites
- Python 3.8 or higher
- [PyTorch](https://pytorch.org/) (with GPU support recommended)
- [Streamlit](https://streamlit.io/)
- [Transformer](https://pypi.org/project/transformers/)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/HiIamPhuc/ChineseNom-translator-by-transformer.git
   cd ChineseNom-translator-by-transformer
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure the model files are in the `models/translation/mt5-nom-translator` directory.

## Usage

### Streamlit UI
1. Run the Streamlit app:
   ```bash
   streamlit run web/translator.py
   ```

2. Open the app in your browser at `http://localhost:8501`.

3. Enter Chinese-Nom text in the input area and click "Translate" to see the translated text.

### Programmatic Usage
You can use the `generate_translation_batch` function from `web/utils/translate.py` to perform translations programmatically:
```python
from utils.translate import generate_translation_batch

texts = ["Your Chinese-Nom text here"]
model_dir = "models/translation/mt5-nom-translator"
translations = generate_translation_batch(texts, model_dir)
print(translations)
```

## Model Details
The MT5 model is fine-tuned for translating Chinese-Nom text into Vietnamese. The model files are located in the `models/translation/mt5-nom-translator` directory.

### Key Files
- `model.safetensors`: The model weights.
- `tokenizer_config.json` and `spiece.model`: Tokenizer configuration and vocabulary.
- `config.json`: Model configuration.