#include <stdio.h>
#include <limits.h>
// given that you can buy stock at a cheaper price and sell it at a later date,
// what is the max profit you can get?
int getMaxProfit(int *p){
    int minPrice=INT_MAX;
    int maxProfit=0;
    
    for(int i=0; i<6; i++){
        if(p[i] < minPrice) minPrice=p[i];
        else{
    if((p[i] - minPrice) > maxProfit) maxProfit=p[i]-minPrice;
        }
    }
    return maxProfit;
}

int main()
{
    
    int stockPrice[6]={7,1,5,3,6,4};
    
    printf("%d",getMaxProfit(stockPrice));
    // prints 5 i.e stock bought at $1 and sold at $6
    
    return 0;
}
