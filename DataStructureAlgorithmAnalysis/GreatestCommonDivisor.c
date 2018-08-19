#include <stdio.h>

//欧几里德算法
//O(logN)
int euclidean(int n, int m)
{
    int rem;
    while (m > 0) {
        rem = n % m;
        n = m;
        m = rem;
    }
    return n;

}
int main(int argc, char const *argv[]) {

    return 0;
}
