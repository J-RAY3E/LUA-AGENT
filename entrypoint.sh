#!/bin/bash

echo "Starting Ollama server..."
ollama serve &

echo "Waiting for Ollama to be ready..."
for i in {1..60}; do
    if curl -s http://localhost:11434/api/tags > /dev/null; then
        echo "Ollama is ready!"
        break
    fi
    sleep 1
done

export OLLAMA_NUM_PARALLEL=1

echo "Starting Lua Agent Application..."
python src/main.py