'''
* Interface for Memory Management Unit.
* The memory management unit should maintain the concept of a page table.
* As pages are read and written to, this changes the pages loaded into the
* the limited number of frames. The MMU keeps records, which will be used
* to analyse the performance of different replacement strategies implemented
* for the MMU.
*
'''
class MMU:

    page_table = []             ## Page_table is a list of pages of the form -
                                ## [[page_number, dirty_bit], ..., [page_number, dirty_bit]]

    def __init__(self, frames):
        self.frames = frames
        self.total_disk_reads = 0
        self.total_disk_writes = 0
        self.total_page_faults = 0
        self.debug_mode = ""

        for i in range(frames):
            self.page_table.append([None, None])


    def read_memory(self, page_number):
        """ 
        This method is called when a page is read from memory.
        The method calls find_page_number to find the page number in the page table.
        Params: page_number - The page number to be read
        Returns: Same return value as find_page_number()
        """
        return self.find_page_number(page_number)

    def write_memory(self, page_number):
        pass

    def find_page_number(self, page_number):
        """ 
        Finds the page number in the page table and returns the index of the page.
        Params: page_number - The page number to be found
        Returns: index of page_number in page_table, -1 if page_number not found 
        """
        for i in range(len(self.page_table)):
            if self.page_table[i][0] == page_number:
                return i
        return -1
    
    def find_empty_frame(self):
        """
        
        """
        pages = [page[0] for page in self.page_table]  # List of page numbers in page table
        if(pages.count(None) > 0):
            return pages.index(None)                   # Return index of first empty frame

        return False                                   # Return False if no empty frames
        

    def set_debug(self):
        self.debug_mode = "debug"

    def reset_debug(self):
        self.debug_mode = "quiet"

    def get_total_disk_reads(self):
        return self.total_disk_reads

    def get_total_disk_writes(self):
        return self.total_disk_writes

    def get_total_page_faults(self):
        return self.total_page_faults
