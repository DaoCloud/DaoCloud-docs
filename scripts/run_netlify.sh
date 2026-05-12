#!/bin/bash

set -euo pipefail

make sync
make build all
