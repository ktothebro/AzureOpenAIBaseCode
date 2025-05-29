from classifier import classify_ticket

if __name__ == '__main__':
    ticket = input('Enter IT ticket description: ')
    print('Category:', classify_ticket(ticket))