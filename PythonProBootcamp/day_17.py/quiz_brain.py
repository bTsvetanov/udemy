class Brain:
    def __init__(self,q_B):
        self.question_num = 0
        self.question_bank = q_B
        self.guees_right = 0

    def still_has_q(self):
        return self.question_num<len(self.question_bank)
    
    def next_question(self):
        current_question = self.question_bank[self.question_num]
        self.question_num += 1
        answer = input(f"Q.{self.question_num}:{current_question.text} True/False:")
        self.check_answer(answer,current_question.answer)   
       
        
            
    def check_answer(self,answer,right_answer):
        if answer == right_answer:
             print(f"You got it right! It was: {right_answer}")
             self.guees_right+=1
        else:
            print(f"Wrong !It was: {right_answer}")
        print(f"{self.guees_right}/{self.question_num}\n")







