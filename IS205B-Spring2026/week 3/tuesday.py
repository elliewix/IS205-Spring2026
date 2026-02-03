# apt 1 details
apt1 = 1000 # sqft
apt1_rent = 1500 # $
apt1_b1 = 12 * 14
apt1_b2 = 11 * 14

# apt 2 details

apt2 = 1190 # sqft
apt2_b1 = 13 * 14
apt2_b2 = 12 * 9
apt2_b3 = 15 * 9
apt2_b4 = 9 * 15

# start calculating b1

# print(apt1_b1 + apt1_b2)
# total bedroom size
apt1_total_bed = apt1_b1 + apt1_b2
print(apt1_total_bed)
# total communal space
apt1_total_comm = apt1 - apt1_total_bed
print(apt1_total_bed, apt1_total_comm)

# calculate for apt2

apt2_total_bed = apt2_b1 + apt2_b2 + apt2_b3 + apt2_b4
apt2_total_comm = apt2 - apt2_total_bed

print(apt2_total_bed, apt2_total_comm)

# let's calculate some proportions
# for apt 1
print(apt1_b1, apt1_b2)
apt1_b1_prop = apt1_b1 / apt1_total_bed
print(apt1_b1_prop)
# print(apt1_rent * apt1_b1_prop)
apt1_b1_rent = apt1_rent * apt1_b1_prop
print(apt1_b1_rent, (apt1_rent - apt1_b1_rent))

#### calculate the total cost of the bedrooms together

# 1) calculate the proportion of bedrooms to total size
# print(apt1_total_bed / apt1)
apt1_bed_prop = apt1_total_bed / apt1
# 2) calculate that actual cost
# print("$", apt1_rent * apt1_bed_prop)
apt1_bed_cost = apt1_rent * apt1_bed_prop
print(apt1_bed_cost)
#3) communal space
print(apt1_rent - apt1_bed_cost)