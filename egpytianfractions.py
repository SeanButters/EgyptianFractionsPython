
#takes a numerator and denominator of fraction
#returns string of egyptian unit fractions that make up the given fractions
def egyptianFract(num, den):
    return greedy(num, den)[:-2] + "= "+str(num)+"/"+str(den) #returns the string result of greedy + " = num/den"

#greedy algorithim
def greedy(num, den):
    #continue loop
    if(num>0):
        n = 0 #n declaration so compiler is happy

        if(greedy(((-1 *den)%num), den*n)== ""): #last fraction in sequence
            n = den//num  #n = den/num rounded down to integer
        else: #not the last fraction
            n = den//num +  1 #n = den/num rounded up to next integer
        return "1/"+str(n)+" + " +greedy(((-1 *den)%num), den*n) #returns (1/(n))+greedy((-den%num)/(den*(n)))
    #end loop
    else:
        return ""




def main():
    print(egyptianFract(int(input("Enter numerator: ")), int(input("Enter denominator: "))))

if __name__ == "__main__":
    main()