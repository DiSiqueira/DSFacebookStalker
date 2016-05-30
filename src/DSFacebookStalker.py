

import facebook
import requests


access_token = 'CAACEdEose0cBAN3TBvIVsboForLbDa4vNFlodyAHp58CU4ZAdLjB7lZCiWZCDjBHkjiT2CSDrI1i3XYcMTVCyV5uZBM0mKCnWvStSZBfmPGeOfL4EeGOaKL3FHYhZA00cUReFtEzdrFZB3tXHfGNtZBMic5tm36O3AvsvW92NrM0cnJ0JXym7m1Wt3IZBVwLaDsHidMHNqc4FNgZDZD'
user1 = 'scota.marcela'
graph = facebook.GraphAPI(access_token)


def get_all(user_id,connection):
    result = graph.get_connections(user_id,connection)

    all = result['data']
    print(result['data'])

    while True:
        try:
            result = requests.get(result['paging']['next']).json()
            all = result['data'] + all

            print(result['data'])
        except KeyError:
            break

    return all


def get_me():
    profile = graph.get_object("me")
    return profile['id']


def get_my_friends():
    me = get_me()
    return get_all(me, "invitable_friends")


def get_all_photos(user_id):
    profile = graph.get_object(user_id)
    photos = graph.get_connections(profile['id'], 'photos')
    print(photos['data'])

print(get_my_friends())

#get_all_photos(user1)

# while True:
#     try:
#         [some_action(post=post) for post in posts['data']]
#         # Attempt to make a request to the next page of data, if it exists.
#         posts = requests.get(posts['paging']['next']).json()
#     except KeyError:
#         # When there are no more pages (['paging']['next']), break from the
#         # loop and end the script.
#         break