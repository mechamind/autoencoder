# Developer: Dr. Pankaj Kumar
# pkumar.vt@gmail.com

import sys

def read_user_input():
    parsed_data = {}
    with open("user_input.inp", 'r') as file:
        for line in file:
            if line.startswith('#') or len(line.strip())==0:
                continue
            parts = line.strip().split(':')
            if len(parts) != 2:
                print("Error: Not valid input", line.strip())
                sys.exit()
            
            # Extract key and value from valid intputs
            key = parts[0].strip()
            value = parts[1].strip()
            try:
                # Reading numeric values
                if value.isdigit():
                    value = int(value)
                else:
                    value = float(value)
            except ValueError:
                pass
            parsed_data[key] = value
    return parsed_data

