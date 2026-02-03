apt1 = 850 #sqft
apt1_b1 = 12 * 14
apt1_b2 = 11 * 14
print(apt1, apt1_b1, apt1_b2)
print("apt 1 total communal space",
      apt1 - apt1_b1 - apt1_b2)

apt2 = 1190 # sqft
apt2_b1 = 13 * 14
apt2_b2 = 12 * 9
apt2_b3 = 15 * 9
apt2_b4 = 9 * 15
apt2_bedroom_total = apt2_b1 + apt2_b2 + apt2_b3 + apt2_b4
print("apt 2 total communal space",
      apt2 - apt2_bedroom_total)

# calculating bedroom proportion
apt1_total_bed = apt1_b1 + apt1_b2
print(apt1_total_bed / apt1)

print(apt2_bedroom_total / apt2)

# okay so what is our bedroom proportion?
print(apt1_b1 / apt1_total_bed)
print(apt1_b2 / apt1_total_bed)
# change these so we save the results
b1_bed_prop = apt1_b1 / apt1_total_bed
b2_bed_prop = apt1_b2 / apt1_total_bed

apt1_rent = 1300
# bed rent
print("$", apt1_rent * (apt1_total_bed / apt1))
bed_rent = apt1_rent * (apt1_total_bed / apt1)
## bed 1 proportional rent....
print("bedroom 1 rent", bed_rent * b1_bed_prop)
print("bedroom 2 rent", bed_rent * b2_bed_prop)
# communal rent
comm_rent = apt1_rent - bed_rent
print("communal half", comm_rent * .5)