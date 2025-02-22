from delfer/alpine-ftp-server:latest
RUN echo 'pasv_promiscuous=YES' >> /etc/vsftpd/vsftpd.conf
EXPOSE 20 21
EXPOSE 30000-30002
ENTRYPOINT ["start_vsftpd.sh"]