FROM python:latest

RUN  apt-get update
RUN  apt-get install wget
RUN  wget -O company_0.txt https://raw.githubusercontent.com/mschermann/forensic_accounting/master/fb_sub.csv
RUN  grep -E -o '([a-zA-Z]+)\sINC' company_0.txt > company.txt
RUN  rm company_0.txt