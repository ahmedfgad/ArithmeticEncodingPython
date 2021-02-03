import scipy.misc
import pyae
import numpy
import matplotlib.pyplot

# Change the precision to a bigger value
from decimal import getcontext
getcontext().prec = 10000

# Read an image.
im = scipy.misc.face(gray=True)

# Just work on a small part to save time. The larger the image, the more time consumed.
im = im[:50, :50]

# Convert the image into a 1D vector.
msg = im.flatten()

# Create the frequency table based on its hitogram.
hist, bin_edges = numpy.histogram(a=im,
                                  bins=range(0, 257))
frequency_table = {key: value for key, value in zip(bin_edges[0:256], hist)}

# Create an instance of the ArithmeticEncoding class.
AE = pyae.ArithmeticEncoding(frequency_table=frequency_table)

# Encode the message
encoded_msg, _ = AE.encode(msg=msg, 
                        probability_table=AE.probability_table)

# Decode the message
decoded_msg, _ = AE.decode(encoded_msg=encoded_msg, 
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
