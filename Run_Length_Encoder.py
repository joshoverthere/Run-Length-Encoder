
def encode(message):
    encodedMessage = ""

    #remove substrings of identical characters from the main string until it has length 0...
    while len(message)>0:
        #count tracks number of identical chars, eg 000 or 111, in string so far
        count = 0
        
        #while current letter is the same as the next letter
        while message[count:count+1] == message[count+1:count+2]:
            #increment number of identical chars 
            count += 1

        currentChar = message[0]
        
        message = message[count+1:len(message)]

        #increment by 1 since indexing starts at 0 but quantities start at 1
        count += 1;

        encodedMessage += str(count) + currentChar

    return encodedMessage


def main():
    while (1):
        message = "001100110011"
        while len(message)<1:
            message = input("Enter message to encode: ")
        print("Encoded message: ", encode(message))
        input()

main()





