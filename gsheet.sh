#!/bin/bash

[[ ! -n "$1" ]] && {
  echo "Usage: "
  echo "       "
  echo "  gspreadsheet <export|import> <spreadsheetname> <sheetgid> <type>"
  echo ""
  echo "  type can be 'xls' 'csv' 'pdf' 'ods' 'tsv' 'ods' or 'html'"
  echo ""
  echo "import takes tabseperated (tsv) as input, not spaceseparated (ssv)"
  echo ""
  echo "Example:"
  echo "  user=my@email.com pass=googlepasswd gspreadsheet export 'My spreadsheet' 12323";
  echo "  echo \"foo\\tflop\" | user=my@email.com pass=googlepasswd gspreadsheet import 'My spreadsheet' 12323"
  echo "  echo '\"foo\",\"bar\"' | user=my@email.com pass=googlepasswd gspreadsheet import 'My spreadsheet' 12323 csv"
  echo "  ls -al | gspreadsheet ssvtotsv | user=my@email.com pass=googlepasswd gspreadsheet import 'My spreadsheet' 12323 csv"
  exit 0
}

spreadsheetname="$2"
sheet="$3"
token="(no token)"
[[ -n "$4" ]] && type="$4" || type="tsv"

# gets the authentication token from google
gettoken(){
  curl -L --silent https://www.google.com/accounts/ClientLogin -d Email="$1" -d Passwd="$2" -d accountType=GOOGLE  -d source=cURL-Example -d service="$3"
}

prettyxml(){
  cat - | sed ':a;N;$!ba;s/\n/ /g' | sed 's/</\n&/g;s/  / /g' | sed '/^\s*$/d'
}

export(){
  token="$(gettoken "$user" "$pass" "wise")"
  curl -L --silent --header "Authorization: GoogleLogin auth=$token" "http://spreadsheets.google.com/feeds/download/spreadsheets/Export?key=$1&exportFormat=$type&gid=$2"
  echo ""
}

list(){
  curl -L --silent --header "Authorization: GoogleLogin auth=$1" "https://docs.google.com/feeds/documents/private/full?title=$2&title-exact=true" 2>&1 | prettyxml
}

tsvtocsv(){
  cat - | awk -F '\t' '{ for(i = 1; i <= NF; i++) { gsub(/"/,"\"\"\"",$i); printf "\"%s\"",$i; if( i < NF ) printf "," }; printf "\n" }'
}

csvtotsv(){
  cat - | awk '{$1=$1;gsub(/"/,"")}1' FPAT='([^,]+)|(\"[^\"]+\")' OFS='\t'
}

ssvtotsv(){
  cat - | awk '{ for(i = 1; i <= NF; i++) { printf "%s",$i; if( i < NF ) printf "\t" }; printf "\n" }'
}

import(){
  token="$(gettoken "$user" "$pass" "writely" | grep Auth | cut -d\= -f2)"
  [[ "$type" == "csv" ]] && data="$(cat -)" || data="$(cat - | tsvtocsv )"
  echo "$data" | curl -L --silent --request PUT --header "Authorization: GoogleLogin auth=$token" --header "Slug: $spreadsheetname" --header "If-Match: *" --header "Content-Type: text/csv" --data-binary @- "https://docs.google.com/feeds/default/media/spreadsheet%3A$1?v=3#gid=$2"
}

getid(){
  token="$(gettoken "$user" "$pass" "writely" | grep Auth | cut -d\= -f2)"
  config="$(list "$token" "$1")"
  echo "$config" | grep "<gd:resourceId>spreadsheet:" | sed 's/.*spreadsheet://g'
}

case "$1" in 
  *to*) "$@"
        ;;
  *)    $1 "$(getid "$spreadsheetname")" "$sheet" "$type"
        ;;
esac

