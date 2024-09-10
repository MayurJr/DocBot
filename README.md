PDF Chatbot using Generative AI

This project presents the development of a PDF chatbot utilizing Google's GEMMA 2B-IT, an open-source large language model, enhanced with Retrieval-Augmented Generation (RAG) techniques. The implementation involves setting up the environment, integrating the language model with retrieval systems, developing a user-friendly web interface, and ensuring seamless interaction between the user and the chatbot. This approach enables the chatbot to provide accurate, contextually relevant responses to user queries based on PDF documents, showcasing the combined power of advanced NLP techniques and efficient data handling. The result is a robust and interactive PDF chatbot capable of enhancing user engagement and information accessibility.

Running the project:
1. To use certain LLM models like Gemma, you need to create a .env file containing the line “ACCESS_TOKEN=<your hugging face token>”.
2. You can create your own token in the HuggingFace website and then request access to the various LLM models on the website.
3. Install the required libraries with “pip install -r requirements.txt”
4. Run the project by typing “streamlit run src/app.py” in the terminal.

**Using quantization requires a GPU**
To use bitsandbytes quantization, a Nvidia GPU is required. Make sure to install the NVIDIA Toolkit first and then PyTorch.

You can check if your GPU is available in Python with

import torch
print(torch.cuda.is_available())

If you do not have a compatible GPU, try setting device="cpu" for the model and remove the quantization config.
