'''
we are going to implement the hash map using a technique of searching 'hashing'
so we are going to implement the HashTable class using two lists
slots list==> this will be our hash table on which we are going to perform all the operation of hashing upon the keys
data list ==> this will store the data.. each slot of this list corresponds to it key in the slots list

READ into the section of Hashing in the Problem solving using Data Structures and Algorithms in python Book
'''
class HashTable:
    def __init__(self):
        self.size = 11  # must be a prime number to be able to use the whole slots
        self.slots = [None] * self.size     # stores the keys after get hashed
        self.data = [None] * self.size      # stores the data for each key in a corresponding place

    def put(self, key, val):
        """ This function takes a key-value pair and store them into the map """
        # compute the hash code for the key
        hash_code = self.hashFunction(key)

        # check for the hash code in the slots table
        # if empty.. put the key and data 
        if self.slots[hash_code] == None:
            self.slots[hash_code] = key
            self.data[hash_code] = val

        # if not empty.. two odds..collision { occuped(same key) or occuped(with other key) }
        elif self.slots[hash_code] != None:
            # if the same key.. replace data
            if self.slots[hash_code] == key:
                # overwrite the data
                self.data[hash_code] = val

            else:   # slot occuped with other key... rehash till get an empty slot
                next_hash = self.rehash(key)

                # iterate over the slots list
                while self.slots[next_hash] != None and self.slots[next_hash] != key:
                    # get new hash value using open addressing 'plus 1' linear probing
                    next_hash = self.rehash(next_hash)

                # now got an empty slot.. douple check and insert the data 
                if self.slots[next_hash] == None:
                    self.slots[next_hash] = key
                    self.data[next_hash] = val
                else:
                    # overwirte the existing data
                    self.data[next_hash] = val
                
    def get(self, key):
        """ Given a key.. we have to return the value associated with if it exist or None """
        # get the hash code for this key
        hash_code = self.hashFunction(key)

        # keep track of the first slot to break out of the loop when we come back again to the first of the table
        start_slot = hash_code 

        # make a boolean value to change its state when we get back to the begin of the table to be able to stop the looping
        stop = False

        next_hash = hash_code       # this like the counter.. to change its value every iteration to the next expected slot to be existing in
        while self.slots[next_hash] != None and not stop:   # iterate over the occuped slots
            # check for the current slot key
            if self.slots[next_hash] == key:
                # data found
                return self.data[next_hash]

            else:   # not the key we search for
                # so rehash to get the next expected slot to be exist in
                next_hash = self.rehash(next_hash)

                # check if we get back to the begining again.. break
                if self.slots[next_hash] == self.slots[start_slot]:
                    stop = True

        # not found 
        return None

    def __getitem__(self, key):
        """ This function is going to allow for using [] for get() method  on form of obj[key] """
        return self.get(key)

    def __setitem__(self, key, val):
        """ This function will allow for using put[key] = val """
        return self.put(key, val)

    def length(self):
        pass

    def hashFunction(self, key):
        # I am going to use the remainder method for hashing keys to get their hash codes
        return key % self.size

    def rehash(self, old_hash):
        """ 
            To resolve the collisions, I will use the Open addressing with linear probing
            'plus 1' technique, which means we increment the slots by one
            h(pos) = (pos + 1) % Table_size
        """
        return (old_hash + 1) % self.size


if __name__ == '__main__':

    h = HashTable()
    
    # put the data into the table
    h[54] = 'cat'
    h[26] = 'dog'
    h[93] = 'lion'
    h[17] = 'tiger'
    h[77] = 'bird'
    h[31] = 'cow'
    h[44] = 'goat'
    h[55] = 'pig'
    h[20] = 'chicken'

    # print the hash table (key list)
    print(h.slots)

    # print the data
    print(h.data)

    # getting data from the map using its key
    print(h[54])        # 'cat'
    print(h[77])        # 'bird'
    print(h[44])        # 'goat'
    print(h[4323])      # None

'''
The get(key) method is still not working at... recheck it please 
'''