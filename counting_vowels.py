def count_vowels(s):
    count = 0
    vowels = ['a','e','i','o','u']
    for c in s:
        if vowels.__contains__(c):
            count = count + 1
    print 'Number of vowels {}'.format(count)

if __name__ == '__main__':
    countVowels('This one has a couple of vowels')