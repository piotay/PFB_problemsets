taxa_string = 'sapiens : erectus : neanderthalensis'
print(taxa_string)

taxa_list = taxa_string.split(" : ")

print(taxa_list)

print(taxa_list[1])

print(type(taxa_string))

print(type(taxa_list))

print(sorted(taxa_list))

print(sorted(taxa_list, key = len))

