#! /bin/sh
if [ $1 ]; then
	curl -sI $* | grep "Location: " | cut -d " " -f 2
fi