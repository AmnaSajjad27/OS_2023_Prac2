# OrderedDict to maintain the insertion order 
from collections import OrderedDict 
# this is inheriting from base class MMU
from mmu import MMU

class LruMMU(MMU):
    def __init__(self, frames):
        # Constructor logic for LruMMU
        self.frames = frames
        # Using an ordered dictionary to keep track of the order in what the pages were accessed in 
        self.cache = OrderedDict()
        # Flag to print debug info or not 
        self.debug_mode = False
        # Counters for disk reads, writes and pages requested from disk memory 
        self.total_disk_reads = 0
        self.total_disk_writes = 0
        self.total_page_faults = 0

    def set_debug(self):
        # set to true initally 
        self.debug_mode = True

    def reset_debug(self):
        # set to false initally 
        self.debug_mode = False

    def read_memory(self, page_number):
        # Moved accessed pages
        if page_number in self.cache:
            # move to the end, update least recently used 
            self.cache.move_to_end(page_number)
        # page fault occurs and page needs to be loaded from disk into memory     
        else:
            # increment number of page faults 
            self.total_page_faults +=1 

                # kick off the page and update the list of least recently used
            if len(self.cache) >= self.frames:
                # pop item removes the last inserted key-value pair and returns it
                # the popped out page number is assigned to "evicted page" 
                # value is ignored by _ because we dont need it
                evicted_page, _ = self.cache.popitem(last = False)
                if self.debug_mode:
                    print(f"Page popped off frames {evicted_page}")

            # Add a new page to the cache frames 
            self.cache[page_number] = None
            
            # increment the number of disk reads
            self.total_disk_reads += 1
            
        if self.debug_mode:
            print(f"Reading Page number {page_number}")

    def write_memory(self, page_number):
        # dirty/modified page, write into memory
        self.read_memory(page_number)
        # increment counter 
        self.total_disk_writes += 1

        if (self.debug_mode):
            print(f"Page written{page_number}")

    def get_total_disk_reads(self):
        # return counter 
        return self.total_disk_reads

    def get_total_disk_writes(self):
        # return counter
        return self.total_disk_writes

    def get_total_page_faults(self):
        # return page faults 
        return self.total_page_faults
