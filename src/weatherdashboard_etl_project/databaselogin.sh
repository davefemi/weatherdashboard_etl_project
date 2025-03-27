#!/bin/bash
# Copyright David Ojo (2024)

echo "Hello, you are logging on to database 'Informatica'. Today is "  `date`
SERVER="aws-0-eu-central-1.pooler.supabase.com"
DATABASE="postgres"
PORT="6543"
USERNAME="postgres.hmewojubqiwirdnxklhc"


"/Library/PostgreSQL/17/bin/psql" -h $SERVER -p $PORT -U $USERNAME $DATABASE
RET=$?

if [ "$RET" != "0" ];
then
    echo
    echo -n "Press <return> to continue..."
    read dummy
fi

exit $RET