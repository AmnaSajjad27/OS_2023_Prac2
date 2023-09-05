from mmu import MMU
from random import randint

class RandMMU(MMU):
    def __init__(self, frames):
        super().__init__(frames)
        for i in range(frames):
            self.page_table.append([None, None])
    
    def find_page(self, page_number):

        pages = [page[0] for page in self.page_table]

        if page_number in pages:
            return pages.index(page_number)
        
        self.total_page_faults += 1 
        return False
    
    def select_victim(self):
        victim_idx = randint(0, self.frames - 1)
        return victim_idx   
    
    def read_memory(self, page_number):

        idx = self.find_page_number(page_number)

        #page found
        if idx is not False:
            return
        
        # page does not exist
        # no empty frames
        if self.find_empty_frame() == -1:
            victim = self.select_victim()
            
            if(self.page_table[victim][1] == 1):
                self.page_table[victim] = [page_number, 0]
                self.total_disk_writes += 1
        else:
            # empty frame exists
            self.page_table[self.find_empty_frame()] = [page_number, 0]
        
        self.total_disk_reads += 1

    def write_memory(self, page_number):
        
        idx = self.find_page_number(page_number)
        #page found
        if idx is not False:
            self.page_table[idx][1] = 1
            return
        
        # page does not exist
        # no empty frames
        if self.find_empty_frame() == -1:
            victim = self.select_victim()
            
            if(self.page_table[victim][1] == 1):
                self.page_table[victim] = [page_number, 1]
                self.total_disk_writes += 1 
        
        else:
            # empty frame exists
            self.page_table[self.find_empty_frame()] = [page_number, 1]
        
        self.total_disk_reads += 1
        

    def set_debug(self):
        super().set_debug()

    def reset_debug(self):
        super().reset_debug()

    def get_total_disk_reads(self):
        return super().get_total_disk_reads()

    def get_total_disk_writes(self):
        return super().get_total_disk_writes()

    def get_total_page_faults(self):
        return super().get_total_page_faults()
