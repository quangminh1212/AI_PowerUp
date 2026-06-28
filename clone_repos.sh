#!/usr/bin/env bash
# Clone all repos from repos.json (shallow, single branch)
set -euo pipefail
jq -r '.[] | "\(.path) \(.url)"' repos.json | while read -r path url; do
  if [[ -d "$path" ]]; then
    echo "SKIP $path"
    continue
  fi
  mkdir -p "$(dirname "$path")"
  echo "CLONE $url -> $path"
  git clone --depth 1 --single-branch "$url" "$path" || true
done
echo "Done."