#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"

if ! command -v javac >/dev/null 2>&1; then
  echo "No JDK found. Install Java 17 and put javac on PATH."
  exit 1
fi

mkdir -p out
javac -d out \
  src/main/java/bilt/part1/*.java \
  src/test/java/bilt/part1/InterviewTest.java
java -cp "out:src/main/resources" bilt.part1.InterviewTest
