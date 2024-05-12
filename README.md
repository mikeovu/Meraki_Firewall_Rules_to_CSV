# Firewall_Rules_to_CSV

prototype code to output L3 and L7 firewall rules from Dashboard to JSON and CSV files.

## Contacts

- Michael Vu

## Solution Components

- Meraki
- MX

## Installation/Configuration

This is as a template, project owner to update

1. Include your personal api key inside the config.py file for the script to use

```python
    api_key=""

```

2. install the dependencies required for the python script

```console
foo@bar(env):~$ pip install -r requirements.txt
```

3. run the python script

```console
foo@bar:~$ python3 security_to_csv.py
```

4. You will be asked to specify the Dashboard Organization you will be requesting firewall rules from.

5. You will be asked to specify the network you will be requesting firewall rules from.

# Notes

# Screenshots

MX firewall rules you will be outputting to JSON and CSV

![/IMAGES/Dashboard_Firewall_Rules.png](/IMAGES/Dashboard_Firewall_Rules.png)

4th step

![/IMAGES/Specify_Organization.png](/IMAGES/Specify_Organization.png)

5th step

![/IMAGES/Specify_Network.png](/IMAGES/Specify_Network.png)

Firewall Rules Directory

![/IMAGES/firewall_rules_output.png](/IMAGES/firewall_rules_output.png)

L3 Firewall Rules CSV & JSON

![/IMAGES/L3_Rules_CSV.png](/IMAGES/L3_Rules_CSV.png)

![/IMAGES/L3_Rules_JSON.png](/IMAGES/L3_Rules_JSON.png)

L7 Firewall Rules CSV & JSON

![/IMAGES/L7_Rules_CSV.png](/IMAGES/L7_Rules_CSV.png)

![/IMAGES/L7_Rules_JSON.png](/IMAGES/L7_Rules_JSON.png)

### CODE_OF_CONDUCT

Our code of conduct is available [here](CODE_OF_CONDUCT.md)

#### DISCLAIMER:

<b>Please note:</b> This script is meant for demo purposes only. All tools/ scripts in this repo are released for use "AS IS" without any warranties of any kind, including, but not limited to their installation, use, or performance. Any use of these scripts and tools is at your own risk. There is no guarantee that they have been through thorough testing in a comparable environment and we are not responsible for any damage or data loss incurred with their use.
You are responsible for reviewing and testing any scripts you run thoroughly before use in any non-testing environment.
