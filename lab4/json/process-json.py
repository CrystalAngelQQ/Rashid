import json

with open("sample-data.json", "r") as read_file:
    data = json.load(read_file)

dn_length = 50 - 1
description_length = 20 - 1
speed_length = 10 - 1
mtu_length = 10 - 1

print("Interface Status")
print("=" * (dn_length + description_length + speed_length + mtu_length + 4))
print(
    f"{'DN':{dn_length}} {'Description':{description_length}} {'Speed':{speed_length}} {'MTU':{mtu_length}}"
)
print("-" * dn_length, "-" * description_length, "-" * speed_length, "-" * mtu_length)
for interface in data["imdata"]:
    attributes = interface["l1PhysIf"]["attributes"]
    dn = attributes["dn"]
    description = attributes["descr"]
    speed = attributes["speed"]
    mtu = attributes["mtu"]
    print(
        f"{dn:{dn_length}} {description:{description_length}} {speed:{speed_length}} {mtu:{mtu_length}}"
    )
