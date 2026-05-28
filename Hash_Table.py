class HashTable:
    def __init__(self):
        # Initialize collection to an empty dictionary
        self.collection = {}

    def hash(self, key_string):
        # Compute the sum of the Unicode (ASCII) values of each character
        return sum(ord(char) for char in key_string)

    def add(self, key, value):
        # Compute the hash value of the key
        hash_key = self.hash(key)
        
        # If the hash key is not in the collection, create a new nested dictionary
        if hash_key not in self.collection:
            self.collection[hash_key] = {}
            
        # Store the key-value pair inside the nested dictionary
        self.collection[hash_key][key] = value

    def remove(self, key):
        # Compute the hash value of the key
        hash_key = self.hash(key)
        
        # Check if the hash exists and the specific key is within that nested dictionary
        if hash_key in self.collection and key in self.collection[hash_key]:
            del self.collection[hash_key][key]
            
            # Clean up the parent dictionary index if the nested dictionary becomes empty
            if not self.collection[hash_key]:
                del self.collection[hash_key]

    def lookup(self, key):
        # Compute the hash value of the key
        hash_key = self.hash(key)
        
        # Check if the hash exists and the key is within the nested dictionary
        if hash_key in self.collection and key in self.collection[hash_key]:
            return self.collection[hash_key][key]
            
        # Return None if the key does not exist
        return None
