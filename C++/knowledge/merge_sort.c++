#include<iostream>
#include<vector>
using namespace std;
vector<int> merge_sort(vector<int> &left, vector<int> &right){
    vector<int> result;
    int i=0, j=0;
    while(i<left.size() && j<right.size()){
        if(left[i] < right[j]){
            result.push_back(left[i]);
            i++;
        }
        else{
            result.push_back(right[j]);
            j++;
        }
    }
    while(i<left.size()){
        result.push_back(left[i]);
        i++;
    }
    while(j<right.size()){
        result.push_back(right[j]);
        j++;
    }
    return result;
}   
vector<int> merge(vector<int> &array){
    if (array.size() == 1){
        return array;
    }
    int mid = array.size()/2;

    vector<int> left(array.begin(), array.begin()+mid);
    vector<int> right(array.begin()+ mid, array.end());
    vector<int> left_m = merge(left);
    vector<int> right_m = merge(right);
    return merge_sort(left_m, right_m);
}

int main(){
    vector<int> array = {11, 465 ,564, 4, 2, 7, 8, 9, 1, 0};
    vector<int> sorted_array = merge(array);
    for(int i=0; i<sorted_array.size(); i++){
        cout<<sorted_array[i]<<" ";
    }
    return 0;
}