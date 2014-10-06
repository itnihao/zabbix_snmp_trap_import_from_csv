README
===============
Module used to generate Zabbix import xml for snmp traps


Step 1:
--------------------------------------------
    Select the Alarms from the iReasoning MIB browser and Export them as CSV.
    
    This Script expect MIB information to be in CSV format.
    Export from a iReasoning Browser will generate CSV as below.
    
    "Name","Full Name","OID","Type","Access","Indexes","MIB Module","Description"
    
    We use this information to create snmptrap items and corresponding Trigger in the XML.
    Which can be imported directly.


Step 2: To Generate xml import file.
--------------------------------------------
    python zabbix_snmp_trap_import_from_csv.py <export_csv> <host_name> <host_group_name> <host_interface_name>
    
    example: python zabbix_snmp_trap_import_from_csv.py -e export_csv_from_ireasoning_mib_browser.csv -n GGSN-1-LONDON -g GGSN-GROUP -i 127.0.0.1
    
    usage: zabbix_snmp_trap_import_from_csv.py [-h] -e EXPORT_CSV -n HOST_NAME -g
                                               HOST_GROUP -i HOST_INTERFACE
    
    Select the Alarms from the iReasoning MIB browser and Export them as CSV. This
    Script expect MIB information to be in CSV format. Export from a iReasoning
    Browser will generate CSV as below. "Name","Full
    Name","OID","Type","Access","Indexes","MIB Module","Description" We use this
    information to create snmptrap items and corresponding Trigger in the XML.
    Which can be imported directly.
    
    optional arguments:
      -h, --help            show this help message and exit
      -e EXPORT_CSV, --export-csv EXPORT_CSV
                            OID file, Gives all OIDs on the device
      -n HOST_NAME, --host-name HOST_NAME
                            Host name as given in Zabbix server.
      -g HOST_GROUP, --host-group HOST_GROUP
                            Host Group which the host belongs to, as in Zabbix
                            server.
      -i HOST_INTERFACE, --host-interface HOST_INTERFACE
                            SNMP Interface configured on Zabbix server. (Assuming
                            Single Interface in Configured)


USAGE in CODE.
--------------------------------------------

```python
import zabbix_snmp_trap_import_from_csv

# Creating XML tree as a String from CSV file.
xml_tree_gen_as_string = zabbix_snmp_trap_import_from_csv.zabbix_snmp_trap_import_from_csv(
    'export_csv_from_ireasoning_mib_browser.csv','GGSN','GGSN-GROUP','127.0.0.1')

# Creating an XML file from xml_tree.
zabbix_snmp_trap_import_from_csv.xml_pretty_me('zabbix_import_file.xml',xml_tree_gen_as_string)
```