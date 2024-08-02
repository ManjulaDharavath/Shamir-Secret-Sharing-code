import json

# Function to convert a value from any base to base 10
def convert_to_base10(value, base):
    return int(value, base)

# JSON-like input string
input_str = '''
{
    "keys": {
        "n": 4,
        "k": 3
    },
    "1": {
        "base": "10",
        "value": "4"
    },
    "2": {
        "base": "2",
        "value": "111"
    },
    "3": {
        "base": "10",
        "value": "12"
    },
    "6": {
        "base": "4",
        "value": "213"
    }
}
'''

# Parse the JSON string
data = json.loads(input_str)

# Extract n and k
n = data['keys']['n']
k = data['keys']['k']

# Extract the key-value pairs and convert values to base 10
pairs = {}
for key, value in data.items():
    if key not in ['keys']:
        base = int(value['base'])
        val = value['value']
        pairs[int(key)] = convert_to_base10(val, base)

# Output n, k, and converted pairs
print(f"n: {n}")
print(f"k: {k}")
print("Converted Pairs:")
for key, value in pairs.items():
    print(f"  ({key}, {value})")

# Function to reconstruct the secret
def reconstruct_secret(pieces):
    # Pieces are given as (index, value)
    n = len(pieces)
    
    # We need exactly k pieces to reconstruct the secret
    if n < k:
        raise ValueError(f"Need at least {k} pieces to reconstruct the secret")

    # Extract indices and values from pieces
    indices = [piece[0] for piece in pieces]
    values = [piece[1] for piece in pieces]

    # Calculate the coefficients of the polynomial
    # Using Lagrange interpolation formula to find the secret
    def lagrange_interpolation(x, indices, values):
        total = 0
        n = len(indices)
        for i in range(n):
            xi, yi = indices[i], values[i]
            term = yi
            for j in range(n):
                if i != j:
                    xj = indices[j]
                    term *= (x - xj) / (xi - xj)
            total += term
        return total

    # The secret D is the value of the polynomial at x = 0
    D = lagrange_interpolation(0, indices, values)

    return D

# Convert the pairs dictionary to a list of tuples sorted by the index
pieces_list = sorted(pairs.items())

# Use the first k pieces to reconstruct the secret
secret = reconstruct_secret(pieces_list[:k])
print("The secret is:", secret)

# Now we handle the provided test case

# Read the JSON file content
file_path = 'testcase2.json'
with open(file_path, 'r') as file:
    data = json.load(file)

# Extract n and k
n = data['keys']['n']
k = data['keys']['k']

# Extract the key-value pairs and convert values to base 10
pairs = {}
for key, value in data.items():
    if key not in ['keys']:
        base = int(value['base'])
        val = value['value']
        pairs[int(key)] = convert_to_base10(val, base)

# Output n, k, and converted pairs for the provided test case
print(f"n: {n}")
print(f"k: {k}")
print("Converted Pairs:")
for key, value in pairs.items():
    print(f"  ({key}, {value})")

# Convert the pairs dictionary to a list of tuples sorted by the index
pieces_list = sorted(pairs.items())

# Use the first k pieces to reconstruct the secret
secret = reconstruct_secret(pieces_list[:k])
print("The secret is:", secret)