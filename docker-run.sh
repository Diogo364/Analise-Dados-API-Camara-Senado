#!/bin/bash

docker run --rm -it \
-p 8501:8501 \
--name parlamentares \
-v $( pwd ):/app \
streamlit-parlamentares:latest
# --entrypoint "/bin/bash" \