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
                                ## dirty_bit is 1 if page has been written to, 0 otherwise

    def __init__(self, frames):
        self.frames = frames
        self.total_disk_reads = 0
        self.total_disk_writes = 0
        self.total_page_faults = 0
        self.debug_mode = False


    def read_memory(self, page_number):
        pass

    def write_memory(self, page_number):
        pass

    def find_page_number(self, page_number):

        pages = [page[0] for page in self.page_table]

        if page_number in pages:
            return pages.index(page_number)
        
        self.total_page_faults += 1 
        return False

    def find_empty_frame(self):

        pages = [page[0] for page in self.page_table]
        
        free_frame_count = pages.count(None)

        #return index of first free frame
        if free_frame_count > 0:
            try:
                return pages.index(None)
            except ValueError:
                return -1
            
        return -1


    def set_debug(self):
        self.debug_mode = True

    def reset_debug(self):
        self.debug_mode = False

    def get_total_disk_reads(self):
        return self.total_disk_reads

    def get_total_disk_writes(self):
        return self.total_disk_writes

    def get_total_page_faults(self):
        return self.total_page_faults
    

