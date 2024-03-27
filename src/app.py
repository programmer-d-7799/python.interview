from pydantic import BaseModel
import heapq


class HeapNode:
    content_id: int
    popularity: int

    def __init__(self, content_id: int, popualrity: int) -> None:
        self.content_id = content_id
        self.popularity = popualrity

    def __eq__(self, __value: object) -> bool:
        return self.popularity == __value.popularity

    def __lt__(self, __value: object) -> bool:
        return self.popularity < __value.popularity


class MostPopular:

    def __init__(self):
        # self.min_heap = heapq.heapify([])
        self.min_heap = []
        self.content_dict = {}

    def increase_popularity(self, content_id: int) -> None:
        if not isinstance(content_id, int) or content_id < 1:
            raise ValueError

        if content_id in self.content_dict:
            content = self.content_dict[content_id]
            content.popularity += 1

        else:
            content = HeapNode(content_id, 1)
            self.content_dict[content_id] = content
            heapq.heappush(self.min_heap, content)

    def most_popular(self) -> int:
        if len(self.content_dict) < 1:
            return -1

        result = heapq.nlargest(1, self.min_heap, key=lambda x: x.popularity)
        return result[0].content_id

    def decrease_popularity(self, content_id: int) -> None:
        if content_id in self.content_dict:
            content = self.content_dict[content_id]
            content.popularity -= 1
            if content.popularity == 0:
                del self.content_dict[content_id]

        else:
            raise ValueError("not in here")


if __name__ == "__main__":
    popularityTracker = MostPopular()

    popularityTracker.increase_popularity(7)
    popularityTracker.increase_popularity(7)
    popularityTracker.increase_popularity(8)
    result = popularityTracker.most_popular()
    # // returns 7
    popularityTracker.increase_popularity(8)
    popularityTracker.increase_popularity(8)
    result = popularityTracker.most_popular()
    # // returns 8
    popularityTracker.decrease_popularity(8)
    popularityTracker.decrease_popularity(8)
    result = popularityTracker.most_popular()
    # // returns 7
    popularityTracker.decrease_popularity(7)
    popularityTracker.decrease_popularity(7)
    popularityTracker.decrease_popularity(8)
    result = popularityTracker.most_popular()
    # // returns -1 since there is no content with popularity greater than 0
