FROM grafana/grafana
USER root
COPY certificates/client/client.crt /etc/grafana/cert/
COPY certificates/client/client.key /etc/grafana/cert/
WORKDIR /etc/grafana/cert
RUN ls
ENV GF_INSTALL_PLUGINS=snuids-trafficlights-panel,briangann-gauge-panel,grafana-clock-panel,flant-statusmap-panel,natel-discrete-panel,yesoreyeram-boomtheme-panel
ENV GF_SERVER_PROTOCOL=https
ENV GF_SERVER_CERT_FILE=/etc/grafana/cert/client.crt
ENV GF_SERVER_CERT_KEY=/etc/grafana/cert/client.key
