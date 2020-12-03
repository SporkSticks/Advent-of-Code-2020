d2 = open("C:/Users/zstavrakas/Desktop/Advent of Code 2020/2015/Day2.1.txt", 'r')

content = d2.read().split('\n')

# PART 1
# Take dimensions of each right rectangular prism + area of smallest side --> find sum of all areas
def total_surface_area(box_list):
    total = 0

    for box in box_list:
        dimensions = sorted([int(b) for b in box.split('x')])      
        l, w, h = dimensions[0], dimensions[1], dimensions[2]
        
        total += 2*l*w + 2*w*h + 2*h*l + l*w

    return total

print(total_surface_area(content))

# PART 2
# Find the length of ribbon required to wrap all the boxes: the perimeter of the smallest face + the volume of the box

def total_ribbon(box_list):
    total = 0

    for box in box_list:
        dimensions = sorted([int(b) for b in box.split('x')])      
        l, w, h = dimensions[0], dimensions[1], dimensions[2]

        total += l*w*h + (l+l+w+w)

    return total

print(total_ribbon(["2x3x4"])) # should be 34
print(total_ribbon(content))