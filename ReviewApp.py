#変数の定義
line    =   "\n--------------------------"

#関数の定義
def post_review():
    post    =   {}
    print("Input genre:")
    post["genre"]   =   input()
    print("Input title:")
    post["title"]   =   input()
    print("Input review:")
    post["review"]  =   input()
    
    # レビューを表示
    print("ジャンル : " + post["genre"] + line)
    print("タイトル : " + post["title"] + line)
    print("感想 :" + post["review"] + line)
    
    posts.append(post)
    
def read_reviwes():
    
    for (num,pos) in enumerate(posts):
        print("[num_" + str(num) + "]" + pos['title'])
        
    print("input number")
    num = int(input())
    
    post = posts[num]
    
    # レビューを表示
    print("ジャンル : " + post["genre"] + line)
    print("タイトル : " + post["title"] + line)
    print("感想 :" + post["review"] + line)
    

def end_program():
    exit()

def exception():
    print("error")

    
posts   =   []

#Top_action
while True:
    print("レビュー数：" + str(len(posts)) + "\n[0]レビューを書く\n[1]レビューを読む\n[2]アプリを終了する")
    print("Select and input num")
    num =   int(input())
    
    if num == 0:
        post_review()
    elif num == 1:
        read_reviwes()
    elif num == 2:
        end_program()
    else:
        exception()
    

