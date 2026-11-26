#!/usr/bin/env bash
set -euo pipefail

user="${GITHUB_USER:-Piyush-r-bhaskar}"
readme="${1:-README.md}"

shipped=$(gh api -X GET search/issues \
    -f q="is:pr is:merged is:public author:${user} org:kestra-io" \
    -f sort=created -f order=desc -f per_page=100 \
    --jq '.items[] | select(.title | test("^feat")) | [.title, .html_url, .closed_at[0:10]] | @tsv' \
    | awk -F'\t' '!seen[$1]++' \
    | head -n 6 \
    | while IFS=$'\t' read -r title url date; do
        scope=$(sed -nE 's/^feat\(([^)]+)\).*/\1/p' <<<"$title")
        text=$(sed -E 's/^feat(\([^)]*\))?:[[:space:]]*//' <<<"$title")
        text="$(tr '[:lower:]' '[:upper:]' <<<"${text:0:1}")${text:1}"
        printf '| `%s` | [%s](%s) | %s |\n' "${scope:-core}" "$text" "$url" "$(date -d "$date" '+%b %-d' 2>/dev/null || date -j -f %F "$date" '+%b %-d')"
    done)

SHIPPED="$shipped" awk '
    /<!-- SHIPPED:START -->/ { print; print "| Area | Shipped | Merged |\n|:--|:--|--:|\n" ENVIRON["SHIPPED"]; skip = 1; next }
    /<!-- SHIPPED:END -->/ { skip = 0 }
    !skip
' "$readme" > "$readme.tmp" && mv "$readme.tmp" "$readme"
