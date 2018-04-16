#!/usr/bin/python
import urllib.request as ur
import urllib.error
import json
from collections import defaultdict
from geopy import distance


def get_closest_neighbor(name, lat, lon, users):
    neighbor = ""
    min_dist = 25000
    for user in users:
        try:
            user_lat = float(user["address"]["geo"]["lat"])
            user_lon = float(user["address"]["geo"]["lng"])
            dist = distance.distance((lat, lon), (user_lat, user_lon))
            if dist < min_dist and user["username"] != name:
                min_dist = dist
                neighbor = user["username"]
        except (KeyError, ValueError):
            continue
    return neighbor


def get_user_posts(users, posts):
    posts_per_user = {}
    user_names = {}
    res_array = []
    try:
        for user in users:
            posts_per_user[user["id"]] = 0
            user_names[user["id"]] = user["username"]
        for post in posts:
            posts_per_user[post["userId"]] += 1
        for k, v in posts_per_user.items():
            res_array.append("User " + user_names[k] + " napisal " + str(v) + " postow.")
    except KeyError as e:
        print("Couldn't get user posts. No value for key " + str(e))
    return res_array


def get_duplicate_posts(posts):
    posts_count = defaultdict(int)
    res_array = []
    try:
        for post in posts:
            posts_count[post["title"]] += 1
            if posts_count[post["title"]] > 1:
                res_array.append(post["title"])
    except KeyError as e:
        print("Can't get info about duplicate titles. No value for key " + str(e))
    return res_array


def get_distances(users):
    shortest_distances = {}
    try:
        for user in users:
            lon = float(user["address"]["geo"]["lng"])
            lat = float(user["address"]["geo"]["lat"])
            name = user["username"]
            shortest_distances[name] = get_closest_neighbor(name, lat, lon, users)
    except KeyError as e:
        print("Couldn't check distances for users. No value for key " + str(e))
    return shortest_distances


def main():
    try:
        with ur.urlopen("https://jsonplaceholder.typicode.com/posts") as posts_url,\
                ur.urlopen("https://jsonplaceholder.typicode.com/users") as users_url:
            posts_json = json.loads(posts_url.read().decode())
            users_json = json.loads(users_url.read().decode())
    except (urllib.error.URLError, ValueError):
        print("Cannot download or decode JSON")
    else:
        print("\n".join(get_user_posts(users_json, posts_json)))
        print("---------------------")
        print("Duplicates: ")
        print(get_duplicate_posts(posts_json))
        print("---------------------")
        print("Closest living neighbors: ")
        distances = get_distances(users_json)
        for k, v in distances.items():
            print(k + " lives the closest to " + v)


if __name__ == "__main__":
    main()
