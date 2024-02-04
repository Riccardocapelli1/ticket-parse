docker run -it --rm --name deb-tic -v C:/Projects/gitlab/ticket:/py debian

apt-get update && apt-get -y upgrade && apt-get -y install git && apt-get -y install make && apt -y install tesseract-ocr && apt -y install imagemagick && apt -y install python3 && apt -y install python3-pip -y && apt -y install python3-pandas 

tesseract "./img/2-lidl.jpg" "./text/2-lidl-text" 

