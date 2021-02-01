import json


class Movie:
    '''
        This class for just create a Movie or any genre you would
        like to create
    '''
    genres = ["film", "series"]
    styles = ["action", "comedy", "drama", "romantic", "fictional"]

    def __init__(self,
                 genre=input("type your genre %s: " % genres),
                 style=input("style of movie %s: " % styles),
                 name=input("name of movie: "),
                 count_letters=input("define the count of movie: "),
                 author=input("who is actor of the movie? [you can leave it empty]\n"),
                 about=input("type short story about it. [you can leave it empty]\n")):
        self.genre = genre.lower()
        self.style = style.lower()
        self.name = name.lower()
        self.count_letters = count_letters
        self.author = author
        self.about = about

    def genre_func(self):
        if self.genre not in self.genres:
            raise Exception("Type have to be one of this list %s" % self.genres)
        elif self.genre == '':
            raise Exception("genre cannot be empty field it's required")
        return self.genre

    def style_func(self):
        if self.style not in self.styles:
            raise Exception("Style have to be one of this list %s" % self.styles)
        elif self.style == '':
            raise Exception("style cannot be empty field it's required")
        return self.style

    def counts(self):
        if int(self.count_letters) != len(self.name):
            raise Exception("ensure for your counts, [don't forget to count hyphens or apostrophe and etc...]")
        elif self.count_letters == '':
            raise Exception("counts cannot be empty field it's required")
        return self.count_letters


class Validation(Movie):
    '''
        verify your fields before handle it,
        then save it.
    '''

    def __init__(self, *args):
        super().__init__(*args)
        self.valid = False

    # verify from data
    def validation_obejct(self):
        obj = Movie(
            genre=self.genre_func(),
            style=self.style_func(),
            name=self.name,
            count_letters=self.counts(),
            author=self.author or None,
            about=self.about or None
        )

        if obj:
            self.valid = True
        else:
            raise Exception("Invalid Form")
        return obj

    # don't save film if name of film is exist
    def unique_object(self):
        obj = self.validation_obejct()
        with open("film.json", "r") as fp_unique:
            all_data = json.load(fp_unique)
            for data in all_data["data"]:
                if obj.name == data["name"]:
                    self.valid = False
                    raise Exception("the %s movie is already exists" % obj.name)
                else:
                    return obj
        return obj

    def save(self, **origin_data):
        obj = self.unique_object()

        if self.valid:
            try:
                fp_read = open("film.json", "r", encoding="utf8")
                json_data = json.load(fp_read)
                json_data["data"].append({
                    "genre": obj.genre,
                    "style": obj.style,
                    "name": obj.name,
                    "count_letters": obj.count_letters,
                    "author": obj.author,
                    "about": obj.about
                })
                fp_write = open("film.json", "w", encoding="utf8")
                json.dump(json_data, fp_write, indent=4)
            except:
                # data format if JSON file is empty
                fp_write = open("film.json", "w", encoding="utf8")
                arr = []
                all_data = {
                            "genre": obj.genre,
                            "style": obj.style,
                            "name": obj.name,
                            "count_letters": obj.count_letters,
                            "author": obj.author,
                            "about": obj.about
                        }
                arr.append(all_data)
                origin_data["data"] = arr
                json.dump(origin_data, fp_write, indent=4)

        return origin_data


if __name__ == "__main__":
    v = Validation()
    v.save()
