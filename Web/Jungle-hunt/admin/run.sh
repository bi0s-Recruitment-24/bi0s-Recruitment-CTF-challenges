docker build -t jungle_hunt . && \
    clear && \
    echo "[+] BUILD SUCCESS" && \
    docker run -p 1337:1337 jungle_hunt