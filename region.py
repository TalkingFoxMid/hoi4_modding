from countries_list import Countries


class Region:
    def __init__(self, default_owner):
        self.owner = Countries.Free
        self.default_owner = default_owner
