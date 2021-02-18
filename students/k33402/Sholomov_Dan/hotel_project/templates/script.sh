#!/bin/bash

date="Дата: $(date '+%F %T')"
user="Пользователь: $USER"
host_name="Имя хоста: $(uname -n)"
kernel="Ядро: $(uname -sr)"
os_name="ОС $(grep -E '^NAME=.*$' /etc/os-release)"
os_name=${os_name//"\""/""}
os_name=${os_name/"="/": "}
os_version="ОС: $(grep -E '^VERSION=.*$' /etc/os-release)"
os_version=${os_version//"\""/""}
os_version=${os_version/"="/": "}
proc_model="Процессор: $(lscpu | fgrep 'Model name:')"
proc_frequency="Частота процессора: $(lscpu | fgrep 'CPU MHz:э')"
mem_total="Объем памяти: $(head -n 1 /proc/meminfo)"
bb_name="Имя матплаты: $(dmidecode -s baseboard-product-name)"
bios_version="Версия BIOS: $(dmidecode -s bios-version)"
bios_release="Дата релиза BIOS: $(dmidecode -s bios-release-date)"

result="$date\n$user\n$host_name\n$kernel\n$os_name\n$os_version\n$proc_model\n$proc_frequency\n$mem_total\n$bb_name\n$bios_version\n$bios_release"

if [ -z $1 ]; then
  echo -e $result
  echo "PCI:"
  lspci
else
  echo -e $result > $1
  echo "PCI:" >> $1
  lspci >> $1
fi

exit 0