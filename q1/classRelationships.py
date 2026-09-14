 Anime:
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


class StreamingService:
    def __init__(self, name: str):
        self.name = name
        self.catalog = []

    def add_anime(self, anime: Anime):
        self.catalog.append(anime)
        print(f"Added '{anime.title}' to {self.name}.")

    def display_catalog(self):
        print(f"\n--- {self.name} Catalog ---")
        for anime in self.catalog:
            print(f"- {anime.title} ({anime.episodes} eps)")


if __name__ == "__main__":
    service = StreamingService("Crunchyroll")

    anime1 = Anime("Haikyu!!", 85, "Manga", 24.0)
    anime2 = Anime("Jujutsu Kaisen", 47, "Manga", 23.5)
    anime3 = Anime("Demon Slayer", 55, "Manga", 23.0)

    print("--- BEFORE ---")
    service.display_catalog()
    print("Catalog is Empty")

    print("\n--- BUILDING RELATIONSHIP ---")
    service.add_anime(anime1)
    service.add_anime(anime2)
    service.add_anime(anime3)

    print("\n--- AFTER ---")
    service.display_catalog()

    print("\n--- ACCESSING DATA ---")
    service.catalog[0].play()
    service.catalog[0].skipForward(120.0)
