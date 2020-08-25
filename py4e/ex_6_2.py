text = "X-DSPAM-Confidence:    0.8475";

pos = text.find('0')
float_value = text[pos:pos+6]
float_value = float(float_value)
print(float_value)
