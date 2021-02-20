import pyae
# from decimal import getcontext

# Example for encoding a simple text message using the PyAE module.

# Create the frequency table.
frequency_table = {"a": 2,
                   "b": 3,
                   "c": 1,
                   "d": 4}

# Create an instance of the ArithmeticEncoding class.
AE = pyae.ArithmeticEncoding(frequency_table, 
                             save_stages=True)

# Default precision is 28. Change it to do arithmetic operations with larger/smaller numbers.
# getcontext().prec = 28

original_msg = "bdab"
print("Original Message: {msg}".format(msg=original_msg))

# Encode the message
encoded_msg, encoder , interval_min_value, interval_max_value = AE.encode(msg=original_msg, 
                                                                          probability_table=AE.probability_table)
print("Encoded Message: {msg}".format(msg=encoded_msg))

# Decode the message
decoded_msg, decoder = AE.decode(encoded_msg=encoded_msg, 
                                 msg_length=len(original_msg),
                                 probability_table=AE.probability_table)
print("Decoded Message: {msg}".format(msg=decoded_msg))

decoded_msg = "".join(decoded_msg)
print("Message Decoded Successfully? {result}".format(result=original_msg == decoded_msg))
