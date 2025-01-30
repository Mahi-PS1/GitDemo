# Problem stmt in automated scrip the cart 
# have 2 items but they by any case do not get added , in that case to for failed case exception are being thrown 
CartCount = 0 
if CartCount!=2:
    raise Exception("Cart Products count in not 2") 


# 2 ways to raise exceptions 1 by raise Exception other comman and desired way is assertion 