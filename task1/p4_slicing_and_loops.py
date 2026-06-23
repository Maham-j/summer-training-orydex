"""
Task 1 — Slicing and Loops

Practice slicing, loops, enumerate, zip, and comprehensions.
Complete this file without using AI tools.
"""

patient_ids = [101, 102, 103, 104, 105, 106, 107]
patient_names = ["Ayesha", "Omar", "Sara", "Bilal", "Hina", "Usman", "Maha"]


def slicing_examples():
    """Return examples of list slicing."""
    # TODO: Return first three IDs, last three IDs, and reversed IDs.
    first = patient_ids[0:3]
    last = patient_ids[-3:]
    reverse = patient_ids[::-1]

    return (first, last, reverse)
    
 



def loop_examples():
    """Practice range, enumerate, and zip."""
    # TODO: Use enumerate to print numbered patient names.
    # TODO: Use zip to pair IDs with names.
    for i,name in enumerate(patient_names):
        print(i,name)
    
    for i,name in zip(patient_ids, patient_names):
        print(i,name)


def comprehension_examples():
    """Return values created using comprehensions."""
    # TODO: Create a list of even patient IDs.
    # TODO: Create uppercase patient names.
    even = [ids for ids in patient_ids if ids%2==0]
    upper = [names.upper() for names in patient_names]
    
    return (even, upper)


if __name__ == "__main__":
    slicing_examples()
    loop_examples()
    comprehension_examples()
