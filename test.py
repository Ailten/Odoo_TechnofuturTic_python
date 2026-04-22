
from functools import reduce
print(

    reduce(lambda a, b : (
        a | b
    ), ( 
        {
            { (x, y) for y in range(0, 4)}
        for x in range(0, 4) }
    ))

)