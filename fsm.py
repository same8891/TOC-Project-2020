from transitions.extensions import GraphMachine

from utils import send_text_message


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    
    def is_going_to_q1(self, event):
        text = event.message.text
        return text.lower() == "start"

    def is_going_to_q2_yes(self, event):
        text = event.message.text
        return text.lower() == "yes"
    
    def is_going_to_q4_yes(self, event):
        text = event.message.text
        return text.lower() == "yes"
    def is_going_to_q4_no(self, event):
        text = event.message.text
        return text.lower() == "no"
    def is_going_to_q3_no(self, event):
        text = event.message.text
        return text.lower() == "no"
    def is_going_to_q3_yes(self, event):
        text = event.message.text
        return text.lower() == "yes"
    def is_going_to_q5_no(self, event):
        text = event.message.text
        return text.lower() == "no"
    def is_going_to_a_yes(self, event):
        text = event.message.text
        return text.lower() == "yes"
    def is_going_to_b_no(self, event):
        text = event.message.text
        return text.lower() == "no"
    def is_going_to_c_yes(self, event):
        text = event.message.text
        return text.lower() == "yes"
    def is_going_to_d_no(self, event):
        text = event.message.text
        return text.lower() == "no"
    def on_enter_restart(self, event):
        print("I'm entering restart")
        reply_token = event.reply_token
        send_text_message(reply_token, "enter start to restart")   
    def on_enter_q3(self, event):
        print("I'm entering state3")
        reply_token = event.reply_token
        send_text_message(reply_token, "你能夠說出五位小學同班 同學的姓名，並記得他們的長相？\nenter yes or no")
    def on_enter_q1(self, event):
        print("I'm entering state1")
        reply_token = event.reply_token
        send_text_message(reply_token, "去年至少看過一次美術展覽，家中書櫃裏至少有一本和美術相關的書籍？\nenter yes or no")
    def on_exit_q1(self,event):
        print("Leaving state1")
    def on_exit_q3(self,event):
        print("Leaving state3")
    def on_enter_q2(self, event):
        print("I'm entering state2")
        reply_token = event.reply_token
        send_text_message(reply_token, "你的地理國文成績比數學理化好？\nenter yes or no")
    def on_enter_q4(self, event):
        print("I'm entering state4")
        reply_token = event.reply_token
        send_text_message(reply_token, "朋友裏有學美術或是相關領域的人？\nenter yes or no")
    def on_enter_a(self, event):
        print("I'm entering a")
        reply_token = event.reply_token
        send_text_message(reply_token, "Ａ　性格基因\n你是自視甚高的天才型人物，口才好，頭腦清楚，性格犀利，具備良好的\n洞察能力，為人理性且深懂分寸拿捏，與外界維持一定的關係。儘管有時會因\n為情緒因素而顯得熱絡，但大半時間都是過著一個人的生活，外人很難貼近你\n的內心世界。擅長隱藏情緒的你，不容易相信他人，寧可孤獨一人也不願冒\n險，理想主義色彩濃厚，對於金錢不太關注，對你來說，出名或是獲得認可比\n中彩券頭獎還重要。\n生命路線\n你需要學習生命的彈性，藉由他人的視野來看這個世界。一廂情願或是孤\n注一擲都不能讓你有所獲得，若不想老是和機會擦身而過，就要以務實態度過\n日子，任性而為是要付出代價。高處不勝寒的滋味你嘗過，隨著年齡漸長，你\n將會越來越孤獨。")
        self.go_back()
    def on_enter_q5(self, event):
        print("I'm entering q5")
        reply_token = event.reply_token
        send_text_message(reply_token, "你曾經組過樂團，或是參與過任何與美術音樂有關的表演活動？\nenter yes or no")
    def on_enter_b(self, event):
        print("I'm entering b")
        reply_token = event.reply_token
        send_text_message(reply_token, "Ｂ　性格基因\n你有獨特的人生觀，不喜歡隨波逐流、人云亦云，但若脫離團體又會感到\n不安和害怕。終其一生你都在鐘擺的兩端矛盾掙扎，因為拿不定主意，經常在\n機會降臨時猶豫不定，因此經常錯失良機或是誤判情勢。\n生命路線\n不甘寂寞又不願意妥協的個性，是你這輩子的痛苦來源。雖然你聰明伶\n俐、反應敏捷，卻經常在狀況外，很難融入群體的現實，搖擺不定且難以安定\n下來，工作、愛情和人際關係都很難穩定發展。學著為自己的決定負責，調適\n生活腳步，是將生活導向正軌的一個方式。")
        self.go_back()
    def on_enter_c(self, event):
        print("I'm entering c")
        reply_token = event.reply_token
        send_text_message(reply_token, "Ｃ　性格基因\n高更型的男女情緒喜怒無常，腦子裏經常打轉著古怪想法，表面上和團體\n融成一片，事實上只是你的保護色。你的存在是個活問號，別說他人很難真正\n了解你，連你自己也不能百分之百的掌控自己。你喜歡冒險、挑戰、變化，對\n於不正常或是特異的人事物最感興趣。\n生命路線\n尊重對自己和他人的承諾，是讓生活「正常化」的第一步。習慣主導和獨\n角戲的你，有時候也得讓別人有表現的機會。感情生活是你最難以駕馭的課\n題。你經常挑選難題，討厭容易到手的機會，這樣的傾向一直將你推向不可知\n的危險邊緣。對於事物容易感到厭惡，儘管興趣廣泛卻難以專精，中年之後，\n得面對走了一圈卻毫無具體建樹的生活。")
        self.go_back()
    def on_enter_d(self, event):
        print("I'm entering d")
        reply_token = event.reply_token
        send_text_message(reply_token, "Ｄ　性格基因\n你是個執著樂觀的人，對人生的看法充滿熱忱和幾分難得的孩子氣。重視\n情感的你很容易被打動，正因為如此，經常受制於人情壓力，且因為情感付出\n太多，最後被毫無保留的傷害而深感痛苦不已。你的想法單純，不夠世故是你\n的優點，也是缺點。\n生命路線\n你需要更理性地厘清自己的需要，不要順著感情做判斷和過日子。你已經\n耗費很多時間與心力在成就他人，和滿足自己的情緒感動，剩下來的時間，你\n應該學著為自己訂出原則。保持生命的熱忱很重要，但請不要忘了也要善待自\n己，過濾朋友和予取予求的家人，或是與情人保持距離，是你要加強的務實理\n性生存態度，千萬不要過分燃燒自己，最後只是為了照亮他人。")        
        self.go_back()   
    def on_exit_q2(self,event):
        print("Leaving state2")
    def on_exit_q4(self,event):
        print("Leaving state4")
    def on_exit_q5(self,event):
        print("Leaving state5")
     def on_exit_restart(self,event):
        print("Leaving restart")
    def on_exit_a(self):
        print("Leaving a")
    def on_exit_b(self):
        print("Leaving b")
    def on_exit_c(self):
        print("Leaving c")
    def on_exit_d(self):
        print("Leaving d")