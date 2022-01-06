rabs, seats = [int(i) for i in input().split()]
rab_coords = []
seat_coords = []
for i in range(rabs): 
    x, y = [int(i) for i in input().split()]
    rab_coords.append((x, y))
for i in range(seats):
    x, y = [int(i) for i in input().split()]
    seat_coords.append((x, y))
    
if rabs==seats: 
    print(0)
else: 
    rabbit_tracker = list(range(rabs+1))
    
    def remove_min_from_tracker(sqr, rabbit_tracker): 
        index = 0
        minimum = min(sqr)
        while sqr.index(minimum)+1 not in rabbit_tracker: 
            maximum = max(sqr)
            sqr[sqr.index(minimum)] = maximum
            minimum = min(sqr)
            
        rabbit_tracker.remove(sqr.index(minimum)+1)
        return rabbit_tracker 
    
    for x1, y1 in seat_coords: 
        
        sqr = []
        for x2, y2 in rab_coords: 
            dist = (y2-y1)**2 + (x2-x1)**2
            sqr.append(dist)

        rabbit_tracker = remove_min_from_tracker(sqr, rabbit_tracker)
        
    for i in rabbit_tracker[1:]: 
        print(i)