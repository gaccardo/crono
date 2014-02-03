#!/bin/bash

STATUS=0

if [ ! -d "configuration/" ];
then
	echo "Configuration directory does not exists"
	exit -1
fi

if [ ! -f "configuration/global.fw" ];
then
	echo "Global configuration file does not exists"
	exit -1
else
	source configuration/global.fw
fi

function start
{
	ERROR=0
	STATUS=0

	if [ ! -f "configuration/filter.fw" ];
	then
		echo "Filter table configuration file does not exists"
		let "ERROR++"
	fi

	if [ ! -f "configuration/nat.fw" ];
	then
		echo "NAT table configuration file does not exists"
		let "ERROR++"
	fi

	if [ ! -f "configuration/mangle.fw" ];
	then
		echo "Mangle table configuration file does not exists"
		let "ERROR++"
	fi

	if [ ! -f "configuration/routes.rt" ];
	then
		echo "Routes configuration file does not exists"
		let "ERROR++"
	fi

	if [ "$ERROR" -gt 0 ];
	then
		exit -1
	else
		echo -n "Starting firewall: "
		source configuration/filter.fw
		source configuration/nat.fw
		source configuration/mangle.fw
		source configuration/routes.rt
	fi

	if [ "$IP_FORWARD" -eq "1" ];
	then
		#echo "1" > /proc/sys/net/ipv4/ip_forward
		echo -n "."
	fi

	echo " [ OK ]"
}

function stop
{
	STATUS=1
	ERROR=0

	if [ ! -f "configuration/filter.fw" ];
	then
		echo "Filter table configuration file does not exists"
		let "ERROR++"
	fi

	if [ ! -f "configuration/nat.fw" ];
	then
		echo "NAT table configuration file does not exists"
		let "ERROR++"
	fi

	if [ ! -f "configuration/mangle.fw" ];
	then
		echo "Mangle table configuration file does not exists"
		let "ERROR++"
	fi

	if [ ! -f "configuration/routes.rt" ];
	then
		echo "Routes configuration file does not exists"
		let "ERROR++"
	fi

	if [ "$ERROR" -gt 0 ];
	then
		exit -1
	else
		echo -n "Stoping firewall: "
		source configuration/filter.fw
		source configuration/nat.fw
		source configuration/mangle.fw
		source configuration/routes.rt
	fi

	if [ "$IP_FORWARD" -eq "1" ];
	then
		#echo "0" > /proc/sys/net/ipv4/ip_forward
		echo -n "."
	fi

	echo " [ OK ]"
}

function help
{
	echo "help"
}

case $1 in

	start)
		start
	;;

	stop)
		stop
	;;

	restart)

	;;

	*)

	;;

esac