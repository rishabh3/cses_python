def solve():
    n = int(input())
    movies = []

    for _ in range(n):
        movie = tuple(map(int, input().split(' ')))
        movies.append(movie)

    movies.sort(key=lambda x: x[-1])

    movie_count = 1
    top = movies[0]

    for idx in range(1, n):
        if movies[idx][0] < top[-1]:
            continue
        movie_count += 1
        top = movies[idx]
    
    print(movie_count)


if __name__ == "__main__":
    solve()