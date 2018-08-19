#include <stdio.h>


int binarySearch(const int array[], int x, int length)
{
    int low,high,mid;
    low = 0;
    high = length-1;
    while (low <= high) {
        mid = (low+high)/2;
        if(x < array[mid])
            high = mid-1;
        else if ( x > array[mid])
            low = mid+1;
        else
            return mid;
    }
    return -1;
}

int main(int argc, char const *argv[]) {

    
    return 0;
}
