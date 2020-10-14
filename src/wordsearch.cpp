//simple puzzle generation

#include <iostream>
#include <string>
#include <time.h>
using namespace std;

int random(int min, int max) //range : [min, max]
{
   static bool first = true;
   if (first) 
   {  
      srand( time(NULL)); //seeding for the first time only!
      first = false;
   }
   return min + rand() % (( max + 1 ) - min);
}

const int rows = 15 , cols = 15;
const int wordlistSize = 15;
string puzzle[rows][cols];
string wordList[wordlistSize] = {"turbo","food","zombie","alien","human","lambda","word","search","puzzle","games","program","loser","cipher","dog","man"};
void placeHorizontal(int r,int c , string word) {
   for(int i = 0; i <= word.size(); i++) {
      puzzle[r][c++] = word[i];
   }
}

bool canPlaceHorizontally(int c , int size) {
   return(c-size == 0);
}

bool isAllClearHorizontally(int r , int c , string word) {
   if(canPlaceHorizontally(c,word.size())) {
      for(int i = 0; i <= word.size(); i++) {
         if(puzzle[r][c++] != " ") {
            return false;
            break;
         }
      }
   } return true;
}

void placeVertically(int r,int c , string word) {
   for(int i = 0; i <= word.size(); i++) {
      puzzle[r++][c] = word[i];
   }
}

bool canPlaceVertically(int r , int size) {
   return(r-size == 0);
}

bool isAllClearVertically(int r , int c , string word) {
   if(canPlaceVertically(r,word.size())) {
      for(int i = 0; i <= word.size(); i++) {
         if(puzzle[r++][c] != " ") {
            return false;
            break;
         }
      }
   } return true;
}

void placeDiagnolly(int r,int c,string word) {
   for(int i = 0; i <= word.size(); i++) {
      puzzle[r++][c++] = word[i];
   }
}

bool canPlaceDiagnolly(int r , int c , int size) {
   return(r <= size && c <= size);
}

bool isAllClearDiagnolly(int r , int c , string word) {
   if(canPlaceDiagnolly(r,c,word.size())) {
      for(int i = 0; i <= word.size(); i++) {
         if(puzzle[r++][c++] != " ") {
            return false;
            break;
         }
      }
   } return true;
}

bool generatePlace(string word) {

      //Generate random position for a word
      int r = random(0,rows-1);
      int c = random(0,cols-1);

      if(!canPlaceHorizontally(c,word.size())) {
         if(!canPlaceVertically(r,word.size())) {
            if(!canPlaceDiagnolly(r,c,word.size())) {
               return false;
            } else {
               if(isAllClearDiagnolly(r,c,word)) {
                  placeDiagnolly(r,c,word);    
                  return true; 
               }
            }
         } else {
            if(isAllClearVertically(r,c,word)) {
               placeVertically(r,c,word);
               return true;
            }
         }
      } else {
         if(isAllClearHorizontally(r,c,word)) {
            placeHorizontal(r,c,word);
            return true;
         }
      }   
}

void puzzleReset() {
    //Initialize list
   for(int i = 0; i <= rows-1; i++) {
      for(int j = 0; j <= cols-1; j++) {
         puzzle[i][j] = " ";
      }
   }
}

int main() {

   //Initialize list
   for(int i = 0; i <= rows-1; i++) {
      for(int j = 0; j <= cols-1; j++) {
         puzzle[i][j] = " ";
      }
   }

   int generatedWords = 0;
   bool flag = false;
   while(generatedWords <= wordlistSize)
   {
      if(!flag) {
         flag = generatePlace(wordList[generatedWords]);
      } else {
         generatedWords += 1;
         flag = false;
      }

   }

/*
   //Fill empty with random
   for(int i = 0; i <= rows-1; i++) {
      for(int j = 0; j <= cols-1; j++) {
         if(puzzle[i][j] == " ") { puzzle[i][j] = random(97,122);}
      }
   }
*/
   //Print the list
   for(int i = 0; i <= rows-1; i++) {
      for(int j = 0; j <= cols-1; j++) {
         cout << puzzle[i][j];
      } cout << "\n";
   }
}