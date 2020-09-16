from random import sample

def read_practice_file(file_name):
    practice_items = []
    with open(file_name) as practice_file:
        for line in practice_file:
            if not line.startswith('#') and not line.isspace():
                practice_items.append(line.strip())
    return practice_items

terms_header = "\n======== Search Terms ========\n"
permissions_header = "\n======== Permissions ========\n"
def get_output(practice_terms, practice_permissions):
    terms_output = get_sampled_output(practice_terms)
    permsissions_output = get_sampled_output(practice_permissions)
    return terms_header + terms_output + "\n" + permissions_header + permsissions_output

def get_sampled_output(items):
    sample = sample_items(items)
    return "\n".join(sample)

sample_size = 5
def sample_items(items):
    return sample(items, sample_size)


practice_terms = read_practice_file("searchTerms.txt")
practice_permissions = read_practice_file("permissions.txt")

output = get_output(practice_terms, practice_permissions)
print(output)