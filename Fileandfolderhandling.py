read=open("util.txt","r")
print(read)
print(read.mode)
print(read.readable())
print(read.closed)
user=open('user.txt',"w")
user.write("hello")
print(user)
users_list = open("users.txt", "w")
# friends = ["Jordan", "Alex", "Michel", "HuXn"]
friends = ["Jordan\n", "Alex\n", "Michel\n", "HuXn\n"]
users_list.writelines(friends)
users_list.close()