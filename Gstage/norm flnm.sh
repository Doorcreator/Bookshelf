#!/bin/bash
# Replace special characters in a filename with spaces to normalize it.
# . norm_flnm.sh
# spec_char='–—"#$%&\+,-/:;<=>?@[].\`|}~^!{)(* '
spec_char='–—_"#$%&\+,-/:;<=>?@\`|}~^!{)(* '
function norm_flnm {
    local path="$1"
    for ((i=0;i<${#path};i++));do
        tmp="${path:i:1}"
        if [[ "$spec_char" =~ "$tmp" ]];then
        # if special characters in the spec_char set are found in a filename, they shall be substituted with whitespaces
            path=${path//"$tmp"/ }
        fi
    done
    # an open bracket is substituted with an underline sign, and a closing bracket is deleted
    path=$(echo "$path" | sed "{s/'/”/g;s/ \?\[/_/g;s/\]//g;s/ \+/ /g;s/^_//}")
    # return the substituted result
    echo "$path"
}
