from mmu import MMU


class ClockMMU(MMU):
    def __init__(self, frames):
        super().__init__(frames)
        self.hand = 0 
        self.total_disk_reads = 0
        self.total_disk_writes = 0
        self.total_page_faults = 0
  

    def set_debug(self):
        # TODO: Implement the method to set debug mode
        pass

    def reset_debug(self):
        # TODO: Implement the method to reset debug mode
        pass

    def read_memory(self, page_number):
        
        page_index = self.find_page_number(page_number)
        
        if page_index is not False:
        # Page is already in memory, update the use bit to 1
            self.page_table[page_index][2] = 1
            return
            
        empty_frame = self.find_empty_frame()
        if empty_frame is not False:
            self.total_disk_reads+=1
            self.total_page_faults+=1
            self.page_table[empty_frame]=[page_number,0,1]
        else:
            self.total_disk_reads+=1
            self.total_page_faults+=1
            self.replaceCLOCK(page_number,"r")

        
    def write_memory(self, page_number):
        page_index = self.find_page_number(page_number)
        if page_index is not False:
            self.page_table[page_index][1] = 1
            self.page_table[page_index][2] = 1
            return
        
        empty_frame = self.find_empty_frame()

        if empty_frame is not False:
            self.total_disk_reads+=1
            self.total_page_faults+=1
            self.page_table[empty_frame]=[page_number,1,1]
        else:
            self.total_disk_reads+=1
            self.total_page_faults+=1
            self.replaceCLOCK(page_number,"w")

    def get_total_disk_reads(self):
        # TODO: Implement the method to get total disk reads
        return self.total_disk_reads

    def get_total_disk_writes(self):
        # TODO: Implement the method to get total disk writes
        return self.total_disk_writes

    def get_total_page_faults(self):
        # TODO: Implement the method to get total page faults
        return  self.total_page_faults
    
    def replaceCLOCK(self, page_number,operation):

        while True:
            
            if self.page_table[self.hand][2]== 0:  
                if self.page_table[self.hand][1] == 0:
                    
                    if (operation=="r"):
                       self.page_table[self.hand] = [page_number, 0, 1] 
                    elif (operation == "w"):
                       self.page_table[self.hand] = [page_number, 1, 1] 

                    self.hand = (self.hand + 1) % self.frames 
        
                    return
                    
                else:
                    self.total_disk_writes += 1

                    if (operation=="r"):
                        self.page_table[self.hand] = [page_number, 0, 1]  
                    elif (operation == "w"):
                        self.page_table[self.hand] = [page_number, 1, 1]  

                    self.hand = (self.hand + 1) % self.frames
                                    
                    return
                     
            else:
                self.page_table[self.hand][2]= 0
                self.hand = (self.hand + 1) % self.frames
        