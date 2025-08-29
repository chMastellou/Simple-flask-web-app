#!/bin/bash

cd /opt/website
/usr/bin/docker compose up -d
cd /opt/mailcow
/usr/bin/docker compose up -d

exit 0
