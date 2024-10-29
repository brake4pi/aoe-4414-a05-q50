# ray_ellipsoid_intersection.py
#
# Usage: python3 ray_ellipsoid_intersection.py d_l_x d_l_y d_l_z c_l_x c_l_y c_l_z
# Parameters:
# d_l_x: x-coordinate of origin-referenced ray unit vector
# d_l_y: y-coordinate of origin-referenced ray unit vector
# d_l_z: z-coordinate of origin-referenced ray unit vector
# c_l_x: x-coordinate of the ray origin offset
# c_l_y: y-coordinate of the ray origin offset
# c_l_z: z-coordinate of the ray origin offset
# Output:
# x,y, and z coordinates of the intersection if it exists 
#
# Written by Lee Wallenfang

# import Python modules
import math # math module
import sys # argv

# "constants"
R_E_KM = 6378.137
E_E = 0.081819221456

# initialize script arguments
d_l_x= float('nan')
d_l_y= float('nan')
d_l_z= float('nan')
c_l_x= float('nan')
c_l_y= float('nan')
c_l_z= float('nan')

# parse script arguments
if len(sys.argv)==7:
    d_l_x= float(sys.argv[1])
    d_l_y= float(sys.argv[2])
    d_l_z= float(sys.argv[3])
    c_l_x= float(sys.argv[4])
    c_l_y= float(sys.argv[5])
    c_l_z= float(sys.argv[6])
else:
    print(\
     'Usage: '\
     'python3 ray_ellipsoid_intersection.py d_l_x d_l_y d_l_z c_l_x c_l_y c_l_z'
   )
    exit()

# write script below this line

## setup vectors
d_l=[d_l_x, d_l_y,d_l_z]
c_l=[c_l_x, c_l_y,c_l_z]

## discriminant
a= d_l_x**2 + d_l_y**2 + (d_l_z**2/(1-(E_E**2)))
b= 2*(d_l_x*c_l_x + d_l_y*c_l_y + (d_l_z*c_l_z)/((1-(E_E**2))))
c= c_l_x**2 + c_l_y**2 + (c_l_z**2)/(1-(E_E**2)) - R_E_KM**2
discr=b*b-4.0*a*c

## solution logic
if discr>=0.0:
    d= (-b-math.sqrt(discr))/(2*a)
    if d<0.0:
        d= (-b+math.sqrt(discr))/(2*a)
    if d>= 0.0:
        l_d_x = d*d_l_x+c_l_x
        l_d_y = d*d_l_y+c_l_y
        l_d_z = d*d_l_z+c_l_z
        l_d = [l_d_x, l_d_y, l_d_z]
        print(l_d[0])
        print(l_d[1])
        print(l_d[2])