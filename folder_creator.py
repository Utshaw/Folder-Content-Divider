import os



def main():
    '''
    Creates 212 files under dummy directory
    
    '''
    dummyDir = 'dummy'
    if not os.path.exists(dummyDir):
        os.mkdir('dummy')
    os.chdir('dummy')
    for i in range(0, 212):
        open(str(i) + '.txt', 'a').close()


if __name__ == "__main__":
    main()