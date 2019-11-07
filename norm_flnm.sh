#!/bin/bash
# Normalize a filename by substituting special characters with spaces.
# spec_char_set='–—"#$%&\+,-/:;<=>?@[].\`|}~^!{)(* '
# Single quote is not included in the set due to its special use as delimiter in shell, but it can be individually substituted as well.
spec_char='–—_"#$%&\+,-/:;<=>?@\`|}~^!{)(* '
function norm_flnm {
    local path="$1"
    for ((i=0;i<${#path};i++));do
        char="${path:i:1}"
        if [[ "$spec_char" =~ "$char" ]];then
        # If special characters in the spec_char set are found in a filename, they shall be substituted with whitespaces.
            path=${path//"$char"/ }
        fi
    done
    # An open bracket is substituted with an underline sign, and a closing bracket is deleted. Single quotes are substituted with Chinese quotation marks. A leading underline sign is deleted.
    path=$(echo "$path" | sed "{s/'/”/g;s/ \?\[/_/g;s/\]//g;s/ \+/ /g;s/^_//}")
    # return the substituted result
    echo "$path"
}
