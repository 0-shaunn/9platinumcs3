class Anime:
    def __init__(self, title: str, episodes: int, source: str, duration: float):
        self.title = title
        self.episodes = episodes
        self.source = source
        self.duration = duration
        self.__current_time = 0.0

    def get_current_time(self) -> float:
        return self.__current_time

    def play(self):
        print(f"Playing '{self.title}' from {self.__current_time}s.")

    def skipForward(self, seconds: float):
        self.__current_time += seconds
        print(f"Skipped forward {seconds}s in '{self.title}'. Position: {self.__current_time}s.")


# Inheritance: ShojoAnime IS-A Anime
class ShojoAnime(Anime):
    def __init__(self, title: str, episodes: int, source: str, duration: float, romance_subgenre: str):
        super().__init__(title, episodes, source, duration)
        self.romance_subgenre = romance_subgenre

    def shojo_info(self):
        print(f"Shojo Title: {self.title} | Subgenre: {self.romance_subgenre} | Episodes: {self.episodes}")


# Aggregation: StreamingService HAS-A list of Anime
class StreamingService:
    def __init__(self, name: str):
        self.name = name
        self.catalog = []  # Stores list of independent Anime object references

    def add_anime(self, anime: Anime):
        self.catalog.append(anime)
        print(f"Added '{anime.title}' to {self.name}.")

    def display_catalog(self):
        print(f"\n--- {self.name} Catalog ---")
        for anime in self.catalog:
            print(f"- {anime.title} ({anime.episodes} eps)")


if __name__ == "__main__":
    service = StreamingService("Crunchyroll")

    # Creating Anime objects independently
    anime1 = Anime("Haikyu!!", 85, "Manga", 24.0)
    shojo1 = ShojoAnime("Kimi ni Todoke", 38, "Manga", 23.0, "High School Romance")

    print("--- INHERITANCE ---")
    shojo1.shojo_info()
    shojo1.play()  # Inherited method
    shojo1.skipForward(120.0)  # Inherited method

    print("\n--- AGGREGATION ---")
    # Adding pre-existing objects into the catalog
    service.add_anime(anime1)
    service.add_anime(shojo1)
    service.display_catalog()
