
def sequential(List, target):
    ''' of course we would easely say (if target in List: return True)'''
    ''' search for target in list and return true if exist '''
    for i in range(len(List)):
        if List[i] == target:
            return True
    return False

if __name__ == '__main__':
    arr = list(map(int, input().split()))
    to_find = int(input())

    print(sequential(arr, to_find))