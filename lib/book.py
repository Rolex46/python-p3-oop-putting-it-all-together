#!/usr/bin/env python3

#!/usr/bin/env python3

class Book:
    def __init__(self,title,page_count = 0):
        self.title = title
        self.page_count = page_count

        

    def get_pagec(self):
        print("retrieving pagecount")
        return self._page_count
    
    def set_pagec(self,page_count):
        if isinstance(page_count, int):
            print(f"setting page_count to {page_count}")
            self._page_count = page_count
        else:
            print("page_count must be an integer")

    page_count = property(get_pagec,set_pagec)

    def turn_page(self):
        print("Flipping the page...wow, you read fast!" )
