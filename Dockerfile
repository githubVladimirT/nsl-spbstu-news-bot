FROM ubuntu:20.04

#RUN echo nameserver 8.8.8.8 >> /etc/resolv.conf ;
RUN apt-get update && apt install software-properties-common -y && add-apt-repository ppa:deadsnakes/ppa && apt-get update && apt -y install make python3.11 python3-pip python3.11-distutils python3-distutils-extra curl


WORKDIR /home/nsl-spbstu-news-bot

ADD . /home/nsl-spbstu-news-bot

#RUN python3.11 -m pip install --upgrade pip
RUN curl -sS https://bootstrap.pypa.io/get-pip.py | python3.11

RUN python3.11 -m pip install -r ./requirements.txt

CMD ["./main.py"]
ENTRYPOINT ["/usr/bin/python3.11"]
