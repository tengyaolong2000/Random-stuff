# TODO: complete this class
from math import ceil
from math import floor

class PaginationHelper:

  # The constructor takes in an array of items and a integer indicating
  # how many items fit within a single page
  def __init__(self, collection, items_per_page):
    self.collection = collection
    self.items_per_page = items_per_page
  
  def divide_into_chunks(self):
    for i in range(0, len(self.collection),self.items_per_page):
      yield self.collection[i:i+self.items_per_page]
      
  
  # returns the number of items within the entire collection
  def item_count(self):
    return len(self.collection)
  
  # returns the number of pages
  def page_count(self):
    return ceil(len(self.collection)/self.items_per_page)


      
  # returns the number of items on the current page. page_index is zero based
  # this method should return -1 for page_index values that are out of range
  def page_item_count(self,page_index):
    y = self.page_count()
    if page_index >= 0 and page_index <= y-1:
      x = self.divide_into_chunks()
      x = list(x)
      return len(x[page_index])
    else:
      return -1


      
  
  # determines what page an item is on. Zero based indexes.
  # this method should return -1 for item_index values that are out of range
  def page_index(self,item_index):
    if item_index >= 0 and item_index <= len(self.collection)-1:
      x = floor(item_index/self.items_per_page)
      return x
    else:
      return -1
    


collection = range(1,25)
print(len(collection))
helper = PaginationHelper(collection, 10)
z = helper.page_count()
print(z)
x = helper.page_item_count(3)
print(x)
y = helper.divide_into_chunks()
print(list(y))

