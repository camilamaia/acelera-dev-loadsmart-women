def is_underage(age):
    # debug with python shell: import pdb; pdb.set_trace()
    # debug with ipython shell: import ipdb; ipdb.set_trace()
    if age < 0:
        return 'Invalid age, it only accepts positive numbers'

    return age < 18
