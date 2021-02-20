import scipy.misc
import pyae
import numpy
import matplotlib.pyplot

# Example for encoding an image using the PyAE module.
# This example returns the floating-point value in addition to its binary code that encodes the image. 

# Change the precision to a bigger value
from decimal import getcontext
getcontext().prec = 444

# Read an image.
im = scipy.misc.face(gray=True)

# Just work on a small part to save time. The larger the image, the more time consumed.
im = im[:15, :15]

# Convert the image into a 1D vector.
msg = im.flatten()

# Create the frequency table based on its hitogram.
hist, bin_edges = numpy.histogram(a=im,
                                  bins=range(0, 257))
frequency_table = {key: value for key, value in zip(bin_edges[0:256], hist)}

# Create an instance of the ArithmeticEncoding class.
AE = pyae.ArithmeticEncoding(frequency_table=frequency_table, save_stages=True)

# Encode the message
encoded_msg, encoder, interval_min_value, interval_max_value = AE.encode(msg=msg, 
                                                                         probability_table=AE.probability_table)

# Get the binary code that encodes the image
binary_code, encoder_binary = AE.encode_binary(float_interval_min=interval_min_value,
                                               float_interval_max=interval_max_value)
print("The binary code is: {binary_code}".format(binary_code=binary_code))

# Decode the message
decoded_msg, decoder = AE.decode(encoded_msg=encoded_msg, 
                                 msg_length=len(msg),
                                 probability_table=AE.probability_table)

# Reshape the image to its original shape.
decoded_msg = numpy.reshape(decoded_msg, im.shape)

# Show the original and decoded images.
fig, ax = matplotlib.pyplot.subplots(1, 2)
ax[0].imshow(im, cmap="gray")
ax[0].set_title("Original Image")
ax[0].set_xticks([])
ax[0].set_yticks([])
ax[1].imshow(decoded_msg, cmap="gray")
ax[1].set_title("Reconstructed Image")
ax[1].set_xticks([])
ax[1].set_yticks([])
