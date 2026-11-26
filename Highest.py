# # # # highest = None

# # # # for i in [8,9,5,3,2]:
# # # #     if highest is None:
# # # #         highest = i
# # # #     else:
# # # #         if i > highest:
# # # #             highest = i
# # # # print(highest)

# # # seen = set()
# # # seen.add(1)
# # # seen.add(3)

# # # print(seen)


# # # The function below is supposed to take a list of posts (each with a list of tags) and return the set of every distinct tag used across all of them. It has a bug — find it and fix it.

# # # Requirements

# # #     Function name: all_unique_tags (do not rename it)
# # #     Takes one parameter: posts, a list of dictionaries, each shaped like {"title": string, "tags": list of strings}
# # #     Returns a set containing every distinct tag used across all posts
# # #     If posts is empty, return an empty set

# # # def all_unique_tags(posts):
# # #     unique_tags = {}
    
# # #     if not posts:
# # #         return set()
    
# # #     for post in posts:
# # #         unique_tags.update(post["tags"])
# # #     return unique_tags
# # # print(all_unique_tags([{"title": "A", "tags": []}]))
    
# # username = "Victor"
# # password = 12345

# # print("======================BANKING APP=========================")

# # user_input= input("Enter logins: ")
# # password = int(input("Enter password: "))

# # if user_input != username:
# #     print("Invalid username")
# #     break




# # def has_all_vowels(word: str):
# #     required_vowels = {'a', 'e', 'i', 'o', 'u'}
# #     lowercase_word = word.lower()
# #     found_characters = set(lowercase_word)
# #     vowels_in_word = found_characters.intersection(required_vowels)
# #     return vowels_in_word == required_vowels
# # print(has_all_vowels("education"))

# # def has_all_vowels(word: bool):
# #     return {'a', 'e', 'i', 'o', 'u'}.issubset(word.lower())
# # print(has_all_vowels("education"))

# # fruits = ["Mango", "Apple", "Kiwi", "Pineapple"]

# # new_list = []

# # for fruit in fruits:
# #         new_list.append(fruit)
# # print(new_list)
        
# # newlist = [x for x in range(10)]
# # print(newlist)

# # fruits = ["apple", "banana", "orange"]
# # print(fruits.reverse())

# student = {
#     "name": "Ada",
#     "age": 20,
#     "class": "Python"
# }
# print(student.keys())

Student = ["Maxwell", "Fred", "Ifeanyi"]
print(Student[0])
Student[0] = "Victor"