#include<iostream>
main()
{
	int i;
    string s="xybobobob";
    string g;
    int z =s.length();`
    
    for(i=0;i<z;i++)
    {
        j=i+1;
        k=i+2;
        g[0]=s[i];
        g[1]=s[j];
        g[2]=s[k];
        if (g=="bob") {
            q++;
            i++;
            g[0]='m';
            g[1]='m';
            g[2]='m';
        }
    }
    cout <<"The number of times bob %d", q;
    

}