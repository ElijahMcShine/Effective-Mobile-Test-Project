#include "fcgi_stdio.h"
#include <stdlib.h>

int main(void)
{
    while(FCGI_Accept() >= 0)
    {
        printf("Status: 200 OK\r\n");
        printf("Content-type: text/html\r\n\r\n");
        printf("<!doctype><html><head><title>Hello from Effective Mobile!</title></head>\n");
        printf("<body><p>Hello from Effective Mobile!</p>\n");
        printf("</body></html>\n");
    }

    return 0;
}
