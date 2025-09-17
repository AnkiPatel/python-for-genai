# DICTIONARY OPERATIONS AND METHODS: ACCESSING, UPDATING, .GET(), .KEYS(), AND .VALUES()

# ASSIGNMENT AND COPYING
print('ASSIGNMENT AND COPYING\n-------------------------')
# Creating a dictionary
model_params = {'layers': 24, 'units': 512, 'activation': 'relu'}

# Assigning the same dictionary reference to another variable (not a copy)
shared_params = model_params  # Both variables point to the same dictionary
print(id(model_params)) #OP:2237327713664
print(id(shared_params)) #OP:2237327713664

# Modifying the dictionary affects both variables
model_params['activation'] = 'gelu'
print(model_params) #OP:{'layers': 24, 'units': 512, 'activation': 'gelu'}
print(shared_params) #OP:{'layers': 24, 'units': 512, 'activation': 'gelu'}


# Creating a separate copy of the dictionary to avoid unintentional modifications
safe_params = model_params.copy()
print(id(model_params)) #OP:2237327713664
print(id(safe_params)) #OP:2472584186304
# Modifying model_params does not affect safe_params (since it's a separate copy)
model_params['layers'] = 48
print(model_params) #OP:{'layers': 48, 'units': 512, 'activation': 'gelu'}
print(safe_params)  #OP:{'layers': 24, 'units': 512, 'activation': 'gelu'}

# MERGING DICTIONARIES WITH update()
base_config = {'batch_size': 32, 'epochs': 10}
version_config = {'learning_rate': 0.001, 'units': 128}

# Merge version_config into base_config (overwriting matching keys)
base_config.update(version_config)
print(base_config) #OP:{'batch_size': 32, 'epochs': 10, 'learning_rate': 0.001, 'units': 128}

# CLEARING A DICTIONARY
# Removes all key-value pairs from model_params
model_params.clear()
print(model_params)  #OP:{}

# DICTIONARY VIEWS WITH .keys(), .values(), AND .items()

# Get all keys from base_config
print(base_config.keys()) #op:dict_keys(['batch_size', 'epochs', 'learning_rate', 'units'])

# Get all values from base_config
print(base_config.values()) #op:dict_values([32, 10, 0.001, 128])

# Iterate through key-value pairs
for key, value in base_config.items():
    print(f'{key} => {value}')
# Output:
# batch_size => 32
# epochs => 10
# learning_rate => 0.001
# units => 128

# TESTING MEMBERSHIP USING in

# Check if a key exists in the dictionary
print('batch_size' in base_config)  # Output: True

# Check if a value exists in the dictionary
print(32 in base_config.values())  # Output: True

# Check if a key-value pair exists in the dictionary
print(('batch_size', 32) in base_config.items())  # Output: True

# Removing from dictionary
# dict.pop(key) -> Remove item for givne key

pc_config = {'Linux': 6.7, 'flavour': 'red-hat'}
print(f'pc_config: {pc_config}') #OP:pc_config: {'Linux': 6.7, 'flavour': 'red-hat'}
val = pc_config.pop('flavour');
print(f'pc_config: {pc_config}, val: {val}') #OP:pc_config: {'Linux': 6.7}, val: red-hat

#val = config_a1.pop('abc'); # since 'abc' key is not there, this will give error
#Safer way
val = pc_config.pop('abc', 'Not found');
print(f'pc_config: {pc_config}, val: {val}') #pc_config: {'Linux': 6.7}, val: Not found

# dict.popitem() -> Remove the last item from dictionary
pc_config = {'Linux': 5.3, 'flavour': 'Ubuntu', 'ram': '512'}
val = pc_config.popitem();
print(f'pc_config: {pc_config}, val: {val}') #op:pc_config: {'Linux': 5.3, 'flavour': 'Ubuntu'}, val: ('ram', '512')

# delete the dictionary
# del dictionary[key] -> delete
pc_config = {'Linux': 5.3, 'flavour': 'Ubuntu', 'ram': '512'}
del pc_config['Linux']
print(f'pc_config: {pc_config}') #op:pc_config: {'flavour': 'Ubuntu', 'ram': '512'}


# MATHEMATICAL SET OPERATIONS WITH DICTIONARY KEYS AND ITEMS

config_a = {'batch_size': 32, 'optimizer': 'adam'}
config_b = {'batch_size': 64, 'optimizer': 'adam', 'momentum': 0.9}

# Find common keys between two dictionaries using set intersection
common_config = config_a.keys() & config_b.keys()
print(common_config) #op: {'optimizer', 'batch_size'}

# Find all possible keys between two dictionaries using set union
all_config = config_a.keys() | config_b.keys()
print(all_config) #op: {'optimizer', 'batch_size', 'momentum'}

pc_config = {'Linux': 5.3, 'flavour': 'Ubuntu', 'ram': '512'}

# ITERATING OVER KEYS, VALUES, AND ITEMS

# Iterate over keys
for key in pc_config:
    print(f'Key: {key}')

# Iterate over values
for value in pc_config.values():
    print(f'Value: {value}')

# Iterate over key-value pairs
for key, value in pc_config.items():
    print(f'{key} => {value}')