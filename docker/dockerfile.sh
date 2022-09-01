#!/bin/bash

passwd=$1
A=($(echo $passwd | awk '{ gsub(" ", "\n", $0); print }' | awk '{ split($0, arr, ":"); if( arr[3]>=1000 &&  arr[3]<65534 ) printf("%s %s %s\n", arr[1], arr[3], arr[4]) }'))
k=0
B=()

for el in "${A[@]}"
do

 B+=($el)
 k=$(expr $k + 1)

 if [ ${k} = 3 ]
 then
 
  adduser --uid ${B[1]} --disabled-password --gecos '' ${B[0]} && adduser ${B[0]} sudo && echo "${B[0]} ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers ;
  k=0
  B=()

 fi

done