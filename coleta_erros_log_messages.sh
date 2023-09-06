#!/bin/bash

# Script: coleta_erros_log_messages.sh
# Desenvolvido por: Robson Berthelsen
# Data: 24/08/2023
# Versão: 1

# Descrição: Este script coleta mensagens de erro no arquivo de log /var/log/messages
# e envia as mensagens para o Zabbix usando o utilitário zabbix_sender.

# Dependências: Necessário ter o pacote zabbix_sender instalado
# Trigger no zabbix - Expressão do incidente: length(last(/ESRVAIRFLOW01/message_log_errors,#1))>0
#                   - Expressão de recuperação: length(last(/ESRVAIRFLOW01/message_log_errors,#10))=0

# Configurações
log_file="/var/log/messages"
zabbix_server="10.150.25.56"  # Endereço IP do servidor Zabbix
hostname=$(hostname -s)        # Nome do host
zabbix_key="message_log_errors"  # Chave do item no Zabbix

# Padrões de erros a serem ignorados (separados por |)
# Exemplo: ignored_errors="pattern1|pattern2|pattern3"
ignored_errors="airflow: **kwargs: {'failed_states': 'failed'}"

# Coleta de erros no log
errors=$(tail -n 100 "$log_file" | grep -E -i "error|failed|miss" | grep -E -v "$ignored_errors")

if [ -n "$errors" ]; then
    while IFS= read -r line; do
        # Envia cada mensagem de erro para o Zabbix
        echo "$line" | zabbix_sender -z "$zabbix_server" -s "$hostname" -k "$zabbix_key" -o "$line"
    done <<< "$errors"
else
    # Se não houver erros, envia "null" para o Zabbix
    echo "" | zabbix_sender -z "$zabbix_server" -s "$hostname" -k "$zabbix_key" -o ""
fi
