#include <cstdio>

int main(int argc, char** argv){

#ifdef DEBUG
    if(argc<2 || NULL == freopen(argv[1],"r",stdin)) {
        printf("can't open file\n");
        return -1;
    }
#endif
    return 0;

}
