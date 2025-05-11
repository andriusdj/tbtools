#!/bin/bash

WEEK=`date +%V`
WEEKDAY=`date +%a`
DATE=`date +%F`
DATETIME=`date +'%F_%H:%M:%S'`

FILENAME="LDK_$DATE.json"

if [[ ! -f $FILENAME ]]; then
	touch $FILENAME;
	echo "{}" > $FILENAME;
fi

echo "Recording chests ... "
./record-chests.py ./$FILENAME
echo "Done."
echo "----------------------------"
echo -e "Date\t$DATE"
echo -e "Week\t$WEEK"
echo -e "Day\t$WEEKDAY"
echo -e "Update\t$DATETIME"
./count-chests.py $FILENAME chest-values.json
echo "----------------------------"
