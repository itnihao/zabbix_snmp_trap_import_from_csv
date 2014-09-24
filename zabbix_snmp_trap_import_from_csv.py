#!/usr/bin/python

__author__ = 'ahmed'


import csv
import sys
from logging import exception
from xml.etree import ElementTree
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import SubElement
import datetime
import logging
from xml.dom import minidom

# --------------------------------------------------------
# Generate Complete Export/Import XML File
# --------------------------------------------------------
def generate_items_xml_file_complete(alarm_list, host_name, host_group_name, host_interface):

    zabbix_export = Element('zabbix_export')
    version = SubElement(zabbix_export, 'version')
    version.text = '2.0'

    fmt = '%Y-%m-%dT%H:%M:%SZ'
    date =  SubElement(zabbix_export, 'date')
    date.text = datetime.datetime.now().strftime(fmt)

    groups = SubElement(zabbix_export, 'groups')
    group_under_groups = SubElement(groups, 'group')
    name_under_group = SubElement(group_under_groups, 'name')
    name_under_group.text = host_group_name.upper()

    hosts = SubElement(zabbix_export, 'hosts')
    host_under_hosts = SubElement(hosts, 'host')
    host_under_host = SubElement(host_under_hosts, 'host')
    host_under_host.text = host_name.upper()

    name_under_host = SubElement(host_under_hosts,'name')
    name_under_host.text = host_name.upper()
    SubElement(host_under_hosts, 'proxy')

    status_under_host = SubElement(host_under_hosts, 'status')
    status_under_host.text = '0'

    ipmi_authtype_under_host = SubElement(host_under_hosts, 'ipmi_authtype')
    ipmi_authtype_under_host.text = '-1'

    ipmi_privilege_under_host = SubElement(host_under_hosts, 'ipmi_privilege')
    ipmi_privilege_under_host.text = '2'

    SubElement(host_under_hosts, 'ipmi_username')
    SubElement(host_under_hosts, 'ipmi_password')
    SubElement(host_under_hosts, 'templates')

    groups_under_hosts = SubElement(host_under_hosts, 'groups')
    group_under_groups_host = SubElement(groups_under_hosts, 'group')
    name_group_under_groups_host = SubElement(group_under_groups_host, 'name')
    name_group_under_groups_host.text = host_group_name.upper()

    interfaces_under_host = SubElement(host_under_hosts, 'interfaces')
    interface_under_interfaces_host = SubElement(interfaces_under_host, 'interface')
    default_under_interface = SubElement(interface_under_interfaces_host, 'default')
    default_under_interface.text = '1'

    type_under_interface = SubElement(interface_under_interfaces_host, 'type')
    type_under_interface.text = '2'

    useip_under_interface = SubElement(interface_under_interfaces_host, 'useip')
    useip_under_interface.text = '1'

    ip_under_interface = SubElement(interface_under_interfaces_host, 'ip')
    ip_under_interface.text = host_interface

    SubElement(interface_under_interfaces_host, 'dns')
    port_under_interface = SubElement(interface_under_interfaces_host, 'port')
    port_under_interface.text = '161'

    interface_ref_under_interface = SubElement(interface_under_interfaces_host, 'interface_ref')
    interface_ref_under_interface.text = 'if1'

    SubElement(host_under_hosts, 'applications')
    items = SubElement(host_under_hosts, 'items')
    triggers = SubElement(zabbix_export, 'triggers')

    # Iterate through the unique list to create XML
    for alarm_values in alarm_list:
        item_creator_type_17(items, host_name.upper(), triggers, alarm_values)

    SubElement(host_under_hosts, 'discovery_rules')
    macros = SubElement(host_under_hosts, 'macros')
    macro = SubElement(macros, 'macro')
    sub_macro = SubElement(macro, 'macro')
    value = SubElement(macro, 'value')
    sub_macro.text = '{$SNMP_COMMUNITY}'
    value.text = 'Public'
    SubElement(host_under_hosts, 'inventory')

    return  zabbix_export


