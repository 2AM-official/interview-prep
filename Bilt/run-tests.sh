#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"

if ! command -v javac >/dev/null 2>&1; then
  echo "No JDK found. Install one, then re-run this script:"
  echo "  brew install openjdk@17"
  echo "  echo 'export PATH=\"/opt/homebrew/opt/openjdk@17/bin:\$PATH\"' >> ~/.zshrc"
  echo "  source ~/.zshrc"
  exit 1
fi

mkdir -p out
javac -d out src/main/java/bilt/RewardsService.java src/test/java/bilt/RewardsServiceTest.java
java -cp out bilt.RewardsServiceTest
