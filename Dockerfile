From centos:latest

MAINTAINER root

WORKDIR .
COPY ./core /root/core

RUN buildDeps='glibc.i686 libX11.i686 libXext-devel.i686 libXft-devel.i686 libncurses.so.5 ' \
    && preSetup='vim unzip make python36 python36-pip' \
    && yum update -y \
    && yum install -y wget \
    && wget http://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm \
    && rpm -ivh epel-release-latest-7.noarch.rpm \
    && yum repolist -y \
    && yum install jq -y \
    && yum install -y $buildDeps \
    && yum install -y $preSetup \
    && pip3 install flask \
    && echo "export PATH="'$PATH'":/root/modelsim_ase/linuxaloem" >> /root/.bashrc \
    && rm epel-release-latest-7.noarch.rpm \
    && chmod +x /root/core/*.sh

CMD ["tail", "-f", "/dev/null"]
