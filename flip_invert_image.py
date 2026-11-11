'''An image is a binary matrix of 0s and 1s.
To flip it horizontally, reverse each row.
To invert it, swap every 0 for 1 and every 1 for 0.
Return the image after flipping and then inverting, without modifying the input.'''


def flip_and_invert(image):
    flipped_image = []

    for row in image:
        new_row = []
        for i in range(len(image[0]) - 1, -1, -1):
            if row[i] == 0:
                element = 1
            elif row[i] == 1:
                element = 0
            new_row.append(element)
        flipped_image.append(new_row)

    return flipped_image


print(flip_and_invert([[1, 1, 0], [1, 0, 1], [0, 0, 0]]))
print(flip_and_invert([[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]))
print(flip_and_invert([[0]]))
print(flip_and_invert([[1]]))
print(flip_and_invert([[0, 1]]))
