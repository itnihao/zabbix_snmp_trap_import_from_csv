---
README -- Module used to generate Zabbix import xml for snmp traps
---

This Script expect MIB information to be in CSV format.
Export from a iReasoning Browser will generate CSV as below.

"Name","Full Name","OID","Type","Access","Indexes","MIB Module","Description"

We use this information to create snmptrap items and corresponding Trigger in the XML.
Which can be imported directly.

 --------------------------------------------
                    USAGE
 --------------------------------------------

 1. To Generate xml import file.
 --------------------------------------------
 python zabbix_snmp_trap_import_from_csv.py <export_csv> <host_name> <host_group_name> <host_interface_name>
    example: python zabbix_snmp_trap_import_from_csv.py export_csv_from_ireasoning_mib_browser.csv GGSN-1-LONDON GGSN-GROUP 127.0.0.1

 Parameter Information
 --------------------------------------------
 <export_csv>           : Is the XML KPI file for GGSN Device.
 <host_name>            : Host name as given in Zabbix server.
 <host_group_name>      : Host Group which the host belongs to, as in Zabbix server.
 <host_interface_ip>    : SNMP Interface configured on Zabbix server. (Assuming Single Interface in Configured)
 --------------------------------------------
