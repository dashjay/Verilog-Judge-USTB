#!  /bin/bash

#Get the info of variables
function getVarInfo(){
    for i in $(cat $1 | grep 'input' -o)
    do
        var_number=$(($var_number+1))
    done
    for out in $(cat $1 | grep 'output' -o)
    do
        var_number=$(($var_number+1))
    done
    return $var_number
}

#Jsonfy the serialize data
function jsonfy(){
    var_name=$2
    flag=$(($1+2))
    for ((i=3;i<3+$1;i++))
    do
        data='data:'`jq  -R -c -M -s 'split(" ")' <  temp$i`
        tmp=$tmp`echo "{name:"'"'${var_name[$i-3]}'"'",wave:"'"'$(str=$(printf "%-10s" "=");echo "${str// /=}")'"',$data"}"`
        if [[ $i < $flag ]]
        then
            tmp=$tmp','
        fi
    done

    result=`echo "{signal:[$tmp]}"` 
    result=`jq -n -c -M $(echo $result)`
    echo $result > signal.json
    echo $result
}

#Serialize the simulition 
function serialize(){
    getVarInfo $1
    var_number=$?
    var_name=(`cat var_name`)
    for ((i=3;i<3+$var_number;i++))
    do
        array=$(awk -F " " "{print "$`echo -n $i`"}" sim.lst)
        echo -n $array > "temp$i"
    done

    jsonfy  $var_number "${var_name[@]}"
}

function main(){
    serialize "$1.v"
    rm temp*
} 

top_module=$1
main $1
