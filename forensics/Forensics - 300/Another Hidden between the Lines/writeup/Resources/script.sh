#!/bin/bash

file_name="hidden"
binary_flag=""

while IFS= read -r line; do
    if [[ "$line" == *"^M$" ]]; then
        binary_flag+="1"
    elif [[ "$line" == *"$" ]]; then
        binary_flag+="0"
    fi
done < <(cat -A "$file_name")

if [ -n "$binary_flag" ]; then
    ascii_flag=""
    for ((i=0; i<${#binary_flag}; i+=8)); do
        byte=${binary_flag:$i:8}
        ascii_flag+=$(echo "$((2#$byte))" | awk '{printf("%c", $1)}')
    done
    echo "Decrypted flag: $ascii_flag"
else
    echo "No flag found or incorrect input."
fi
