#!/bin/bash
ARM_ARCH=${1:-}
docker build --rm -t -f Dockerfile${ARM_ARCH} excelsius/owm_agregator${ARM_ARCH}:latest .