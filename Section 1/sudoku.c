int isValidSudoku(const char** A, int n1) {
    int i,j,k,p,q,m,n;
    for(i=0;i<n1;i++)
    {
        for(j=0;j<n1;j++)
        {
            if(A[i][j]!='.')
            {
                for(k=(j+1);k<n1;k++) //row check
                {
                    if(A[i][j]==A[i][k])
                    {
                        return 0;
                    }
                }
                
                for(k=(i+1);k<n1;k++) //col check
                {
                    if(A[i][j]==A[k][j])
                    {
                        return 0;
                    }
                }
                
                m=i/3; //box check
                n=j/3;
                for(p=(3*m)+0;p<(3*m)+3;p++)
                {
                    for(q=(3*n)+0;q<(3*n)+3;q++)
                    {
                        if(A[i][j]==A[p][q] && ((i!=p) && (j!=q)))
                        {
                            return 0;
                        }
                    }
                }
            }
        }
    }
    return 1;
}