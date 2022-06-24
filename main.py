from eth_account import Account
import secrets
import argparse
import json
from collections import defaultdict

parser = argparse.ArgumentParser()
parser.add_argument("-n", "--number", help="number of address to be generated")
parser.add_argument("-f", "--filename", help="file name of the csv")
args = parser.parse_args()

num_of_address = int(args.number)
file_name = args.filename 

def write_csv(address, key):
    with open(file_name +'.csv', 'a') as f:
            f.write(str(address) + ',' + str(key))
            f.write('\n')

def write_json(d):
    with open(file_name +'.json', 'a', encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False, indent=4)

d = defaultdict(list)
for i in range(num_of_address):
    priv = secrets.token_hex(32)
    private_key = "0x" + priv
    acct = Account.from_key(private_key)
    write_csv(acct.address, private_key)
    d[acct.address].append(private_key)
write_json(d)