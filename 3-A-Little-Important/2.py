class TagCloud:
    def __init__(self):
        self.__tags = {}

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getItem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setItem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    # to make it iterable
    def __iter__(self):
        return iter(self.__tags)
        # iter obj returns one item at a time


cloud = TagCloud()
cloud.add("Python")
cloud.add("python")
cloud.add("python")
cloud.__setItem__("python", 10)
print(cloud.__tags)
print(len(cloud))
