import meraki
import json
import config
import csv

dashboard = meraki.DashboardAPI(config.api_key,single_request_timeout=999999)

# Uses the Meraki library to grab Organization info.
orgs = dashboard.organizations.getOrganizations()

# Displays the org name and ID 
for org in orgs:
    print("Organization name: " + str(org["name"]) + " | " + "ID: " + str(org["id"]))

# Prompts user to select Organization ID

org_id = input("Select an organization id: ")

# Displays dashboard orrganization mapped to organization ID
networks = dashboard.organizations.getOrganizationNetworks(organizationId=org_id)

# Displays all networks in the organization the user has selected

for network in networks:
    print("Network name: " + str(network["name"]) + " | " + "ID: " + str(network["id"]))

print("-------------------------------------")
breaker = "1"
networks_to_output = []

# Promps user to specify network ids that they would like to see

while breaker == "1":
    net_id = input("Continue to add network IDs that you want to receive L3 and L7 firewall rule outputs, enter 0 when finished\n")

    if net_id == "0":
        breaker = "0"
        break

    networks_to_output.append(net_id)

confirmation = input("press y to proceed ")

# Iterates through L7 rules of chosen network and creates a json file containing l7 policies

for network in networks_to_output:
    with open('firewall_rules/l7_rules.json', 'w') as f:
        output_l7_response = dashboard.appliance.getNetworkApplianceFirewallL7FirewallRules(networkId=network)
        json.dump(output_l7_response, f, indent=2)

# Iterates through L3 rules of chosen network and creates a json file containing L3 policies

for network in networks_to_output:
    with open('firewall_rules/l3_rules.json', 'w') as f:
        output_l3_response = dashboard.appliance.getNetworkApplianceFirewallL3FirewallRules(networkId=network)
        json.dump(output_l3_response, f, indent=2)


# Convert L7_rules.json to csv

with open('firewall_rules/l7_rules.json') as l7_rules:
    l7_policies = json.load(l7_rules)

policies = l7_policies['rules']

# Open csv for writing l7 rules

rule_data = open('firewall_rules/l7_rules.csv', 'w')

# create the csv writer object
csv_writer = csv.writer(rule_data)

# Counter variable used for writing
# headers to the csv file

count = 0

for rule in policies:
    if count == 0:

# Writing headers of CSV file
        header = rule.keys()
        csv_writer.writerow(header)
        count += 1

# Writing data of CSV file
    csv_writer.writerow(rule.values())

l7_rules.close()

# Convert L3_rules.json to csv

with open('firewall_rules/l3_rules.json') as l3_rules:
    l3_policies = json.load(l3_rules)

policies = l3_policies['rules']

# Open csv for writing l7 rules

rule_data = open('firewall_rules/l3_rules.csv', 'w')

# create the csv writer object
csv_writer = csv.writer(rule_data)

# Counter variable used for writing
# headers to the csv file

count = 0

for rule in policies:
    if count == 0:

# Writing headers of CSV file
        header = rule.keys()
        csv_writer.writerow(header)
        count += 1

# Writing data of CSV file
    csv_writer.writerow(rule.values())

l3_rules.close()
