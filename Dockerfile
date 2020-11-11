FROM ubuntu:16.04

RUN if [ $(command -v apt-get) ]; then apt-get update && apt-get install -y python sudo bash ca-certificates && apt-get clean;
