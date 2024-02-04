FROM debian:bullseye-slim as build

RUN apt-get update && apt-get -y upgrade 
RUN apt-get -y install git 
RUN apt -y install tesseract-ocr 
RUN apt -y install python3 
RUN apt -y install python3-pip -y 
RUN apt -y install python3-pandas 
RUN apt -y install python3-pillow 
RUN apt -y install python3-pil
RUN apt-get install -y tesseract-ocr 
RUN apt-get install -y tesseract-ocr-spa 
RUN apt-get install -y tesseract-ocr-ita

RUN pip install -U git+https://github.com/madmaze/pytesseract.git
RUN pip install tox
RUN tox

WORKDIR /py
