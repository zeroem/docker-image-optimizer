FROM centos:7

COPY docker-image-optimizer.py /usr/lib/yum-plugins/
COPY docker-image-optimizer.conf /etc/yum/pluginconf.d/

