import base64

OUTPUT_PATH = "puzzle_from_terminal.png"

# حالت: "binary", "hex" یا "base64"
MODE = input("Enter mode (binary/hex/base64): ").strip().lower()

data_input = input("Paste your data here (all in one line): ").strip()

if MODE == "binary" :
    if len(data_input) % 8 != 0:
        pad_len = 8 - (len(data_input) % 8)
        data_input += "0" * pad_len
    b = bytes(int(data_input[i:i+8], 2) for i in range(0, len(data_input), 8))

elif MODE == "hex":
    data_input = "".join(data_input.split())
    b = bytes.fromhex(data_input)

elif MODE == "base64":
    data_input = "".join(data_input.split())
    b = base64.b64decode(data_input)

else:
    raise ValueError("Unknown mode. Choose binary, hex or base64.")

with open(OUTPUT_PATH, "wb") as f:
    f.write(b)

print(f"[+] File '{OUTPUT_PATH}' created. Size: {len(b)} bytes")