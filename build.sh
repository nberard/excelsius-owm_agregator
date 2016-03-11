#!/bin/bash
ARM_ARCH=${1:-}
docker build --rm -f Dockerfile${ARM_ARCH} -t excelsius/owm_agregator${ARM_ARCH}:latest .