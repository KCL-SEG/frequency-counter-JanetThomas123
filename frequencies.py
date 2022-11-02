"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""
def remove_items(test_list, item):
 
    # using filter() + __ne__ to perform the task
    res = list(filter((item).__ne__, test_list))
 
    return res
 
def frequencies(items):
    frequencies = {}
    # Your code goes here
    i = 0
    items = [str(r) for r in items]
    while i < len(items):
        count = items.count(items[i])
        frequencies[items[i]] = count
        items = remove_items(items, items[i])
    return frequencies
    
    
