#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <stdbool.h>






#define FILENAME	"../01.txt"

#define LED_CNT		60


int main (void)
{

   FILE * fp;
   int i;
   /* open the file for writing*/
   fp = fopen ( FILENAME,"w");


   uint8_t color_r = 0;
   uint8_t color_g = 0;
   uint8_t color_b = 0;
 
	for (int j = 0; j < 255; j += 20) {
		color_r = j;
		for (i = 0; i < LED_CNT;i++) {
			fprintf (fp, "%d=%d,%d,%d\n", i, color_r, color_g, color_b);
	    }
	}


	for (int j = 0; j < 255; j += 20) {
		color_g = j;
		for (i = 0; i < LED_CNT;i++) {
			fprintf (fp, "%d=%d,%d,%d\n", i, color_r, color_g, color_b);
	    }
	}



	for (int j = 0; j < 255; j += 20) {
		color_b = j;
		for (i = 0; i < LED_CNT;i++) {
			fprintf (fp, "%d=%d,%d,%d\n", i, color_r, color_g, color_b);
	    }
	}
	/////////

	for (int j = 255; j > 0; j -= 20) {
		color_r = j;
		for (i = 0; i < LED_CNT;i++) {
			fprintf (fp, "%d=%d,%d,%d\n", i, color_r, color_g, color_b);
	    }
	}


	for (int j = 255; j > 0; j -= 20) {
		color_g = j;
		for (i = 0; i < LED_CNT;i++) {
			fprintf (fp, "%d=%d,%d,%d\n", i, color_r, color_g, color_b);
	    }
	}



	for (int j = 255; j > 0; j -= 20) {
		color_b = j;
		for (i = 0; i < LED_CNT;i++) {
			fprintf (fp, "%d=%d,%d,%d\n", i, color_r, color_g, color_b);
	    }
	}







   /* close the file*/  
   fclose (fp);
   printf("File %s created.\n", FILENAME);
	return 0;
}