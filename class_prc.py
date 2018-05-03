class Review:
    @classmethod
    def get_review_count(cls):
        return 0
        
    def write_review(self):
        print("タイトルを入力してください")
        self.title = input()
        print("ジャンルを入力してください")
        self.genre = input()
        print("感想を入力してください")
        self.impression = input()
    
    def show_review(self):
        line = "\n---------------------------"
        print("ジャンル : " + self.genre + line)
        print("タイトル : " + self.title + line)
        print("感想 : " + self.impression + line)

review = Review()
review = Review()
review.show_review()
print(Review.get_review_count())