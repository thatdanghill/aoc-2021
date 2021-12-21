import sys

Alg,_,*img_chars = open(sys.argv[1])

def char_to_bin(inp):
    return [char == '#' for char in inp]

Alg = char_to_bin(Alg[:-1])
img = [char_to_bin(img_row[:-1]) for img_row in img_chars]


def pad_img(image, default=False):
    row_len = len(image[0])
    new_img = []
    new_img.append([default for _ in range(row_len + 2)])
    for row in image:
        new_row = [default] + row + [default]
        new_img.append(new_row)
    new_img.append([default for _ in range(row_len + 2)])
    return new_img


def bool_list_to_bin_str(bool_list):
    return ''.join([str(int(i)) for i in bool_list])


def get_img_row(image, x, y, default=False):
    def_str = '1' if default else '0'
    if y < 0 or y >= len(image):
        return def_str*3
    if x == 0:
        return def_str + bool_list_to_bin_str(image[y][0:2])
    if x == len(image[0]) - 1:
        return bool_list_to_bin_str(image[y][-2:]) + def_str
    return bool_list_to_bin_str(image[y][x-1:x+2])


def get_image_bin_str(image, x, y, default=False):
    return (
            get_img_row(image, x, y-1, default) +
            get_img_row(image, x, y, default) +
            get_img_row(image, x, y + 1, default)
    )


def enhance(image, its):
    for it in range(its):
        new_img = []
        default = Alg[0] and (
                it % 2 == 1 or (Alg[-1] and it > 0))
        padded = pad_img(image, default)
        for y in range(len(padded)):
            new_row = []
            for x in range(len(padded[0])):
                binstr = get_image_bin_str(padded, x, y, default)
                new_row.append(Alg[int(binstr, 2)])
            new_img.append(new_row)
        image = new_img
    print_img(image)
    return image

def print_img(image):
    for row in image:
        print(''.join(['#' if i else '.' for i in row]))
    print()

en_2 = enhance(img, 2)
en_50 = enhance(img, 50)
print(sum([sum(row) for row in en_2]))
print(sum([sum(row) for row in en_50]))


