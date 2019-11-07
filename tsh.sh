#!/bin/bash
# source the script <norm_flnm.sh>
. /g/cs/backup2git/norm_flnm.sh
# Link a file (with its full path) to a destination folder (with its full path)
# format: lnkf <file> <des_folder>
COUNT_LNK=0
function lnkf {
    src_path=$1
    des_folder=$2
    if [ -f "$src_path" ] && [[ "$src_path" =~ .*/.* ]];then
        # extract filename from its full path
        src_file=${src_path##*/}
    else
        echo "Please verify that the source file exits and you are using a full path to the file."
        return
    fi
    if [ ! -d "$des_folder" ];then
        mkdir "$des_folder"
    fi
    if [ ! -f "$des_folder/$src_file" ];then
        ln "$src_path" "$des_folder"
        COUNT_LNK=$[ $COUNT_LNK+1 ]
    else
        echo "Oops!$des_folder has already included $src_file,link not successfully made."
    fi
}
# Compress a file using xz
# format: cmprf <file>
COUNT_CMPR=0

function cmprf {
    filename=$1
    
    # only compress a file with a valid name and without a compressed version in the same directory
    if [ -f "$filename" ] && [ ! -f "$filename.xz" ];then
        fmsize=$(echo $(du -h "$filename") | awk '{print $1}')
        
        echo compressing "$filename" $fmsize ...
        xz -9kqQf "$filename"
    fi
}
# Back up a local folder to a git repo.
# format: bkup_fld <src_folder> <des_folder>
# <src_folder> is a local folder to be backed up. <des_folder> is a local folder within a local git repository and will be created if it does not exist.
# The script is intended to be run by a bash program (either git bash or Linux bash).
function bkup_fld {
    src_folder=$1
    des_folder=$2
    IFS=$'\n'
    for f in $(ls $src_folder);do
        src_path="$src_folder/$f"
        lnkf "$src_path" "$des_folder"
        # remove weird characters in file path and rename the file
        newf=$(norm_flnm "$f")
        mv "$des_folder"/"$f" "$des_folder"/"$newf"
        # only files with a size greater than 1 MB shall be compressed
        ## file size in bytes
        fbsize=$(stat -c %s "$des_folder"/"$newf")
        ## file size in Mbytes
        # fmsize=$(awk -v a=$fbsize 'BEGIN{printf "%.2f", a/1024/1024}')
        
        if [ "$fbsize" -gt 1048576 ];then
            cmprf "$des_folder"/"$newf"
            # delete a successfully compressed file
            if [ -f "$des_folder"/"$newf".xz ];then
                COUNT_CMPR=$[ $COUNT_CMPR+1 ]
                rm -f "$des_folder"/"$newf"
            fi
        fi
    done
    echo $COUNT_LNK links made and $COUNT_CMPR files compressed successfully.
    declare -A FSIZE
    for f in $(ls $des_folder);do
        fmsize=$(echo $(du -h "$des_folder"/"$f") | awk '{print $1}')
        git add "$des_folder"/"$f"
        git commit -m "${fmsize}bytes"
    done
    git add -A
    git push bksf master
        # if [ $? -eq 0 ];then rm -f "$des_folder"/"$f";fi
}

bkup_fld /g/cs/batpush /g/cs/backup2git/batpush

