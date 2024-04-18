from rembg import remove

input_path = 'Sample.png'
output_path = 'Sample2.png'

with open(input_path, 'rb') as i:
    with open(output_path, 'wb') as o:
        input = i.read()
        output = remove(input)
        o.write(output)