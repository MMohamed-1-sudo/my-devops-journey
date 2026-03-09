#!/bin/bash

echo "first number: "
read a
echo "operator : ( + * - / )"
read op
echo "second number: "
read b 
 
 if [ "$op" = "-" ]; then 
  echo "$(( a - b ))"
 elif [ "$op" = "+" ]; then
  echo "$((a + b))"
 elif [ "$op" = "*" ]; then
  echo "$((a * b))"
 elif [ "$op" = "/" ]; then
  echo "$((a / b))"
 fi
