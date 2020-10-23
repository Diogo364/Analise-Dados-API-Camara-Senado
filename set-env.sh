#!/bin/bash

if [[ -d data ]]; then
  echo Data dir exists
else
  echo Creating data dir
  mkdir data
fi
