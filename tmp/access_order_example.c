#include <stdlib.h>
#include "rlxutils.h"

void ji(char *arr, long SIZE) {
    long i,j;
    for (j=0; j<SIZE; j++) {
     for (i=0; i<SIZE; i++) {
         arr[i+SIZE*j]++;
     }
    }
}

void ij(char *arr, long SIZE) {
    long i,j;
    for (i=0; i<SIZE; i++) {
       for (j=0; j<SIZE; j++) {
           arr[i+SIZE*j]++;
       }
    }
}

int main(int argc, char **argv) {
    struct timespec tsi, tsf;
    long N = 10;  
    long i,j,k,s;
    double time_diff;

    char *fname = "tmp/Carrays.data";
    printf ("writing to file %s and stdout\n", fname);
    FILE *f = fopen(fname, "w");
    if (f == NULL)
    {
        printf("Error opening file %s\n",fname);
        exit(1);
    }

    double time_ij[N];
    double time_ji[N];

    long sizes[] = {8, 16, 32, 64, 128, 384, 512, 640, 768, 1024, 1536, 2048, 2560,3072, 3584};

    long ssizes = sizeof(sizes)/sizeof(long);
    char *header = "iteration array_size elapsed_time_ij elapsed_time_ji\n";
    printf(    "%s", header);
    fprintf(f, "%s", header);

    for (s=0; s<ssizes; s++) {
      long array_size = sizes[s];
      for (k=0; k<N; k++) {

          char *arr = malloc(array_size*array_size*sizeof(char));
          current_utc_time(&tsi);
          ij(arr, array_size);
          current_utc_time(&tsf);
          time_ij[k] = get_time_diff(tsi, tsf);

          current_utc_time(&tsi);
          ji(arr, array_size);
          current_utc_time(&tsf);
          time_ji[k] = get_time_diff(tsi, tsf);

          free(arr);
      }
      double total_array_size = power(sizes[s],2);
      printf(    "%lu %3.10f %lf %lf\n",s, total_array_size/1024, avg(time_ij, N), avg(time_ji,N));
      fprintf(f, "%lu %3.10f %lf %lf\n",s, total_array_size/1024, avg(time_ij, N), avg(time_ji,N));

    }
    fclose(f);
    return 0; 

}