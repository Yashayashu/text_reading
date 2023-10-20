def count_unique_words(filename):
    word_count = {}
    with open(filename, 'r') as file:
        
        for line in file:
            words = line.split()
            for word in words:
                
                word = word.strip('.,!?()[]{}"\'').lower()
                
                
                if word not in word_count:
                    word_count[word] = 1
                else:
                    
                    word_count[word] += 1

    
    for word, count in word_count.items():
        print(f"{word}: {count}")

if __name__ == "__main__":
    filename = "C:\\Users\\YASHASWINI.B.V\\Desktop\\txtt.txt"  
    count_unique_words(filename)
