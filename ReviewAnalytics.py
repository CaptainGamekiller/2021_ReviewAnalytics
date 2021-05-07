# Calculate the average length of 1000000 reviews in Amazon website.
data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
print('Done! we got',len(data), 'reviews in this txt file.')

# Sum all reviews to get the total length.
sum_len = 0
for d in data:
    sum_len = sum_len + len(d)
print('Average length of all reviews is ', sum_len/len(data), '.')