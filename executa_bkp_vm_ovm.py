# -*- coding: utf-8 -*-

import calendar
import datetime
import subprocess
import sys

first_friday_vm="ESRVMWMANAGER"    # Primeira sexta-feira
second_friday_vm="ESRVPOHS02"      # Segunda sexta-feira
third_friday_vm="ESRVPOHS03"       # Terceira sexta-feira
fourth_friday_vm="ESRVPOHS04"      # Quarta sexta-feira

first_saturday_vm="ESRVP12CSOA01"  # Primeiro sábado
second_saturday_vm="ESRVPSOAMF01"  # Segundo sábado
third_saturday_vm="ESRVPSOAMF02"   # Terceiro sábado

first_sunday_vm="ESRVPOHS01"       # Primeiro domingo
second_sunday_vm="ESRVP12CSOA02"   # Segundo domingo
third_sunday_vm="ESRVPSOA01"       # Terceiro domingo
fourth_sunday_vm="ESRVPSOA02"      # Quarto domingo
								 
# Get today's date
today = datetime.date.today()

# Get the month and year of today's date
month = today.month
year = today.year

# Get the day of the week for the first day of the month (0 = Monday, 6 = Sunday)
first_day_of_month = datetime.date(year, month, 1).weekday()

# Calculate the date of the first Friday of the month
if first_day_of_month <= 4:
    first_friday = datetime.date(year, month, 1) + datetime.timedelta(days=(4 - first_day_of_month))
else:
    first_friday = datetime.date(year, month, 1) + datetime.timedelta(days=(11 - first_day_of_month))

# Calculate the date of the first Saturday of the month
if first_day_of_month <= 5:
    first_saturday = datetime.date(year, month, 1) + datetime.timedelta(days=(5 - first_day_of_month))
else:
    first_saturday = datetime.date(year, month, 1) + datetime.timedelta(days=(12 - first_day_of_month))

# Calculate the date of the first Sunday of the month
if first_day_of_month <= 6:
    first_sunday = datetime.date(year, month, 1) + datetime.timedelta(days=(6 - first_day_of_month))
else:
    first_sunday = datetime.date(year, month, 1) + datetime.timedelta(days=(13 - first_day_of_month))

# Calculate the date of the first Monday of the month
#if first_day_of_month == 0:
#    first_monday = datetime.date(year, month, 1)
#else:
#    first_monday = datetime.date(year, month, 1) + datetime.timedelta(days=(7 - first_day_of_month))

# Calculate the dates of the second, third, and fourth Fridays, Saturdays, Sundays, and Mondays of the month
second_friday = first_friday + datetime.timedelta(days=7)
third_friday = second_friday + datetime.timedelta(days=7)
fourth_friday = third_friday + datetime.timedelta(days=7)
second_saturday = first_saturday + datetime.timedelta(days=7)
third_saturday = second_saturday + datetime.timedelta(days=7)
fourth_saturday = third_saturday + datetime.timedelta(days=7)
second_sunday = first_sunday + datetime.timedelta(days=7)
third_sunday = second_sunday + datetime.timedelta(days=7)
fourth_sunday = third_sunday + datetime.timedelta(days=7)
#second_monday = first_monday + datetime.timedelta(days=7)
#third_monday = second_monday + datetime.timedelta(days=7)
#fourth_monday = third_monday + datetime.timedelta(days=7)

# Funcao para executar o comando de backup e registrar no log
def execute_backup(vm):
    command = "/opt/ovm-bkp/bin/ovm-backup.sh " + vm + " OVA N"
    subprocess.call(command, shell=True)
#    log_message = "{}: Executado backup para {}".format(datetime.datetime.now(), vm)
#    with open("backup_log.txt", "a") as log_file:
#        log_file.write(log_message + "\n")

# Check if today is one of the days
if today == first_friday:
#    print("Today is the first Friday of the month.")
	execute_backup(first_friday_vm)
	
elif today == second_friday:
#    print("Today is the second Friday of the month.")
	execute_backup(second_friday_vm)
	
elif today == third_friday:
#    print("Today is the third Friday of the month.")
	execute_backup(third_friday_vm)
	
elif today == fourth_friday:
#    print("Today is the fourth Friday of the month.")
	execute_backup(fourth_friday_vm)
	
elif today == first_saturday:
#    print("Today is the first Saturday of the month.")
	execute_backup(first_saturday_vm)
	
elif today == second_saturday:
#    print("Today is the second Saturday of the month.")
	execute_backup(second_saturday_vm)
	
elif today == third_saturday:
#    print("Today is the third Saturday of the month.")
	execute_backup(third_saturday_vm)
	
elif today == fourth_saturday:
#    print("Today is the fourth Saturday of the month.")
	execute_backup(vm)
	
elif today == first_sunday:
#    print("Today is the first Sunday of the month.")
	execute_backup(first_sunday_vm)
	
elif today == second_sunday:
#    print("Today is the second Sunday of the month.")
	execute_backup(second_sunday_vm)
	
elif today == third_sunday:
#    print("Today is the third Sunday of the month.")
	execute_backup(third_sunday_vm)
	
elif today == fourth_sunday:
#    print("Today is the fourth Sunday of the month.")
	execute_backup(fourth_sunday_vm)
	
#elif today == first_monday:
#    print("Today is the first Monday of the month.")
#	execute_backup(vm)
#	
#elif today == second_monday:
#    print("Today is the second Monday of the month.")
#	execute_backup(vm)
#	
#elif today == third_monday:
#    print("Today is the third Monday of the month.")
#	execute_backup(vm)
#	
#elif today == fourth_monday:
#    print("Today is the fourth Monday of the month.")
#    execute_backup(vm)
	
else:
    sys.exit(0)
#    print("Today is not a special day.")
