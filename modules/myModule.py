def top_n(items,n):
    """ Returns number of  in items"""
    p= sorted(items,reverse=True)
    p=p[:n]
    return p
top_n([8,3,2,7,4],3)
