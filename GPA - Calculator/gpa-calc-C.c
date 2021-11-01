//This program will accept GPA values from a txt file and compute GPA.
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

float grv(char []);
void calc(FILE *, float []);

int main(void) {
  FILE *fp;
  float qnc[2];   //Array that contains the quality points and the total credit hours
  float GPA;
  qnc[0] = 0;
  qnc[1] = qnc[0];

  fp = fopen("C:\\Users\\Surajkmar\\Documents\\GPA.txt","r");
  calc(fp,qnc);
  fclose(fp);
  GPA = qnc[0] / qnc[1];
  printf("\nGPA: %0.2f\n",GPA);
  printf("Quality hours: %0.2f\n", qnc[0]);
  printf("Credit hours: %0.2f\n", qnc[1]);
  fclose(fp);
  return(0);
}

/*This function will return the quality point earned by achieving a certain grade
  eg: input (A)  -> output 4.0
      input (B-) -> output 2.7
*/
float grv(char a[]) {
  float q = 0; //This is the quality of the grade earned
  char comp[4];

  if (!strcmp(a,"A+")) {
    q = 4.0;
  }
  if (!strcmp(a,"A")) {
    q = 4.0;
  }
  if (!strcmp(a,"A-")) {
    q = 3.7;
  }
  if (!strcmp(a,"B+")) {
    q = 3.3;
  }
  if (!strcmp(a,"B")) {
    q = 3.0;
  }
  if (!strcmp(a,"B-")) {
    q = 2.7;
  }
  if (!strcmp(a,"C+")) {
    q = 2.3;
  }
  if (!strcmp(a,"C")) {
    q = 2.0;
  }
  if (!strcmp(a,"C-")) {
    q = 1.7;
  }
  if (!strcmp(a,"D+")) {
    q = 1.3;
  }
  if (!strcmp(a,"D")) {
    q = 1.0;
  }
  if (!strcmp(a,"D-")) {
    q = 0.7;
  }
  if (!strcmp(a,"F")) {
    q = 0;
  }
  if (!strcmp(a, "W")) {
    q = 0;
  }
 return(q);
}

// This function will calculate and change the input array to have the quality points and total credit hours calculated
void calc(FILE *a, float b[]) {
  char str1[5];
  char str2[2];
  int credits;
  float value;  //Quality points earned
  int code;     //Course number
  int ch_chk;   //Checks if there are stoppers

  while (feof(a) == 0) {
    ch_chk = fscanf(a,"\t%s%d\t\t%d\t\t%s ",str1,&code,&credits,str2);

    if (ch_chk != 4) { //Makes stoppers work
      break;
    }
    if (!(strcmp(str2,"P")) || (!strcmp(str2,"NP")) || (!strcmp(str2, "WF")) || (!strcmp(str2,("W")))) {   //Statement that deals with P/NP option & other miscellaneous grades
      credits = 0;
    } 
    b[0] += (float)credits * grv(str2);
    b[1] += (float)credits;
  }
}