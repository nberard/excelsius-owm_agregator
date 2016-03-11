#!/bin/bash
if [ $(uname -m | grep arm) ]; then
    ARCH_PARAM="-arm"
else
    ARCH_PARAM=""
fi
docker build --rm -f Dockerfile${ARCH_PARAM} -t excelsius/owm_agregator${ARCH_PARAM}:latest .