docker build -t raptor_chat_extractor . && \
    clear && \
    echo "[+] BUILD SUCCESS" && \
    docker run -p 1337:80 raptor_chat_extractor