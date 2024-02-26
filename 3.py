class Member:

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def display(self):
        print(f"회원 이름 : {self.name} , 회원 아이디 : {self.username} \n")


class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author


members = []
posts = []
i = 0
print("회원 인스턴스를 3개 이상 만드세요.\n")
while True:
    i += 1
    print(f"{i}번째 회원 정보를 입력해주세요.\n")
    a = input("회원 이름 : ")
    b = input("\n회원 아이디 설정 : ")
    c = input("\nPassword 설정 : ")
    d = input(f"\n{i}번째 회원을 위 정보로 회원가입합니다. (y/n)\n")
    e = "0"

    # 여기는 멤버추가 조건도 달아놨음 3명이상일때 그만 만들수있게
    if d == "y":
        members.append(Member(a, b, c))
    else:
        i -= 1
        print("회원가입 초기설정으로 이동 \n")

    if i >= 3:
        e = input("그만 만드시겠습니까? (y/n)")
    if e == "y":
        break

print("\n 회원들의 이름 : ")
for member in members:
    # print(member.name)
    member.display()
i = 0
j = 0

print("각 회원당 3개 이상 post를 작성하세요. \n")
while True:
    i += 1
    while True:
        j += 1
        print(f"{i}회원의 {j}번째 post 작성\n")
        a = input("제목 : ")
        b = input("\n내용 : ")
        c = members[i-1].username
        print(f"\n{i}번째의 아이디 : ", c)
        d = input("\n위 정보로 post 작성합니다. (y/n)\n")
        e = "0"
        if d == "y":
            posts.append(Post(a, b, c))
        else:
            j -= 1
            print("post 작성 초기설정으로 이동 \n")
        if j >= 3:
            e = input("그만 만드시겠습니까? (y/n)\n")
        if e == "y":
            j = 0
            break
    if i == len(members):
        break

print("\n특정유저가 작성한 게시글의 제목을 프린트 해주세요. ")
user = input("\n검색할 유저아이디 : ")
print(f"\n{user}의 작성한 글 제목 : ")

for post in posts:
    if post.author == user:
        print(f"\n{post.title} ")


word = input("\n특정 단어 검색 : ")
print("\n특정 단어가 포함된 게시글의 제목 : ")
for post in posts:
    if word in post.content:
        print(post.title)
