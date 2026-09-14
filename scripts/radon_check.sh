#!/bin/bash

# Define thresholds for complexity and maintainability.
#
# Complexity:
#   A = 1-5
#   B = 6-10
#   C = 11-20
#   D = 21-30
#   E = 31-40
#   F = 41+
#
# Maintainability Index:
#   A = 20-100
#   B = 10-19
#   C = 0-9

COMPLEXITY_SCORE="A"
MAINTAINABILITY_THRESHOLD="B"
EXCLUDE="venv/*"
DIRECTORY="./."

# Calculate average cyclomatic complexity.
average_complexity=$(
    radon cc -a -e "$EXCLUDE" "$DIRECTORY" |
        grep -oP '(?<=Average complexity: )\S+'
)

# Check average complexity.
if [ "$average_complexity" != "$COMPLEXITY_SCORE" ]; then
    echo "Average complexity ($average_complexity) is higher than allowed threshold ($COMPLEXITY_SCORE)"

    radon cc -s -n "$COMPLEXITY_SCORE" -e "$EXCLUDE" "$DIRECTORY"

    exit 1
else
    echo "Average complexity ($average_complexity) is within allowed threshold ($COMPLEXITY_SCORE)"
fi

# Find files with a maintainability grade below the allowed threshold.
#
# Radon's `mi -s` output looks like: "path - GRADE (score)"
# so the grade is the second-to-last whitespace-separated field.
# We specifically look for C-grade files, because A and B are allowed.
maintainability_issues=$(
    radon mi -s -e "$EXCLUDE" "$DIRECTORY" |
        awk '$(NF-1) == "C" {print}'
)

# Check maintainability.
if [ -n "$maintainability_issues" ]; then
    echo "Maintainability index is below allowed threshold ($MAINTAINABILITY_THRESHOLD) for the following files:"
    echo "$maintainability_issues"

    exit 1
else
    echo "Maintainability index is within allowed threshold ($MAINTAINABILITY_THRESHOLD)"
fi

exit 0
