# Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
# Use the file name mbox-short.txt as the file name


fname = input("Enter file name: ")
fh = open(fname)
avg = 0;
count = 0
float_value = 0.0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    #print(line)
    count = count + 1
    pos = line.find('0')
    float_value = line[pos:]
    float_value = float(float_value)
    #print(float_value)
    avg = avg + float_value
#print("Done")
#print(count)
avg = avg / count
print("Average spam confidence:", avg)
