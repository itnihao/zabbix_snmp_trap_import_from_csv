import zabbix_snmp_trap_import_from_csv
import merge_csv


path_to_files_cisco = './cisco_itp/'
file_to_create_cisco = 'merge_file_cisco.csv'
merge_csv.merge_csv(path_to_files_cisco, file_to_create_cisco)

# Creating XML tree as a String from CSV file.
xml_tree_gen_as_string = zabbix_snmp_trap_import_from_csv.zabbix_snmp_trap_import_from_csv(
    file_to_create_cisco, 'AMS-ITP1','AMS-ITP1', '10.106.0.18')

# Creating an XML file from xml_tree.
zabbix_snmp_trap_import_from_csv.xml_pretty_me('zabbix_import_alarms_cisco_itp_1.xml',xml_tree_gen_as_string)

# Creating XML tree as a String from CSV file.
xml_tree_gen_as_string = zabbix_snmp_trap_import_from_csv.zabbix_snmp_trap_import_from_csv(
    file_to_create_cisco, 'AMS-ITP2','AMS-ITP2', '10.106.0.19')

# Creating an XML file from xml_tree.
zabbix_snmp_trap_import_from_csv.xml_pretty_me('zabbix_import_alarms_cisco_itp_2.xml',xml_tree_gen_as_string)

path_to_files_ggsn = './cisco_itp/'
file_to_create_ggsn = 'merge_file_cisco.csv'
merge_csv.merge_csv(path_to_files_ggsn, file_to_create_ggsn)

# Creating XML tree as a String from CSV file.
xml_tree_gen_as_string = zabbix_snmp_trap_import_from_csv.zabbix_snmp_trap_import_from_csv(
    file_to_create_ggsn, 'AMS-GGSN', 'AMS-GGSN', '185.39.54.65')

# Creating an XML file from xml_tree.
zabbix_snmp_trap_import_from_csv.xml_pretty_me('zabbix_import_alarms_ams_ggsn.xml',xml_tree_gen_as_string)

# Creating XML tree as a String from CSV file.
xml_tree_gen_as_string = zabbix_snmp_trap_import_from_csv.zabbix_snmp_trap_import_from_csv(
    file_to_create_ggsn, 'BRU-GGSN', 'BRU-GGSN', '185.39.52.65')

# Creating an XML file from xml_tree.
zabbix_snmp_trap_import_from_csv.xml_pretty_me('zabbix_import_alarms_bru_ggsn.xml',xml_tree_gen_as_string)

