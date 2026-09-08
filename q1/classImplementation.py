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

    def pause(self):
        print(f"Paused '{self.title}' at {self.__current_time}s.")

    def skipForward(self, seconds: float):
        max_duration_seconds = self.duration * 60
        if self.__current_time + seconds <= max_duration_seconds:
            self.__current_time += seconds
            print(f"Skipped forward {seconds}s in '{self.title}'. Current position: {self.__current_time}s.")
        else:
            self.__current_time = max_duration_seconds
            print(f"Reached end of episode for '{self.title}'. Position set to max ({self.__current_time}s).")

    def skipBackward(self, seconds: float):
        if self.__current_time - seconds >= 0:
            self.__current_time -= seconds
            print(f"Skipped backward {seconds}s in '{self.title}'. Current position: {self.__current_time}s.")
        else:
            self.__current_time = 0.0
            print(f"Rewound to start for '{self.title}'. Position set to 0.0s.")


if __name__ == "__main__":
    anime1 = Anime("Haikyu!!", 85, "Manga", 24.0)
    anime2 = Anime("Jujutsu Kaisen", 47, "Manga", 23.5)

    print("--- BEFORE ---")
    print(f"Anime 1 ({anime1.title}) Current Time: {anime1.get_current_time()}s")
    print(f"Anime 2 ({anime2.title}) Current Time: {anime2.get_current_time()}s")

    print("\n--- PERFORMING ACTION ON OBJECT 1 ONLY ---")
    anime1.play()
    anime1.skipForward(120.0)

    print("\n--- AFTER ---")
    print(f"Anime 1 ({anime1.title}) Current Time: {anime1.get_current_time()}s")
    print(f"Anime 2 ({anime2.title}) Current Time: {anime2.get_current_time()}s")
