#!/user/bin/python

years = '7';
guess = 0;
q = input('How many years have we been together Mick?');
max = 5;

guess = guess + 1 

while q != years and guess < max:
    print("No that's incorrect!")
    q = input("How about we attempt another number?")
    guess = guess + 1

if guess == max and years != q:
    print("Too bad, you couldnt't get it.  The answer was", years)

else:
    print("Great job, you guessed correctly! It took", guess + 1, 'tries',)


