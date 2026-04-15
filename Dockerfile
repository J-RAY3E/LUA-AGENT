# 1. Base Image: Python 3.10 Slim 
FROM python:3.10-slim

# 2. Install Dependencies System 
RUN apt-get update && apt-get install -y \
    curl \
    ca-certificates \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# 3. Install Ollama
RUN curl -fsSL https://ollama.com/install.sh | sh

# 4. Setup Working Directory
WORKDIR /app

# 5. Copy requirements.txt and Install Dependency Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copy Code Aplication to Container
COPY src/ ./src/
COPY agents/ ./agents/
COPY wiki/ ./wiki/
COPY config/ ./config/

# --- SETUP MODEL OTOMATIS  ---

# make folder to save GGUF model
RUN mkdir -p /app/models

# Download Model Qwen2.5-Coder-7B-Instruct (Quantization Q4_K_M)
RUN curl -L -o /app/models/qwen2.5-coder-7b-instruct-q4_k_m.gguf \
    "https://huggingface.co/Qwen/Qwen2.5-Coder-7B-Instruct-GGUF/resolve/main/qwen2.5-coder-7b-instruct-q4_k_m.gguf?download=true"

#Make dynamic Modelfile for Ollama
RUN echo "FROM /app/models/qwen2.5-coder-7b-instruct-q4_k_m.gguf" > /app/Modelfile
RUN echo "PARAMETER num_ctx 4096" >> /app/Modelfile
RUN echo "PARAMETER num_predict 256" >> /app/Modelfile
RUN echo "PARAMETER temperature 0.2" >> /app/Modelfile
RUN echo "PARAMETER num_gpu 999" >> /app/Modelfile


RUN ollama create qwen-lua-agent -f /app/Modelfile


COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Expose Port Ollama (Internal)
EXPOSE 11434

ENTRYPOINT ["/entrypoint.sh"]