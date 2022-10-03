FROM python:3.10.7
USER root
EXPOSE 8888

RUN pip install jupyter
RUN apt-get install wget
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

ENV JUPYTER_USER rongyulin

RUN useradd -ms /bin/bash ${JUPYTER_USER}

USER ${JUPYTER_USER}


RUN mkdir -p /home/rongyulin/notebooks
RUN wget -P /home/rongyulin/notebooks https://raw.githubusercontent.com/mschermann/forensic_accounting/master/Introduction.ipynb

EXPOSE 8888
CMD jupyter notebook --ip=0.0.0.0 --port 8888 