# Author : Tunç Gürsoy 24/02/2021
# Define : Operation class for the given TEXT ANALYZER challenge
# Functionality : Class can
# 1-Calculate word count with @calculateWordCount function
# 2-Calculate letter count with @letterCount function
# 3-Find longest keyword with @longest function
# 4-Find median word with @med_word
# 5-Calculate median word letter count with @med_word_count
# 6-Detect language with @detect_Language
# 6-Find Duration with @duration
# 6-Find average word length with @avgLength
class operation:
    text = ""
    orj = ""
    list = []
    requests = []
    en_stop = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
               "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
               "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
               "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
               "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
               "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
               "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under",
               "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both",
               "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so",
               "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
    tr_stop = ["a", "acaba", "altı", "altmış", "ama", "ancak", "arada", "artık", "asla", "aslında", "aslında", "ayrıca",
               "az", "bana", "bazen", "bazı", "bazıları", "belki", "ben", "benden", "beni", "benim", "beri", "beş",
               "bile", "bilhassa", "bin", "bir", "biraz", "birçoğu", "birçok", "biri", "birisi", "birkaç", "birşey",
               "biz", "bizden", "bize", "bizi", "bizim", "böyle", "böylece", "bu", "buna", "bunda", "bundan", "bunlar",
               "bunları", "bunların", "bunu", "bunun", "burada", "bütün", "çoğu", "çoğunu", "çok", "çünkü", "da",
               "daha", "dahi", "dan", "de", "defa", "değil", "diğer", "diğeri", "diğerleri", "diye", "doksan", "dokuz",
               "dolayı", "dolayısıyla", "dört", "e", "edecek", "eden", "ederek", "edilecek", "ediliyor", "edilmesi",
               "ediyor", "eğer", "elbette", "elli", "en", "etmesi", "etti", "ettiği", "ettiğini", "fakat", "falan",
               "filan", "gene", "gereği", "gerek", "gibi", "göre", "hala", "halde", "halen", "hangi", "hangisi", "hani",
               "hatta", "hem", "henüz", "hep", "hepsi", "her", "herhangi", "herkes", "herkese", "herkesi", "herkesin",
               "hiç", "hiçbir", "hiçbiri", "i", "ı", "için", "içinde", "iki", "ile", "ilgili", "ise", "işte",
               "itibaren", "itibariyle", "kaç", "kadar", "karşın", "kendi", "kendilerine", "kendine", "kendini",
               "kendisi", "kendisine", "kendisini", "kez", "ki", "kim", "kime", "kimi", "kimin", "kimisi", "kimse",
               "kırk", "madem", "mi", "mı", "milyar", "milyon", "mu", "mü", "nasıl", "ne", "neden", "nedenle", "nerde",
               "nerede", "nereye", "neyse", "niçin", "nin", "nın", "niye", "nun", "nün", "o", "öbür", "olan", "olarak",
               "oldu", "olduğu", "olduğunu", "olduklarını", "olmadı", "olmadığı", "olmak", "olması", "olmayan", "olmaz",
               "olsa", "olsun", "olup", "olur", "olur", "olursa", "oluyor", "on", "ön", "ona", "önce", "ondan", "onlar",
               "onlara", "onlardan", "onları", "onların", "onu", "onun", "orada", "öte", "ötürü", "otuz", "öyle",
               "oysa", "pek", "rağmen", "sana", "sanki", "sanki", "şayet", "şekilde", "sekiz", "seksen", "sen",
               "senden", "seni", "senin", "şey", "şeyden", "şeye", "şeyi", "şeyler", "şimdi", "siz", "siz", "sizden",
               "sizden", "size", "sizi", "sizi", "sizin", "sizin", "sonra", "şöyle", "şu", "şuna", "şunları", "şunu",
               "ta", "tabii", "tam", "tamam", "tamamen", "tarafından", "trilyon", "tüm", "tümü", "u", "ü", "üç", "un",
               "ün", "üzere", "var", "vardı", "ve", "veya", "ya", "yani", "yapacak", "yapılan", "yapılması", "yapıyor",
               "yapmak", "yaptı", "yaptığı", "yaptığını", "yaptıkları", "ye", "yedi", "yerine", "yetmiş", "yi", "yı",
               "yine", "yirmi", "yoksa", "yu", "yüz", "zaten", "zira"]

    def __init__(self, text):
        self.list = []
        self.requests = []
        self.text = text
        self.orj = self.text
        self.orj = self.orj.replace('\n', ' ')
        self.text = self.text.replace(',', ' ')
        self.text = self.text.replace('\n', ' ')
        arr = self.text.split(" ")
        for i in arr:
            if i != '':
                self.list.append(i)

    def calculateWordCount(self):
        self.list = []
        arr = self.text.split(" ")
        for i in arr:
            if i != '':
                self.list.append(i)
        return len(self.list)

    def letterCount(self):
        count = 0
        for i in self.orj:
            count += len(i)
        return count

    def longest(self):
        max = -1
        longest = ""
        for i in self.list:
            if len(i) > max:
                max = len(i)
                longest = i
        return longest

    def med_word(self):
        totalcount = self.calculateWordCount()
        med = int(totalcount / 2)
        result = self.list[med]
        return result

    def med_word_count(self):
        return len(self.med_word())

    def detect_Language(self):
        en_count = 0
        tr_count = 0
        for i in self.list:
            for t in self.en_stop:
                if (i == t):
                    en_count += 1
                    break
            for t in self.tr_stop:
                if (i == t):
                    tr_count += 1
                    break
        if en_count > tr_count:
            return "en"
        elif en_count < tr_count:
            return "tr"
        else:
            return "Unknown"
    def duration(self):
        return int(self.letterCount()/2)
    def avgLength(self):
        return float(self.letterCount()/self.calculateWordCount())


#Test Part
if __name__ == '__main__':
    dump = operation("Dee pressure or deep touch pressure is a form of tactile sensory input. This input is most "
                     "often delivered through firm holding, cuddling, hugging, firm stroking, "
                     "and squeezing.\n\nHowever, before we get into too much detail about deep touch pressure, "
                     "we need to understand our body’s sensory system and why deep touch pressure emerged in the "
                     "first place.\n\nNeurologically, sensory processing is how we feel. Through processing "
                     "sensory input, we make sense of the world around us. In everything we do, we are receiving "
                     "sensory messages from both our bodies and the surrounding world.")
    print(dump.calculateWordCount())
    print(dump.letterCount())
    print(dump.longest())
    print(str(dump.med_word()))
    print(dump.med_word_count())
    print(dump.detect_Language())