def item_creator_type_17(items, host_name, triggers, alarm_values):
    item = SubElement(items, 'item')
    name = SubElement(item, 'name')
    type = SubElement(item, 'type')
    SubElement(item, 'snmp_community')
    multiplier = SubElement(item, 'multiplier')
    SubElement(item, 'snmp_oid')
    key = SubElement(item, 'key')
    delay = SubElement(item, 'delay')
    history = SubElement(item, 'history')
    trends = SubElement(item, 'trends')
    status = SubElement(item, 'status')
    value_type = SubElement(item, 'value_type')
    SubElement(item, 'allowed_hosts')
    SubElement(item, 'units')
    delta = SubElement(item, 'delta')
    SubElement(item, 'snmpv3_contextname')
    SubElement(item, 'snmpv3_securityname')
    snmpv3_securitylevel = SubElement(item, 'snmpv3_securitylevel')
    snmpv3_authprotocol = SubElement(item, 'snmpv3_authprotocol')
    SubElement(item, 'snmpv3_authpassphrase')
    snmpv3_privprotocol = SubElement(item, 'snmpv3_privprotocol')
    SubElement(item, 'snmpv3_privpassphrase')
    formula = SubElement(item, 'formula')
    SubElement(item, 'delay_flex')
    SubElement(item, 'params')
    SubElement(item, 'ipmi_sensor')
    data_type = SubElement(item, 'data_type')
    authtype = SubElement(item, 'authtype')
    SubElement(item, 'username')
    SubElement(item, 'password')
    SubElement(item, 'publickey')
    SubElement(item, 'privatekey')
    SubElement(item, 'port')
    description = SubElement(item, 'description')
    inventory_link = SubElement(item, 'inventory_link')
    SubElement(item, 'valuemap')
    applications = SubElement(item, 'applications')
    application = SubElement(applications, 'application')
    application_name = SubElement(application, 'name')
    interface_ref = SubElement(item, 'interface_ref')

    #
    # Setting basic information for the item.
    #
    name.text = 'An Alarm Notification For : ' + alarm_values['name']
    type.text = '17'
    multiplier.text = '0'
    key.text = 'snmptrap["('+ alarm_values['name'] + ')((.|[[:space:]])*)({#SNMPVALUE})"]'
    delay.text = '0'
    history.text = '90'
    trends.text = '365'
    status.text = '0'
    value_type.text = '2'
    delta.text = '0'
    snmpv3_securitylevel.text = '0'
    snmpv3_authprotocol.text = '0'
    snmpv3_privprotocol.text = '0'
    formula.text = '1'
    data_type.text = '0'
    authtype.text = '0'
    inventory_link.text = '0'
    description.text = alarm_values['description']
    interface_ref.text = 'if1'

    application_name.text = 'Alarms'

    trigger = SubElement(triggers, 'trigger')
    trigger_expression = SubElement(trigger, 'expression')
    trigger_name = SubElement(trigger, 'name')
    SubElement(trigger, 'url')
    trigger_status = SubElement(trigger, 'status')
    trigger_priority = SubElement(trigger, 'priority')
    trigger_description = SubElement(trigger, 'description')
    trigger_type = SubElement(trigger, 'type')
    SubElement(trigger, 'dependencies')

    trigger_expression.text = '{' + host_name + ':snmptrap["('+ alarm_values['name'] + ')((.|[[:space:]])*)({#SNMPVALUE})"].str(' + alarm_values['name'] + ')}=1'
    trigger_name.text = 'ATTENTION : On {HOST.NAME}, An Alarm : ' + alarm_values['name'] + ' - {#SNMPVALUE}, From Module : ' +alarm_values['mib_module']
    trigger_status.text = '0'
    trigger_priority.text = '3'
    trigger_description.text = description.text
    trigger_type.text = '0'


def xml_pretty_me(file_name_for_prettify, string_to_prettify):
    #
    # Open a file and write to it and we are done.
    #
    logging.info("Creating File %s", file_name_for_prettify)

    xml = minidom.parseString(string_to_prettify)
    pretty_xml_as_string = xml.toprettyxml()
    output_file = open(file_name_for_prettify, 'w' )
    output_file.write(pretty_xml_as_string)
    logging.info("Creation Complete")
    output_file.close()

def read_from_csv(csv_file_name):
    try:
        reader = csv.reader(open(csv_file_name, 'r'))
        return reader
    except exception:
        print("Something went wrong in reading file" + str(exception))
        exit()


# --------------------------------------------------------
# Help Menu
# --------------------------------------------------------
def help_menu():
    logging.error(" Wrong Arguments - Please see below for more information")
    logging.error("""\n
     --------------------------------------------
                        USAGE
     --------------------------------------------

     1. To Generate xml import file.
     --------------------------------------------
     python zabbix_snmp_trap_import_from_csv.py <export_csv> <host_name> <host_group_name> <host_interface_name>
     \texample: python zabbix_snmp_trap_import_from_csv.py export_csv_from_ireasoning_mib_browser.csv GGSN-1-LONDON GGSN-GROUP 127.0.0.1

     Parameter Information
     --------------------------------------------
     <export_csv>           : Is the XML KPI file for GGSN Device.
     <host_name>            : Host name as given in Zabbix server.
     <host_group_name>      : Host Group which the host belongs to, as in Zabbix server.
     <host_interface_ip>    : SNMP Interface configured on Zabbix server. (Assuming Single Interface in Configured)
     --------------------------------------------
     """)
    exit()

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    # System Arguments check
    if len(sys.argv) == 1 or len(sys.argv) != 5:
        help_menu()

    xml_file_name = sys.argv[1]
    host_name = sys.argv[2]
    host_group_name = sys.argv[3]
    host_interface_ip = sys.argv[4]

    csv_reader = read_from_csv('export_csv_from_ireasoning_mib_browser.csv')

    alarm_list = []
    for alarm_data in csv_reader:

        # Skipping First Line
        if alarm_data[0] == "Name":
            continue

        oid_dictionary = {}
        oid_dictionary['name'] = alarm_data[0]
        oid_dictionary['full_name'] = alarm_data[1]
        oid_dictionary['oid'] = alarm_data[2]
        oid_dictionary['type'] = alarm_data[3]
        oid_dictionary['access'] = alarm_data[4]
        oid_dictionary['indexes'] = alarm_data[5]
        oid_dictionary['mib_module'] = alarm_data[6]
        oid_dictionary['description'] = alarm_data[7].strip('"')
        alarm_list.append(oid_dictionary)


    xml_tree = generate_items_xml_file_complete(alarm_list, host_name, host_group_name, host_interface_ip)
    xml_pretty_me(host_name.lower()+'-item-trigger-import.xml', ElementTree.tostring(xml_tree))

