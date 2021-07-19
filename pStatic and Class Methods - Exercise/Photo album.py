class PhotoAlbum:

    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count):
        pages = photos_count // 4
        return cls(pages)

    def add_photo(self, label):
        for i in range(len(self.photos)):
            page = self.photos[i]
            if len(page) < 4:
                slot = len(page)
                self.photos[i].append(label)
                return f"{label} photo added successfully on page {i+1} slot {slot+1}"
        return "No more free slots"

    def display(self):
        result = [11 * "-"]
        for page in self.photos:
            photos = ' '.join(["[]"] * len(page))
            result.append(photos)
            result.append(11 * "-")
        result = '\n'.join(result)
        return result


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
