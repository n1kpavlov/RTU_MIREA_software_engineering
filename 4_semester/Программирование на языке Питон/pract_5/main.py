import	re

#1
print("#1")
text = "Contact us at support@example.com or sales@example.org for more info."
emails = re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', text)
print(emails)


#2
print("#2")
text = "You can reach us at +7 (912) 345-67-89 or +7 (901) 234-56-78 during business hours."
emails = re.findall(r'[+]7 [(]\d{3}[)] \d{3}-\d{2}-\d{2}', text)
print(emails)

#3
print("#3")
text = "Join the discussion on #python and share your thoughts on #regex. Don't forget to tag #coding!"
emails = re.findall(r'#\w+', text)
print(emails)

#4
print("#4")
text = "Visit our website at https://example.com or check out http://test.org for more details."
emails = re.findall(r'https?://\w+\.\w+', text)
print(emails)

#5
print("#5")
text = "The total cost is 150 dollars, but you can get a discount of 25 if you buy 3 items."
emails = re.findall(r'\d+', text)
print(emails)

#6
print("#6")
text = "The project deadline is 15/10/2023, and the final review will be on 20/12/2023."
emails = re.findall(r'(?:3[0-1]|[1-2]?\d)/(?:1?\d)/(?:\d{4})', text)
print(emails)

#7
print("#7")
text = "Python is a popular	programming	language. Learn	Regex to improve your Skills."
emails = re.findall(r'[A-Z][a-z]+', text)
print(emails)

#8
print("#8")
text = "The server IPs are 192.168.1.1, 10.0.0.1, and 8.8.8.8. Avoid using invalid IPs like 999.999.999.999."
emails = re.findall(r'(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\.(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\.(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\.(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)', text)
print(emails)

#9
print("#9")
text = "The meeting starts at 14:30 and ends at 16:45. Please arrive by 14:15."
emails = re.findall(r'(?:[01]?[0-9]|2[0-3]):[0-5][0-9]', text)
print(emails)

#10
print("#10")
text = "She is singing and dancing while cooking dinner. The evening is full of fun activities."
emails = re.findall(r'\w+ing\b', text)
print(emails)

#5.2
print("#5.2")
def decode_val(bits):
    decoded_bits = []
    for i in range(0, len(bits), 3):
        triplet = bits[i:i+3]
        if len(triplet) == 3:
            if triplet.count('1') > triplet.count('0'):
                decoded_bits.append('1')
            else:
                decoded_bits.append('0')
    return ''.join(decoded_bits)

def binary_to_char(binary_str):
    return chr(int(binary_str, 2))

def decode_message(encoded_message):
    decoded_message = ""
    for number in encoded_message:
        binary_str = bin(number)[2:].zfill(24)
        decoded_bits = decode_val(binary_str)
        for i in range(0, len(decoded_bits), 8):
            byte = decoded_bits[i:i+8]
            if len(byte) == 8:
                decoded_message += binary_to_char(byte)
    return decoded_message

encoded_message = [815608, 2064837, 2093080, 2063879, 196608, 2067983, 10457031, 1830912,
                   2067455, 2093116, 1044928, 2064407, 6262776, 2027968, 4423680, 2068231,
                   2068474, 1999352, 1019903, 2093113, 2068439, 2064455, 1831360, 1936903,
                   2067967, 2068456]
decoded_message = decode_message(encoded_message)
print(decoded_message)