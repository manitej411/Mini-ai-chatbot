# Mini-ai-chatbot
1. User enters a message in the web interface
2.  Frontend sends a POST request to the Flask backend
3. Backend forwards the prompt to the LLaMA 3 model via Ollama
4.  The model processes the input using Transformer components (attention, embeddings, etc.)
5.  Generated response is sent back to the frontend and displayed
Note: The chatbot leverages a pretrained Transformer-based LLM (LLaMA 3). 
Core NLP operations such as tokenization, embeddings, attention mechanisms, 
and response generation are handled internally by the model.
